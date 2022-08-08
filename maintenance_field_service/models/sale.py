from odoo import fields, models, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    installation_ids = fields.One2many(
        comodel_name='installation.request',
        inverse_name='sale_id',
        string='Installation',
        required=False)
    installation_count = fields.Integer(
        string='Delivery count', 
        required=False, compute='_compute_installation_count')
    

    @api.depends('installation_ids')
    def _compute_installation_count(self):

        for rec in self:

            rec.installation_count = len(rec.installation_ids)




    def action_confirm(self):
        super(SaleOrder, self).action_confirm()

        for line in self.order_line:

            if line.product_id.part_ids:

                parts = []

                for part in line.product_id.part_ids:
                    parts.append([0,0,
                                  {'product_id': part.product_id.id,
                                   'qty_time': part.qty_time,
                                   'period_time': part.period_time,
                                   } ])

                equipment_id = self.env['maintenance.equipments'].create({
                    'product_id': line.product_id.id,
                    'partner_id': self.partner_id.id,
                    'part_ids': parts
                })

                self.env['installation.request'].create({
                    'equipment_id': equipment_id.id,
                    'partner_id': self.partner_id.id,
                    'sale_id': self.id
                })


    def action_view_installations(self):

        action = self.env["ir.actions.actions"]._for_xml_id("maintenance_field_service.installation_request_action")

        installations = self.mapped('installation_ids')
        if len(installations) > 1:
            action['domain'] = [('id', 'in', installations.ids)]
        elif installations:
            form_view = [(self.env.ref('maintenance_field_service.installation_request_view_form').id, 'form')]
            if 'views' in action:
                action['views'] = form_view + [(state, view) for state, view in action['views'] if view != 'form']
            else:
                action['views'] = form_view
            action['res_id'] = installations.id
        # # Prepare the context.
        # installation_id = installations.filtered(lambda l: l.picking_type_id.code == 'outgoing')
        # if installation_id:
        #     installation_id = installation_id[0]
        # else:
        #     installation_id = installations[0]
        # action['context'] = dict(self._context, default_partner_id=self.partner_id.id,
        #                          default_picking_type_id=installation_id.picking_type_id.id, default_origin=self.name,
        #                          default_group_id=installation_id.group_id.id)
        return action
