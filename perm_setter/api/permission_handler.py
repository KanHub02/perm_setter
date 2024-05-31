import frappe
import json

@frappe.whitelist()
def get_all_doctypes():
    doctypes = frappe.get_all("DocType", fields=["name"])
    return doctypes

@frappe.whitelist()
def get_permissions(doctype):
    permissions = frappe.get_all("DocPerm", filters={"parent": doctype}, fields=["role", "read", "write", "create", "delete", "print", "email", "export", "report", "share"])
    return permissions


@frappe.whitelist()
def grant_permissions(doctype, role, permissions):
    print("-----------------------------",doctype)
    if not frappe.session.user:
        frappe.throw("You must be logged in to perform this action.", frappe.PermissionError)
    if not frappe.has_permission(doctype, "write"):
        frappe.throw("You do not have permission to modify permissions for this DocType.", frappe.PermissionError)

    permissions_dict = json.loads(permissions)

    if not frappe.db.exists('Role', 'Permission Provider'):
        frappe.get_doc({'doctype': 'Role', 'role_name': 'Permission Provider'}).insert()

    user_roles = frappe.get_roles(frappe.session.user)
    print(user_roles)
    if 'Permission Provider' not in user_roles:
        frappe.throw("You must have 'Permission Provider' role to grant permissions.", frappe.PermissionError)

    existing_perm = frappe.get_all('DocPerm', filters={'parent': doctype, 'role': role}, fields=['name'])
    docperm = frappe.new_doc('DocPerm')
    docperm.update({
        'parent': doctype,
        'parentfield': 'permissions',
        'parenttype': 'DocType',
        'role': role,
        'read': permissions_dict.get('read', 0),
        'write': permissions_dict.get('write', 0),
        'create': permissions_dict.get('create', 0),
        'delete': permissions_dict.get('delete', 0)
    })
    if existing_perm:
        docperm.name = existing_perm[0]['name']
        docperm.db_update()
    else:
        docperm.insert()
    
    frappe.db.commit()
    return "Permissions updated successfully."
