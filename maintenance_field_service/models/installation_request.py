from odoo import models, fields, api
import datetime

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

    request_date = fields.Date(
        string='Request Date',
        required=False, default=datetime.datetime.today())
    expected_date_installation = fields.Date(
        string='Expected Date',
        required=False)
    installed_date = fields.Date(
        string='Installed Date',
        required=False)
    sale_id = fields.Many2one(
        comodel_name='sale.order',
        string='Sale',
        required=False)


    def install_this(self):

        self.state = 'install'


    def approve_this(self):
        self.installed_date = datetime.datetime.today()


        for part in self.equipment_id.part_ids:
            part.last_maintenance = self.installed_date
            part.calculate_next_maintenance()

        self.equipment_id.compute_dates_maintenance()


        self.state = 'approve'

    @api.model
    def create(self, values):
        # Add code here

        values['name'] = self.env['ir.sequence'].next_by_code('installation.request')

        return super(InstallationRequest, self).create(values)
