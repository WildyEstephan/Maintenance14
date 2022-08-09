from odoo import models, fields, api

class MaintenanceRequest(models.Model):
    _name = 'maintenance.request'
    _description = 'Maintenance Request'

    name = fields.Char(
        string='Name', 
        required=False)
    

