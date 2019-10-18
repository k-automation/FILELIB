# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'e2yun_Online Ticket Submission',
    'category': 'Website',
    'sequence': 58,
    'summary': 'e2yun 服务订单表单在线提交 ',
    'depends': [
        'website_form_editor',
        'website_helpdesk',
        'website_helpdesk_form',
        'im_livechat'
    ],
    'description': """在线提交服务订单.
    """,
    'data': [
        'data/website_helpdesk.xml',
        'views/helpdesk_templates.xml',
        'views/commonproblems_templates.xml',
        'views/helpdesk_views.xml'
    ],
    'license': 'OEEL-1',
}