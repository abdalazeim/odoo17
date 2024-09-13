[![Build Status](https://runbot.odoo.com/runbot/badge/flat/1/master.svg)](https://runbot.odoo.com/runbot)
[![Tech Doc](https://img.shields.io/badge/master-docs-875A7B.svg?style=flat&colorA=8F8F8F)](https://www.odoo.com/documentation/17.0)
[![Help](https://img.shields.io/badge/master-help-875A7B.svg?style=flat&colorA=8F8F8F)](https://www.odoo.com/forum/help-1)
[![Nightly Builds](https://img.shields.io/badge/master-nightly-875A7B.svg?style=flat&colorA=8F8F8F)](https://nightly.odoo.com/)

# Odoo
----

Odoo is a suite of web based open source business apps.

The main Odoo Apps include an <a href="https://www.odoo.com/page/crm">Open Source CRM</a>,
<a href="https://www.odoo.com/app/website">Website Builder</a>,
<a href="https://www.odoo.com/app/ecommerce">eCommerce</a>,
<a href="https://www.odoo.com/app/inventory">Warehouse Management</a>,
<a href="https://www.odoo.com/app/project">Project Management</a>,
<a href="https://www.odoo.com/app/accounting">Billing &amp; Accounting</a>,
<a href="https://www.odoo.com/app/point-of-sale-shop">Point of Sale</a>,
<a href="https://www.odoo.com/app/employees">Human Resources</a>,
<a href="https://www.odoo.com/app/social-marketing">Marketing</a>,
<a href="https://www.odoo.com/app/manufacturing">Manufacturing</a>,
<a href="https://www.odoo.com/">...</a>

# Additional mods from me
## <a href="https://apps.odoo.com/apps/modules/17.0/om_account_accountant">Billing &amp;Full Accounting</a>,
## <a href= "https://apps.odoo.com/apps/modules/17.0/auto_database_backup">Auto Database Backup</a>,
## <a href= "https://apps.odoo.com/apps/modules/17.0/ohrms_core">Open HRMS Core</a>,
## <a href= "https://apps.odoo.com/apps/modules/17.0/bi_print_journal_entriesp">Print Journal Entries Report in Odoo</a>,
## <a href= "https://apps.odoo.com/apps/modules/17.0/project_task_report_app">Project and Task Report in Odoo</a>,





# How to Install Odoo 17 on Ubuntu 22.04 &24
-------------------------
# Step 1 – Install Required Dependencies 
# Odoo is a Python-based software
## sudo apt-get install -y python3-pip python3-dev python3-venv libxml2-dev libxslt1-dev zlib1g-dev libsasl2-dev libldap2-dev build-essential libssl-dev libffi-dev libmysqlclient-dev libjpeg-dev libpq-dev libjpeg8-dev liblcms2-dev libblas-dev libatlas-base-dev -y
# Next, install the NPM package manager.
## sudo apt install nodejs
## sudo apt-get install -y npm
# Then, install other dependencies using NPM.
## sudo npm install -g less less-plugin-clean-css
# Next, install the node-less package.
## sudo apt-get install -y node-less
# Next, download wkhtmltopdf package and install it using the following command:
## sudo apt install wkhtmltopdf -y
## sudo wget https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6-1/wkhtmltox_0.12.6-1.bionic_amd64.deb
## sudo dpkg -i wkhtmltox_0.12.6-1.bionic_amd64.deb
## sudo apt install -f
# Step 2 – Install PostgreSQL
# Odoo uses PostgreSQL as a database backend. You can install it using the following command
## sudo apt-get install postgresql -y
## sudo systemctl status postgresql
## sudo -u postgres psql
## createuser --createdb --username postgres --no-createrole --no-superuser --pwprompt odoo17
## psql
## ALTER USER odoo17 WITH SUPERUSER;
## \q
## exit



To learn the software, we recommend the <a href="https://www.odoo.com/slides">Odoo eLearning</a>, or <a href="https://www.odoo.com/page/scale-up-business-game">Scale-up</a>, the <a href="https://www.odoo.com/page/scale-up-business-game">business game</a>. Developers can start with <a href="https://www.odoo.com/documentation/17.0/developer/howtos.html">the developer tutorials</a>
