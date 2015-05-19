#/usr/bin/python
#-*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.uix.togglebutton import ToggleButton
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.utils import get_color_from_hex
from kivy.core.window import Window
from kivy.config import Config


class RadioButton(ToggleButton):
	def getButtonText(self):
		print self.text
		return self.text

class OzPerformance(BoxLayout):
	pass


class OzMarks(BoxLayout):
	postmarks_visible = False
	def updateSubmitLayout(self):
		postexam_marks = Factory.OzPostMarks()
		mark_selection = self.children[0]
		7
		if not self.postmarks_visible:
			self.add_widget(postexam_marks)
			self.postmarks_visible = True
		else:
			self.remove_widget(self.children[0])
			self.add_widget(postexam_marks)
			mark_selection = self.children[1]

		for child in mark_selection.children:
			if child.state == 'down':
				self.exam_type = child.text
		if self.exam_type.upper() == 'k-cet'.upper():
			self.subject_marks = 60
			self.total_marks = 180 
		elif self.exam_type.upper() == 'jee-mains'.upper():
			self.subject_marks = 120
			self.total_marks = 360
		else:
			self.total_marks = 80
		print self.total_marks
		

class OzRoot(BoxLayout):
	pass


class OzApp(App):
	pass

if __name__ == '__main__':

	back_color = '#262626'

	#Config.set('graphics', 'height', '540')
	#Config.set('graphics', 'width', '960')
	#Config.set('graphics', 'resizable', '0')

	Window.clearcolor = get_color_from_hex(back_color)
	OzApp().run()