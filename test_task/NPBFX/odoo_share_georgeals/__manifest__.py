# -*- coding: utf-8 -*-
{
    'name': "OdooShare_georgeals",

    'summary': """
        OdooShare georgeals""",

    'description': """
        OdooShare georgeals
    """,

    'author': "George Yanguzov",
    'website': "https://artlinespb.ru/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '14.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml', 
    ],
 
}
