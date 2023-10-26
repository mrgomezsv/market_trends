# -*- coding: utf-8 -*-
{
    'name': "treming_profil_market_trends",

    'summary': """
        Arega menus en Compras, asi como un modelo para registrar cotizaciones, y mostrar
        en graficas los datos recabados""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base', 'product'],

    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'wizard/trprmatr_trends_tr.xml',
    ],
}
