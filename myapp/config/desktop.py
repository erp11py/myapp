# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"module_name": "Myapp",
			"color": "grey",
			"icon": "a",
			"type": "module",
			"label": _("Myapp")
		}
	]
