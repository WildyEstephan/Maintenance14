from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    is_part = fields.Boolean(
        string='Is a part',
        required=False)
    part_ids = fields.One2many(
        comodel_name='product.parts',
        inverse_name='product_id',
        string='Parts',
        required=False)


class Parts(models.Model):
    _name = 'product.parts'
    _description = 'Parts'

    name = fields.Char(
        string='Name',
        required=False, related='product_id.name')
    product_id = fields.Many2one(
        comodel_name='product.template',
        string='Product',
        required=True, domain="[('is_part', '=', True)]")
    qty_time = fields.Float(
        string='Qty time',
        required=True)
    period_time = fields.Selection(
        string='Period time',
        selection=[('days', 'Days'),
                   ('months', 'Months'),
                   ('years', 'Years'),
                   ],
        required=True, )



