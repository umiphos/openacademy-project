# -*- coding: utf-8 -*-
import odoorpc
HOST = 'localhost'
PORT = 8069
DB = 'odoo-test'
USER = 'sebastian.hernandez@benandfrank.com'
PASS = 'admin'
ROOT = 'http://%s:%d/xmlrpc/' % (HOST,PORT)

# Prepare connection
odoo = odoorpc.ODOO('localhost', port=8069)

# Check available databases
print(odoo.db.list())

# Login
odoo.login(DB, USER, PASS)

# Current user
user = odoo.env.user
print(user.name)
print(user.company_id.name)

# Simple raw query
user_data = odoo.execute('res.users', 'read', [user.id])
print(user_data)

# Use all methos of a model
# if 'sale.order' in odoo.env:
# 	Order = odoo.env['saler.order']
# 	order_ids = Order.search([])
# 	for order in Order.browse(order_ids):
# 		print(order.name)
# 		products = [line.product_id.name for line in order.order_line]
# 		print(products)
if 'openacademy.course' in odoo.env:
	Course = odoo.env['openacademy.course']
	course_ids = Course.search([])
	print(course_ids)
	for course in Course.browse(course_ids):
		course.name = course.name + ' D'
		print(course.name)