# -*- coding: utf-8 -*-

from odoo import api, fields, models, exceptions
import matplotlib.pyplot as plt
#pip install matplotlib


class TrprmatrTrendsTr(models.TransientModel):
    _name = 'trprmatr.trends.tr'
    _description = 'Generate Market Trend Chart Wizard'

    product_id = fields.Many2one('product.product', string='Producto')
    start_date = fields.Date(string='Fecha de inicio')
    end_date = fields.Date(string='Fecha de fin')
    chart_data = fields.Text(string='Datos del gráfico', readonly=True)


    def action_generate_chart(self): # Obtener los datos del modelo trprmatr.market.trends.tr que coinciden con el producto y las fechas
        trend_records = self.env['trprmatr.market.trends.tr'].search([
            ('product_id', '=', self.product_id.id),
            ('date', '>=', self.start_date),
            ('date', '<=', self.end_date),
        ])

        # if not trend_records:
        #     raise exceptions.UserError('No se encontraron registros para generar el gráfico.')
        #
        # # Crear los datos del gráfico
        # chart_data = {
        #     'labels': [record.date for record in trend_records],
        #     'datasets': [{
        #         'label': 'Precio',
        #         'data': [record.price for record in trend_records],
        #         'borderColor': 'blue',  # Color de la línea
        #         'fill': False,  # Sin relleno debajo de la línea
        #     }]
        # }
        #
        # # Crear el gráfico utilizando matplotlib
        # plt.figure(figsize=(10, 5))  # Definir el tamaño del gráfico
        # plt.plot(chart_data['labels'], chart_data['datasets'][0]['data'],
        #          color=chart_data['datasets'][0]['borderColor'])
        # plt.title('Tendencia de Precio')  # Título del gráfico
        # plt.xlabel('Fecha')
        # plt.ylabel('Precio')
        #
        # # Guardar el gráfico en un archivo
        # chart_image_path = '/path/to/your/chart_image.png'  # Ruta donde deseas guardar el gráfico
        # plt.savefig(chart_image_path)
        #
        # # Cerrar el gráfico
        # plt.close()
        #
        # # Puedes mostrar el gráfico al usuario si lo deseas, o guardarlo en algún lugar y proporcionar un enlace al usuario.
        #
        # return {
        #     'type': 'ir.actions.act_url',
        #     'name': 'Gráfico de Tendencia de Precio',
        #     'url': 'file://{}'.format(chart_image_path),
        #     'target': 'new',
        # }
