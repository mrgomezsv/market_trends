# -*- coding: utf-8 -*-

from odoo import api, fields, models

class TrprmatrMarketTrendsTr(models.Model):
    _name = 'trprmatr.market.trends.tr'
    _description = 'Tendencias de Mercado'
    _rec_name = 'product_id'

    #name = fields.Char(string='Nombre de la Tendencia')
    product_id = fields.Many2one('product.product', string='Producto')
    partner = fields.Many2one('res.partner', string='Proveedor')
    price = fields.Float(string='Precio')
    date = fields.Date(string='Fecha', default=fields.Date.context_today)
