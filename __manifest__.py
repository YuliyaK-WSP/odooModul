{
    'name':'test YulyaK',
    'author':'yulyaK',
    'version': '1.0',
    'summary': 'Custom module for handling invoices and warehouse orders',
    'description': 'Custom module for managing invoices and warehouse orders in Odoo',
    'category': 'Custom',
    'depends': ['base','product','account','purchase','sale','hr','stock','stock_account'],
    'data':[
        'views/menu.xml',
        'views/order.xml',
        'views/invoice.xml',
        'security/ir.model.access.csv',

    ],

    'installable': True,
    'application': True,
    'auto_install': False,
}