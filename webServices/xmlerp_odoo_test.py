# -*- coding: utf-8 -*-
import functools
import xmlrpc.client
HOST = 'localhost'
PORT = 8069
DB = 'odoo-test'
USER = 'sebastian.hernandez@benandfrank.com'
PASS = 'admin'
ROOT = 'http://%s:%d/xmlrpc/' % (HOST,PORT)

# Login
uid = xmlrpc.client.ServerProxy(ROOT + 'common').login(DB,USER,PASS)
print("Logged in as %s (uid: %d)" % (USER,uid))

call = functools.partial(
    xmlrpc.client.ServerProxy(ROOT + 'object').execute,
    DB, uid, PASS)

# Read the sessions
sessions = call('openacademy.session', 'search_read', [], ['name','seats'])
for session in sessions:
    print("Session %s (%s seats)" % (session['name'], session['seats']))

# Create a new session from Course 0
course_id = call('openacademy.course', 'search', [('name','ilike','Course 0')])[0]
session_id = call('openacademy.session', 'create', {
    'name': 'My session',
    'course_id': course_id,
    })