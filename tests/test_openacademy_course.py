# -*- coding: utf-8 -*-
from odoo.tests import common
from psycopg2 import IntegrityError
from odoo.tools import mute_logger

# To mute sql constraints error use:
# "with mute_loger('odoo.sql_db'), ..." or 
# "@mute_logger('odoo.sql_db')" before function

class GloabalTestOpenAcademyCourse(common.TransactionCase):
	# Global test for openacademy module,
	# Test course and sessions

	# Psheudo-constructor method of test etUp
	def setUp(self):

		# Define global variables to test methods
		super(GloabalTestOpenAcademyCourse, self).setUp()
		self.course = self.env['openacademy.course']

	# Class methods (Isn't a test)
	def create_course(self, course_name, course_description, course_responsible_id):
		course_id = self.course.create({
			'name': course_name,
			'description': course_description,
			'responsible_id': course_responsible_id,
			})
		return course_id

	# Tests methods (start with: 'test_')

	@mute_logger('odoo.sql_db')
	def test_10_course_same_name_description(self):
		
		# Test: Create a course with the same name and description.
		# Constraint of different name than description.
		with self.assertRaisesRegexp(IntegrityError,
			'new row for relation "openacademy_course" violates check'
			' constraint "openacademy_course_name_description_check"'):
			print("Creating new test with same name and description")
			self.create_course('test','test', None)

	@mute_logger('odoo.sql_db')
	def test_20_courses_same_name(self):

		# Test: Create a course with ixisting name
		# Constraint of unique name
		with self.assertRaisesRegexp(IntegrityError,
			'duplicate key value violates unique constraint "openacademy_course_name_unique"'):
			print("Creating test with existing name")
			self.create_course('Test Name', 'Test Description', None)
			self.create_course('Test Name', 'Test Description', None)
	
	def test_15_duplicate_course(self):

		# Test: Duplicate course and pass constraint name
		course = self.env.ref('openacademy.course0')
		course_id = course.copy()
		print("Course_id", course_id)