#!/usr/bin/kivy
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.widget import Widget

from accordion_edit import AccordionEdit
import os
# import sqlite3

class MenuScreen(Screen):
	session_storage = ObjectProperty()
	welcome_label = ObjectProperty()

	# def set_user_information(self):
	# 	self.welcome_label.text = "Welcome, " + str(self.session_storage.loggedInUser)

	def create_future_case(self):
		self.parent.current = 'FutureCaseOverviewScreen'