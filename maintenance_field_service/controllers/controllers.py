# -*- coding: utf-8 -*-
# from odoo import http


# class MaintenanceFieldService(http.Controller):
#     @http.route('/maintenance_field_service/maintenance_field_service/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/maintenance_field_service/maintenance_field_service/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('maintenance_field_service.listing', {
#             'root': '/maintenance_field_service/maintenance_field_service',
#             'objects': http.request.env['maintenance_field_service.maintenance_field_service'].search([]),
#         })

#     @http.route('/maintenance_field_service/maintenance_field_service/objects/<model("maintenance_field_service.maintenance_field_service"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('maintenance_field_service.object', {
#             'object': obj
#         })
