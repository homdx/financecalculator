#!/usr/bin/kivy
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty, StringProperty, ListProperty
from kivy.uix.widget import Widget

# from accordion_edit import Accordion
import os
# import sqlite3

from Widgets import IncomeListItem, MutableTextInput

class IncomeScreen(Screen):
	"""
	TODO:
		- test to store information
		- test ot load information
		- format fields
	"""
	sessionStorage = ObjectProperty()
	welcomeLabel = ObjectProperty()
	data = ObjectProperty()

	data_income = ListProperty() # temp

	def set_user_information(self):

		# welcome fields
		self.welcomeLabel.text = str(self.sessionStorage.caseType) + " Income"
		self.data.text = str(self.sessionStorage.baseFilepath)

		# extract data if needed

		# TEST: submit 

	def args_converter(self, row_index, item):
		return {
            'note_index': row_index,
            'note_type': item['type'],
            'note_content': item['content'],
            'note_title': item['title']}

	def create_future_case(self):
		# self.sessionStorage.caseType = "Future"
		self.parent.current = 'CaseOverviewScreen'

	def load_future_case(self):
		self.parent.current = ''#CaseOverviewScreen'

	def compare_future_cases(self):
		self.parent.current = ''#CaseOverviewScreen'


	def create_present_case(self):
		self.sessionStorage.caseType = "Present"
		self.parent.current = 'CaseOverviewScreen'

	def load_present_case(self):
		self.parent.current = ''#FutureCaseOverviewScreen'

	def compare_present_cases(self):
		self.parent.current = ''#FutureCaseOverviewScreen'