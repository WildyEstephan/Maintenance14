from odoo import fields, models, api


class Equipments(models.Model):
    _name = 'maintenance.equipments'
    _description = 'Equipments'

    name = fields.Char(
        string='Name',
        required=False)
    product_id = fields.Many2one(
        comodel_name='product.template',
        string='Product',
        required=False)
    partner_id = fields.Many2one(
        comodel_name='res.partner',
        string='Partner',
        required=False)
    last_maintenance = fields.Date(
        string='Last maintenance',
        required=False)
    part_ids = fields.One2many(
        comodel_name='product.parts.equipments',
        inverse_name='equipment_id',
        string='Parts',
        required=False)

class PartsEquipments(models.Model):
    _name = 'product.parts.equipments'
    _description = 'Parts Equipments'

    name = fields.Char(
        string='Name',
        required=False, related='product_id.name')
    product_id = fields.Many2one(
        comodel_name='product.template',
        string='Product',
        required=False, domain="[('is_part', '=', True)]")
    qty_time = fields.Float(
        string='Qty time',
        required=False)
    period_time = fields.Selection(
        string='Period time',
        selection=[('days', 'Days'),
                   ('months', 'Months'),
                   ('years', 'Years'),
                   ],
        required=False, )
    equipment_id = fields.Many2one(
        comodel_name='maintenance.equipments',
        string='Equipment',
        required=False)
    


