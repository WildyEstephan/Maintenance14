from odoo import fields, models, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

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
                    'partner_id': line.partner_id.id,
                    'part_ids': parts
                })

                self.env['installation.request'].create({
                    'equipment_id': equipment_id.id,
                    'partner_id': self.partner_id.id,
                })
