# -*- coding: utf-8 -*-
# Copyright 2017 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields


class ResCountryState(models.Model):
    _inherit = 'res.country.state'

    name = fields.Char(translate=True)
