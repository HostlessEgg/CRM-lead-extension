{
    'name': 'CRM Lead Extension',
    'version': '1.0',
    'summary': 'Extiende el modelo CRM Lead con campos personalizados',
    'author': 'Jaisher',
    'category': 'Sales/CRM',
    'depends': ['crm'],
    'data': [
        'views/crm_order_view.xml',
        'data/demo_data.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
