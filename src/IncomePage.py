#!/usr/bin/kivy
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.widget import Widget

# from accordion_edit import Accordion
import os
# import sqlite3

class IncomeScreen(Screen):
	sessionStorage = ObjectProperty()
	welcomeLabel = ObjectProperty()

	def set_user_information(self):
		self.welcomeLabel.text = str(self.sessionStorage.caseType) + " Income"

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