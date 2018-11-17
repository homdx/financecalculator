#!/usr/bin/kivy
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty, StringProperty, ListProperty
from kivy.uix.widget import Widget

# from accordion_edit import Accordion
import os
# import sqlite3

from Widgets import InvestmentListItem, MutableTextInput

class InvestmentScreen(Screen):
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
		self.welcomeLabel.text = str(self.sessionStorage.caseType) + " Investments"
		self.data.text = str(self.sessionStorage.baseFilepath)

		note_index = len(self.data_income)
		self.data_income.append({'title': 'income %d' %note_index, 'content': '0', 'type':'income'})

		# extract data if needed

		# TEST: submit 

	def args_converter(self, row_index, item):
		return {
            'note_index': row_index,
            'note_type': item['type'],
            'note_content': item['content'],
            'note_title': item['title']}

	def add_income(self):
		note_index = len(self.data_income)
		self.data_income.append({'title': 'income %d' %note_index, 'content': '0', 'type':'income'})
        # self.save_overview('income')  function for updating income 

	def del_OverviewListItem(self, note_index,note_type):
	        # delte from list
	        if note_type == 'income':
	            del self.data_income[note_index]
	        elif note_type == 'expenditure':
	            del self.data_expenditure[note_index]



    # not sure if the rest I need?


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