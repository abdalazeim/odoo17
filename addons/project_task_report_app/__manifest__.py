# -*- coding: utf-8 -*-
{
    'name': 'Project and Task Report in Odoo',
    "author": "Edge Technologies",
    'version': '17.0.1.0',
    'live_test_url': "https://youtu.be/RGymMBdvNhw",
    "images":['static/description/main_screenshot.png'],
    'summary': "Print project and task report using different filter project task reports tasks print project task report project task pdf report print pdf report on project and task print pdf report task project report task pdf report task reports project task",
    'description': """This app helps user to print project and task report between start date and end date using different filter like user of project or task and task stage.
    
project task repots
reports in project report on tasks print project task report project and task pdf report
print pdf report on project and task print pdf report task project report xls & pdf project task report xls & pdf
task pdf report, task reports project task report project reports
project pdf reports project task pdf reports 




    """,
    "license" : "OPL-1",
    'depends': ['base','project','hr_timesheet'],
    'data': [
            "security/ir.model.access.csv",
            "views/project_task_report_view.xml",
            "views/project_report_template.xml",
            "views/project_task_report_template.xml",
            ],
    'installable': True,
    'auto_install': False,
    'price': 000,
    'currency': "EUR",
    'category': 'Project',

}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
