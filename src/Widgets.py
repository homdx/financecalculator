from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty, StringProperty, \
        NumericProperty, BooleanProperty


from kivy.clock import Clock

"""
To Do
improve the the del_overviewListItem to be more elegant 
"""


class MutableTextInput(FloatLayout):

    text = StringProperty()
    multiline = BooleanProperty(True)

    def __init__(self, **kwargs):
        super(MutableTextInput, self).__init__(**kwargs)
        Clock.schedule_once(self.prepare, 0)

    def prepare(self, *args):
        self.w_textinput = self.ids.w_textinput.__self__
        self.w_label = self.ids.w_label.__self__
        self.view()

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos) and touch.is_double_tap:
            self.edit()
        return super(MutableTextInput, self).on_touch_down(touch)

    def edit(self):
        self.clear_widgets()
        self.add_widget(self.w_textinput)
        self.w_textinput.focus = True

    def view(self):
        self.clear_widgets()
        if not self.text:
            self.w_label.text = "Double tap/click to edit"
        self.add_widget(self.w_label)

    def check_focus_and_view(self, textinput):
        if not textinput.focus:
            self.text = textinput.text
            self.view()

class IncomeListItem(BoxLayout):

    def __init__(self, **kwargs):
        print(kwargs)
        del kwargs['index']
        super(IncomeListItem, self).__init__(**kwargs)
    note_content = StringProperty()
    note_title = StringProperty()
    note_type = StringProperty()
    note_index = NumericProperty()

    def del_OverviewListItem(self, note_index,note_type):
        # delte from list

        print(note_type)
        print(note_index)
        if note_type == 'income':
            del self.overview.data_income[note_index]
        elif note_type == 'expenditure':
            del self.overview.data_expenditure[note_index]

        # save and refresh
        # self.save_overview(note_type)
        # self.refresh_overview(note_type)

class InvestmentListItem(BoxLayout):

    def __init__(self, **kwargs):
        print(kwargs)
        del kwargs['index']
        super(InvestmentListItem, self).__init__(**kwargs)
    note_content = StringProperty()
    note_title = StringProperty()
    note_type = StringProperty()
    note_index = NumericProperty()


