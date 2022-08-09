from odoo import fields, models, api
from datetime import datetime
from datetime import timedelta
from dateutil.relativedelta import relativedelta

class Equipments(models.Model):
    _name = 'maintenance.equipments'
    _description = 'Equipments'

    name = fields.Char(
        string='Name',
        required=False, related='product_id.name')
    product_id = fields.Many2one(
        comodel_name='product.template',
        string='Product',
        required=True)
    partner_id = fields.Many2one(
        comodel_name='res.partner',
        string='Partner',
        required=True)
    last_maintenance = fields.Date(
        string='Last maintenance',
        required=False)
    next_maintenance = fields.Date(
        string='Last maintenance',
        required=False)
    installed_date = fields.Date(
        string='Installed Date',
        required=False)
    part_ids = fields.One2many(
        comodel_name='product.parts.equipments',
        inverse_name='equipment_id',
        string='Parts',
        required=False)

    @api.depends('part_ids')
    def _compute_dates_maintenance(self):

        for rec in self:

            last_part_for_maintenance = self.env['product.parts.equipments'].search([('equipment_id', '=', rec.id)],
                                                                                    order='last_maintenance desc',
                                                                                    limit=1)
            next_part_for_maintenance = self.env['product.parts.equipments'].search([('equipment_id', '=', rec.id)],
                                                                                    order='last_maintenance desc',
                                                                                    limit=1)

            rec.last_maintenance = last_part_for_maintenance.last_maintenance
            rec.next_maintenance = next_part_for_maintenance.next_maintenance


class PartsEquipments(models.Model):
    _name = 'product.parts.equipments'
    _description = 'Parts Equipments'

    name = fields.Char(
        string='Name',
        required=False, related='product_id.name')
    product_id = fields.Many2one(
        comodel_name='product.template',
        string='Product',
        required=True)
    part_id = fields.Many2one(
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

    last_maintenance = fields.Date(
        string='Last maintenance',
        required=False)
    next_maintenance = fields.Date(
        string='Last maintenance',
        required=False)

    equipment_id = fields.Many2one(
        comodel_name='maintenance.equipments',
        string='Equipment',
        required=False)

    def calculate_next_maintenance(self):

        last_maintenance = datetime.strptime(self.last_maintenance, '%Y-%m-%d')

        next_maintenance = ''

        if self.period_time == 'days':
            next_maintenance = last_maintenance + relativedelta(days=self.qty_time)
        elif self.period_time == 'months':
            next_maintenance = last_maintenance + relativedelta(months=self.qty_time)
        elif self.period_time == 'years':
            next_maintenance = last_maintenance + relativedelta(years=self.qty_time)

        self.next_maintenance = next_maintenance



    


