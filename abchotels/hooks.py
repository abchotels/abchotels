# -*- coding: utf-8 -*-
from . import __version__ as app_version

app_name = "abchotels"
app_title = "ABC Hotels"
app_publisher = "Your Name"
app_description = "Custom app for hotel management"
app_icon = "octicon octicon-home"
app_color = "blue"
app_email = "your.email@example.com"
app_license = "MIT"

app_include_css = "/assets/abchotels/css/abchotels.css"
app_include_js = "/assets/abchotels/js/abchotels.js"

desk_page = {"ABC Hotels": "abchotels/workspace/abc_hotels"}

website_include_js = ["/assets/abchotels/js/website.js"]

website_route_rules = [
    {"from_route": "/abchotels/<path:app_path>", "to_route": "abchotels"}
]

fixtures = [
    "Bed Type",
    "Property",
    "Room Category",
    "Room Type",
    "Room Type Room",
    "Room Type Room Bed",
    # the main workspace doc(s)
    {"doctype": "Workspace", "filters": [["module", "in", ["ABC Hotels"]]]},
    # children / related items shown on the workspace
    {"doctype": "Workspace Link", "filters": [["parent", "in", ["ABC Hotels"]]]},
    {"doctype": "Workspace Shortcut", "filters": [["parent", "in", ["ABC Hotels"]]]},
    {"doctype": "Workspace Permission", "filters": [["parent", "in", ["ABC Hotels"]]]},
    # include cards if you used them
    {"doctype": "Number Card", "filters": [["module", "in", ["ABC Hotels"]]]},
]
