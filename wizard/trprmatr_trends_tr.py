# -*- coding: utf-8 -*-

from odoo import api, fields, models, exceptions

class TrprmatrTrendsTr(models.TransientModel):
    _name = 'trprmatr.trends.tr'
    _description = 'Generate Market Trend Chart Wizard'

    product_id = fields.Many2one('product.product', string='Producto')
    start_date = fields.Date(string='Fecha de inicio')
    end_date = fields.Date(string='Fecha de fin')

    def action_generate_chart(self): # Obtener los datos del modelo trprmatr.market.trends.tr que coinciden con el producto y las fechas
        trend_records = self.env['trprmatr.market.trends.tr'].search([
            ('product_id', '=', self.product_id.id),
            ('date', '>=', self.start_date),
            ('date', '<=', self.end_date),
        ])

        if not trend_records:
            raise exceptions.UserError('No se encontraron registros para generar el gráfico.')

        # Aquí debes generar el gráfico con los datos de trend_records
        # Puedes utilizar la biblioteca de gráficos de Odoo o cualquier otra biblioteca de gráficos de tu elección.
        # El código para generar el gráfico dependerá de la biblioteca que elijas.

        # Una vez que tengas el gráfico, puedes mostrarlo al usuario o guardarlo en algún lugar, según tus necesidades.

        return {
            'type': 'ir.actions.act_window',
            'res_model': 'trprmatr.trends.tr',
            'view_mode': 'form',
            'target': 'new',
            'context': {'default_product_id': self.product_id.id, 'default_start_date': self.start_date, 'default_end_date': self.end_date},
        }
