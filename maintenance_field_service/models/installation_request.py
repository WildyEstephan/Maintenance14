from odoo import models, fields, api

class InstallationRequest(models.Model):
    _name = 'installation.request'
    _description = 'Installation Request'

    name = fields.Char(
        string='Name', 
        required=False)

    equipment_id = fields.Many2one(
        comodel_name='maintenance.equipments',
        string='Equipment',
        required=True)
    partner_id = fields.Many2one(
        comodel_name='res.partner',
        string='Partner',
        required=True)
    state = fields.Selection(
        string='State',
        selection=[('draft', 'Created'),
                   ('install', 'Installed'),
                   ('approve', 'Approved'),
                   ],
        required=False, default='draft')

    @api.model
    def create(self, values):
        # Add code here

        values['name'] = self.env['ir.sequence'].next_by_code('installation.request')

        return super(InstallationRequest, self).create(values)
