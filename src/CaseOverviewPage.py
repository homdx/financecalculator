#!/usr/bin/kivy
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.widget import Widget

# from kivy.garden.navigationdrawer import NavigationDrawer

import os
# import sqlite3

# from kivy.garden.navigationdrawer import NavigationDrawer

# class DrawingSpace(NavigationDrawer):
#     pass
    
class CaseOverviewScreen(Screen):
	sessionStorage = ObjectProperty()
	welcomeLabel = ObjectProperty()

	def set_user_information(self):
		self.welcomeLabel.text = str(self.sessionStorage.caseType) + " Case Menu"

	def create_case(self):
		self.parent.current = 'FutureCaseOverviewScreen'