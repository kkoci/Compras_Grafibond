# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


{
    'name': 'Sistema de Compras Grafibond',
    'version': '1.1',
    'category': 'Compras',
    'sequence': 19,
    'summary': 'Ordenes de Compra, Presupuestos, Surtidores',
    'description': """
Sistema base para departamento de compras de Grafibond
==================================================

Este sistema ha sido desarrollado en base a la aplicacion de compra desarrollada por OpenErp,
una suite de modulos completa para solicitar presupuestos, hacer solicitudes de compra, etc etc
    """,
    'author': 'OpenERP SA',
    'website': 'http://www.openerp.com',
    'images' : ['images/purchase_order.jpeg', 'images/purchase_analysis.jpeg', 'images/request_for_quotation.jpeg'],
    'depends': ['stock', 'process', 'procurement'],
    'data': [
        'security/purchase_security.xml',
        'security/ir.model.access.csv',
        'purchase_workflow.xml',
        'purchase_sequence.xml',
        'company_view.xml',
        'purchase_data.xml',
        'wizard/purchase_order_group_view.xml',
        'wizard/purchase_line_invoice_view.xml',
        'compra_report.xml',
        'purchase_view.xml',
        'stock_view.xml',
        'partner_view.xml',
        'process/purchase_process.xml',
        'report/compra_report_view.xml',
        'board_purchase_view.xml',
        'edi/purchase_order_action_data.xml',
        'res_config_view.xml',
    ],
    'test': [
        'test/process/cancel_order.yml',
        'test/process/rfq2order2done.yml',
        'test/process/generate_invoice_from_reception.yml',
        'test/process/run_scheduler.yml',
        'test/process/merge_order.yml',
        'test/process/edi_purchase_order.yml',
        'test/process/invoice_on_poline.yml',
        'test/ui/print_report.yml',
        'test/ui/duplicate_order.yml',
        'test/ui/delete_order.yml',
    ],
    'demo': [
        'purchase_order_demo.yml',
        'purchase_demo.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
