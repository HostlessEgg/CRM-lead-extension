from odoo import models, fields, api
from datetime import date

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    x_lead_category = fields.Selection([
        ('residencial', 'Residencial'),
        ('empresarial', 'Empresarial'),
        ('gubernamental', 'Gubernamental'),
    ], string='Categoría del Lead', tracking=True)

    x_delivery_deadline = fields.Date(string='Fecha límite de entrega', tracking=True)
    x_approved_by = fields.Many2one('res.users', string='Aprobado por', tracking=True)
    x_approved_date = fields.Date(string='Fecha de aprobación', tracking=True)
    x_duration_since_approved = fields.Integer(
        string='Días desde aprobación',
        compute='_compute_duration_since_approved',
        store=True
    )
    x_installation_required = fields.Boolean(string='Requiere instalación', tracking=True)
    x_installation_date = fields.Date(string='Fecha de instalación', tracking=True)
    x_contract_reference = fields.Char(string='Referencia de contrato', tracking=True)
    x_support_required = fields.Boolean(string='Soporte requerido', tracking=True)

    @api.depends('x_approved_date')
    def _compute_duration_since_approved(self):
        for record in self:
            if record.x_approved_date:
                record.x_duration_since_approved = (date.today() - record.x_approved_date).days
            else:
                record.x_duration_since_approved = 0

    def action_approve_lead(self):
        for record in self:
            record.x_approved_by = self.env.user
            record.x_approved_date = fields.Date.today()
