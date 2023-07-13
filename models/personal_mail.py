from odoo import models, fields, api


class EmployeePersonalEmail(models.Model):
    _inherit = "hr.employee"

    personal_email = fields.Char(string='Personal Email')