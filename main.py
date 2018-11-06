#!/usr/bin/kivy
"""
modified by: Tyler Nincevic, James Lee
date modified: Oct. 31, 2018
Module handles the creation, commencement of the AIDA application and links
all the screens together
"""
from kivy.config import Config
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty, StringProperty, BooleanProperty,\
    NumericProperty
from kivy.loader import Loader

# from screeninfo import get_monitors
import sys
import os.path
import sqlite3

sys.path.insert(0, 'src')

#: Load Aida Screen Classes. Needed for KV files to transition between screens
# from LoginPage import LoginScreen
from MenuPage import MenuScreen
from CaseOverviewPage import CaseOverviewScreen#, DrawingSpace
# from NewPatientPage import NewPatientScreen
# from SearchPatientsPage import SearchPatientsScreen
# from AnalysisPage import AnalysisScreen
# from PatientPage import PatientInfoScreen, CurrentPatientInfo, \
#     SortCasesDropDown, SelectImageDropDown

#Probably not needed
# from PatientPage import CurrentPatientInfo, SortCasesDropDown, \
#     SelectImageDropDown

# from LocationPage import LocationSelectionScreen
# from CheckpointPage import CaseCheckpointScreen
# from ImagingPage import ImagingScreen
# from AidaDataBaseHandler import AidaDataBaseHandler
# from BoundingBoxPage import BoundingBoxScreen

debugMode = False  #: Set to true for debug mode
cloudAccess = True  #: Set to True to make AWS db calls throughout app
# baseFilepath = os.path.join(os.path.expanduser('~'), 'Documents', 'AIDA/')


class SessionStorage(Screen):
    """ Keeps track of session variables needed across multiple screen
    This is not an actual screen that will be displayed.
    This 'screen' class just keeps track of global variables that will be
    used by the other screens, such as the debugMode.
    Can also put other globals in here such as encryption information
    Attributes:
        debugMode (bool): set to True if debugging
            Not heavily utilized but currently only skips login credentials
        cloudAccess (bool): if True store all aidaData(images, userInfo,
            patientInfo to AWS)
        baseFilepath (str): Local database directory location and patient
            checkpoint directories are also stored in this directory
        loggedInUser (str): The username of the current logged in user
        loggedInAuthority (str): If the user is a Doctor, Nurse, Admin, etc.
        userAuthTokenAws (str): authentication (JWT) from AWS,
            not encrypted, varying length, when user logs in set to some
            string otherwise None. Make sure to reset to None on logout.
        currentAidaPid (str): The ID of the patient to anonymize their data
        currentCaseNumber (str): Number representing which mole on the users body
        currentCheckpointNumber (str): Number representing which checkpoint
            of the mole. (First appoitment with doctor will be checkpoint 1,
            and the next appointment will be checkpoint 2)
        currentCheckpointFolder (str):
        patientName (str): <patientFirstName>, (if middle name not null)
            <patientMiddleName>, <patientLastName>
        patientFirstName (str):
        patientMiddleName (str):
        patientLastName (str):
        patientAge (str):
        patientBirthDate (str):
        patientPostalCode (str):
        patientSex (str):
        patientRace (str):
        patientCancerHx (str): Cancer History of patient
        locationOnBody (str): The location on patient body where the mole is
            found
    """

    debugMode = BooleanProperty(debugMode)
    # cloudAccess = BooleanProperty(cloudAccess)
    # baseFilepath = StringProperty(baseFilepath)
    # loggedInUser = StringProperty()
    loggedInAuthority = NumericProperty()
    userAuthTokenAws = ""

    # Imaging session information
    currentAidaPid = StringProperty()
    currentCaseNumber = NumericProperty()
    currentCheckpointNumber = NumericProperty()
    currentCheckpointFolder = StringProperty()

    # Patient information
    patientName = StringProperty()
    patientFirstName = StringProperty()
    patientMiddleName = StringProperty()
    patientLastName = StringProperty()
    patientAge = NumericProperty()
    patientBirthDate = StringProperty()
    patientPostalCode = StringProperty()
    patientSex = StringProperty()
    patientRace = StringProperty()
    patientCancerHx = StringProperty()
    locationOnBody = "place_holder"


    def user_logged_in(self, username, authority):
        """The user has logged in, set corresponding sesionStorage attributes
        Args:
            username:
            authority:
        Returns:
            None
        """
        self.loggedInUser = username
        self.loggedInAuthority = authority
        print("User logged in: " + str(username) + ", " + str(authority))


class FinanceApp(App):
    """ The Base Class for Aida
    The App class is the base for creating Kivy applications. Think of it as
    your main entry point into the Kivy run loop. In most cases,
    you subclass this class and make your own app. You create an instance of
    your specific app class and then, when you are ready to start the
    application’s life cycle, you call your instance’s App.run() method
    Notes:
        For more information visit:
        https://kivy.org/doc/stable/api-kivy.app.html
    TODO:
        Set up logging within AIDA
    """

    def build(self):
        """Initializes the application; it will be called only once.
        If this method returns a widget (tree), it will be used as the root
        widget and added to the window.
        Returns:
            None or a root Widget instance if no self.root exists.
        """
        # Get main monitor size
        # monitorWidth = get_monitors()[0].width
        # monitorHeight = get_monitors()[0].heightb
        # Config.set('graphics', 'width', monitorWidth)
        # Config.set('graphics', 'height', monitorHeight)
        # Config.set('graphics', 'fullscreen', 0)
        # Config.set('graphics', 'resizable', 1)
        # Config.write()

        # Set the default loading image
        # Loader.loading_image = 'kv/images/loading.gif'


        root = Builder.load_file("kv/GUIManager.kv")
        return root

if __name__ == "__main__":
    #: When the python interpreter reads the source code, start up the App
    FinanceApp().run()