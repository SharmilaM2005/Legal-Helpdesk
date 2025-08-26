app_name = "legal_helpdesk"
app_title = "Legal Helpdesk"
app_publisher = "Frappe Technologies"
app_description = "Customer Service Software"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "hello@frappe.io"
app_license = "AGPLv3"

add_to_apps_screen = [
    {
        "name": "legal_helpdesk",
        "logo": "/assets/legal_helpdesk/desk/favicon.svg",
        "title": "Legal Helpdesk",
        "route": "/legal_helpdesk",
        "has_permission": "legal_helpdesk.api.permission.has_app_permission",
    }
]

after_install = "legal_helpdesk.setup.install.after_install"
after_migrate = [
    "legal_helpdesk.search.build_index_in_background",
    "legal_helpdesk.search.download_corpus",
]

scheduler_events = {
    "all": [
        "legal_helpdesk.search.build_index_if_not_exists",
        "legal_helpdesk.search.download_corpus",
    ],
    "daily": [
        "legal_helpdesk.legal_helpdesk.doctype.hd_ticket.hd_ticket.close_tickets_after_n_days"
    ],
}

website_route_rules = [
    {
        "from_route": "/legal_helpdesk/<path:app_path>",
        "to_route": "legal_helpdesk",
    },
]

doc_events = {
    "Contact": {
        "before_insert": "legal_helpdesk.overrides.contact.before_insert",
    },
    "Assignment Rule": {
        "on_trash": "legal_helpdesk.extends.assignment_rule.on_assignment_rule_trash",
    },
}

has_permission = {
    "HD Ticket": "legal_helpdesk.legal_helpdesk.doctype.hd_ticket.hd_ticket.has_permission",
}

permission_query_conditions = {
    "HD Ticket": "legal_helpdesk.legal_helpdesk.doctype.hd_ticket.hd_ticket.permission_query",
}

# DocType Class
# ---------------
# Override standard doctype classes
override_doctype_class = {
    "Email Account": "legal_helpdesk.overrides.email_account.CustomEmailAccount",
}

ignore_links_on_delete = [
    "HD Notification",
    "HD Ticket Comment",
]

# setup wizard
# setup_wizard_requires = "assets/legal_helpdesk/js/setup_wizard.js"
# setup_wizard_stages = "legal_helpdesk.setup.setup_wizard.get_setup_stages"
setup_wizard_complete = "legal_helpdesk.setup.setup_wizard.setup_complete"

# Testing
# ---------------
before_tests = "legal_helpdesk.test_utils.before_tests"
