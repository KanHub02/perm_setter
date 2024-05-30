import frappe

@frappe.whitelist()
def check_permissions(doctype):
    if not frappe.session.user:
        frappe.throw("You must be logged in to access this functionality.", frappe.PermissionError)
    if not frappe.has_permission(doctype, "read"):
        frappe.throw("You do not have the necessary permissions to check this DocType.", frappe.PermissionError)

    try:
        permissions = frappe.get_all('DocPerm', fields=['role', 'permlevel', 'read', 'write', 'create', 'delete'], filters={'parent': doctype})
        roles_with_permissions = {}
        for perm in permissions:
            role = perm['role']
            if role not in roles_with_permissions:
                roles_with_permissions[role] = {
                    'permlevel': perm['permlevel'],
                    'read': perm['read'],
                    'write': perm['write'],
                    'create': perm['create'],
                    'delete': perm['delete']
                }
        return roles_with_permissions
    except Exception as e:
        frappe.throw(f"Error checking permissions: {str(e)}")

@frappe.whitelist()
def grant_permissions(doctype, role, permissions):
    if not frappe.session.user:
        frappe.throw("You must be logged in to perform this action.", frappe.PermissionError)
    if not frappe.has_permission(doctype, "write"):
        frappe.throw("You do not have permission to modify permissions for this DocType.", frappe.PermissionError)

    if not frappe.db.exists('Role', 'Permission Provider'):
        frappe.get_doc({'doctype': 'Role', 'role_name': 'Permission Provider'}).insert()

    user_roles = frappe.get_roles(frappe.session.user)
    if 'Permission Provider' not in user_roles:
        frappe.throw("You must have 'Permission Provider' role to grant permissions.", frappe.PermissionError)

    existing_perm = frappe.get_all('DocPerm', filters={'parent': doctype, 'role': role}, fields=['name'])
    docperm = frappe.new_doc('DocPerm')
    docperm.update({
        'parent': doctype,
        'parentfield': 'permissions',
        'parenttype': 'DocType',
        'role': role,
        'read': permissions.get('read', 0),
        'write': permissions.get('write', 0),
        'create': permissions.get('create', 0),
        'delete': permissions.get('delete', 0)
    })
    if existing_perm:
        docperm.name = existing_perm[0]['name']
        docperm.db_update()
    else:
        docperm.insert()
    
    frappe.db.commit()
    return "Permissions updated successfully."
