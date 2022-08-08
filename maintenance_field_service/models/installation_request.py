from odoo import models, fields, api

class InstallationRequest(models.Model):
    _name = 'installation.request'
    _description = 'Installation Request'

    name = fields.Char(
        string='Name', 
        required=False)

