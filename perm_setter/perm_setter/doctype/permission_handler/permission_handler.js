frappe.ui.form.on('Permission Handler', {
    refresh: function (frm) {
        frm.fields_dict['search'].get_query = function () {
            return {
                filters: {
                    name: ['not in', ['DocType', 'Module Def']] 
                }
            };
        };
        frm.add_custom_button(__('Get Permissions'), function() {
            const doctype = frm.doc.search;
            if (doctype) {
                frappe.call({
                    method: "perm_setter.api.permission_handler.get_permissions",  
                    args: {doctype: doctype},
                    callback: function(r) {
                        if (r.message) {
                            console.log("Permissions:", r.message);
                            let message = JSON.stringify(r.message, null, 4); 
                            frappe.msgprint('<pre>' + message + '</pre>', __('Permissions for ' + doctype));
                        }
                    }
                });
            } else {
                frappe.msgprint(__('Please select a DocType first.'));
            }
        });
        frm.add_custom_button(__('Grant Permissions'), function() {
            var dialog = new frappe.ui.Dialog({
                title: __("Enter Details"),
                fields: [
                    {
                        label: 'Role',
                        fieldname: 'role',
                        fieldtype: 'Link',
                        options: 'Role'
                    },
                    {
                        label: 'Read',
                        fieldname: 'read',
                        fieldtype: 'Check'
                    },
                    {
                        label: 'Write',
                        fieldname: 'write',
                        fieldtype: 'Check'
                    },
                    {
                        label: 'Create',
                        fieldname: 'create',
                        fieldtype: 'Check'
                    },
                    {
                        label: 'Delete',
                        fieldname: 'delete',
                        fieldtype: 'Check'
                    }
                ],
                primary_action_label: __("Grant"),
                primary_action(values) {
                    frappe.call({
                        method: "perm_setter.api.permission_handler.grant_permissions",
                        args: {
                            doctype: frm.doc.search,
                            role: values.role,
                            permissions: {
                                read: values.read,
                                write: values.write,
                                create: values.create,
                                delete: values.delete
                            }
                        },
                        callback: function(r) {
                            if (!r.exc) {
                                frappe.msgprint(__('Permissions granted successfully'));
                                dialog.hide();
                            }
                        }
                    });
                }
            });
            dialog.show();
        });
            
        
    }
});