app_name = "perm_setter"
app_title = "perm_setter"
app_publisher = "@KanHub02"
app_description = "App for check linked(DocType) frappe.session permission"
app_email = "usmnvk.work@gmail.com"
app_license = "mit"
# required_apps = []

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/perm_setter/css/perm_setter.css"
# app_include_js = "/assets/perm_setter/js/perm_setter.js"

# include js, css files in header of web template
# web_include_css = "/assets/perm_setter/css/perm_setter.css"
# web_include_js = "/assets/perm_setter/js/perm_setter.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "perm_setter/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "perm_setter/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "perm_setter.utils.jinja_methods",
# 	"filters": "perm_setter.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "perm_setter.install.before_install"
# after_install = "perm_setter.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "perm_setter.uninstall.before_uninstall"
# after_uninstall = "perm_setter.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "perm_setter.utils.before_app_install"
# after_app_install = "perm_setter.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "perm_setter.utils.before_app_uninstall"
# after_app_uninstall = "perm_setter.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "perm_setter.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"perm_setter.tasks.all"
# 	],
# 	"daily": [
# 		"perm_setter.tasks.daily"
# 	],
# 	"hourly": [
# 		"perm_setter.tasks.hourly"
# 	],
# 	"weekly": [
# 		"perm_setter.tasks.weekly"
# 	],
# 	"monthly": [
# 		"perm_setter.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "perm_setter.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "perm_setter.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "perm_setter.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["perm_setter.utils.before_request"]
# after_request = ["perm_setter.utils.after_request"]

# Job Events
# ----------
# before_job = ["perm_setter.utils.before_job"]
# after_job = ["perm_setter.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"perm_setter.auth.validate"
# ]

api_methods = {
    "perm_setter.api.permission_handler.get_all_doctypes": "perm_setter.api.permission_handler.get_all_doctypes",
    "perm_setter.api.permission_handler.get_permissions": "perm_setter.api.permission_handler.get_permissions",
    "perm_setter.api.permission_handler.grant_permissions": "perm_setter.api.permission_handler.grant_permissions",
}

fixtures = [    
            "Role",
           ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

