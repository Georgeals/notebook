# -*- coding: utf-8 -*-

from odoo import models, fields, api


class odoo_share_georgeals(models.Model):

    _name = 'odoo_share_georgeals.odoo_share_georgeals'
    _description = 'odoo_share_georgeals.odoo_share_georgeals'

    datas = fields.Binary('File')
    name = fields.Char('File Name')
    link = fields.Char('Share link', readonly=True)   

    def upload(self):        
        self.link=self.get_base_url()+'/web/content/odoo_share_georgeals.odoo_share_georgeals/'+str(self.id)+'/datas/'+self.name        
        vals=self.read()[0]
        self.write(vals)
        return True
