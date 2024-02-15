from odoo import models, fields, api

class Paciente(models.Model):
    _name = "hosp.paciente"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char('name')
    nombre = fields.Char("Nombre")
    apellido = fields.Char("Apellido")
    dni = fields.Integer("DNI", track_visibility='onchange')
    estado = fields.Selection(selection = [("borrador","Borrador"),("alta","Alta"),("baja","Baja")], track_visibility='onchange')
    tratamiento_id = fields.Many2one('hosp.tratamiento', string='Tratamiento')    

    @api.model
    def create(self,vals):
        
        rec = super(Paciente,self).create(vals)        
        code = self.env['ir.sequence'].next_by_code('secuencia.paciente')            
        rec['name'] = code
        return rec    
    



class Tratamiento(models.Model):
    _name = 'hosp.tratamiento'
    _description = 'Taatamientos de pacientes'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    codigo_tratamiento = fields.Char('Código Tratamiento')
    nombre_tratamiento = fields.Char('Nombre Tratamiento')
    medico_tratante = fields.Char('Médico Tratante')

    def name_get(self):
        result = []
        for record in self:
            name = record.codigo_tratamiento + " - " + record.nombre_tratamiento
            result.append((record.id, name))
        return result