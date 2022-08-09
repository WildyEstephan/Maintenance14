from odoo import models, fields, api
import datetime

class MaintenanceRequest(models.Model):
    _name = 'maintenance.request'
    _description = 'Maintenance Request'

    name = fields.Char(
        string='Name', 
        required=False)
    equipment_id = fields.Many2one(
        comodel_name='maintenance.equipments',
        string='Equipment',
        required=False)
    request_date = fields.Date(
        string='Request Date',
        required=False, default=datetime.datetime.today())
    start_date = fields.Datetime(string="Start Date", required=False, )
    end_date = fields.Datetime(string="End Date", required=False, )
    planned_end_date = fields.Datetime(string="Planned End Date", required=False, )
    planned_end_hours = fields.Float(string="Planned End Hours", required=False, )
    end_hours = fields.Float(string="End Hours By System", required=False, )

    time_effectiveness = fields.Selection(string="Time Effectiveness",
                                          selection=[('mild', 'Mild'), ('normal', 'Normal'), ('optimum', 'Optimum'),
                                                     ], required=False, )
    effectiveness = fields.Integer(string="Effectiveness %", required=False, group_operator="avg")
    type_maintenance = fields.Selection(string="Type of Maintenance",
                                        selection=[('corrective', 'Corrective'),
                                                   ('preventive', 'Preventive'), ],)
    
    
    maintenance_parts_id = fields.One2many(
        comodel_name='maintenance.parts',
        inverse_name='maintenance_request_id',
        string='Parts Maintenance',
        required=False)

    @api.model
    def create(self, values):
        # Add code here

        values['name'] = self.env['ir.sequence'].next_by_code('maintenance.request')

        return super(MaintenanceRequest, self).create(values)

class PartsEquipments(models.Model):
    _name = 'maintenance.parts'
    _description = 'Parts Lines'

    name = fields.Char(
        string='Name',
        required=False, related='product_id.name')
    part_id = fields.Many2one(
        comodel_name='product.template',
        string='Product',
        required=True, domain="[('is_part', '=', True)]")
    serial_part = fields.Char(
        string='Serial',
        required=False)
    equipment_id = fields.Many2one(
        comodel_name='maintenance.equipments',
        string='Equipment',
        required=False)
    equipment_part = fields.Many2one(
        comodel_name='product.parts.equipments',
        string='Equipment Part',
        required=False)
    maintenance_request_id = fields.Many2one(
        comodel_name='maintenance.request',
        string='Maintenance Request',
        required=False)