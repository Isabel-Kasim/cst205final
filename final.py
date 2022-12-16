# CST 205 - Image Manipulator
# This code is designed to take an image from a Pixabay API and display it, while giving the user the ability to manipulate the color of it.
# Isabel Kasim
# 12/16/22
# I worked on this project alone.

import requests, json
import sys
from PySide6.QtWidgets import (QApplication, QLabel, QWidget, 
                                QPushButton, QLineEdit, QVBoxLayout, QComboBox, QHBoxLayout)
from PySide6.QtCore import Slot
from PySide6.QtCore import Qt
from PySide6.QtCore import QUrl
from PySide6.QtWebEngineCore import QWebEnginePage
from PySide6.QtGui import QPixmap, QScreen
from pprint import pprint
from PIL import Image

my_key = '23906144-5a7273fcff585ce8f268ec0d0'

payload = {
  'api_key': my_key
}
endpoint = 'https://pixabay.com/api/?key=23906144-5a7273fcff585ce8f268ec0d0&q=yellow+flowers&image_type=photo'
try:
  r = requests.get(endpoint, params=payload)
  data = r.json()
  pprint(data['hits'][0]['largeImageURL'])
except:
  print('please try again')

class NewWindow(QWidget):
  def __init__(self):
    super().__init__()


class MyWindow(QWidget):
  def __init__(self):
    super().__init__()

    

    self.my_combo_box = QComboBox()
    self.my_combo_box.addItems(self.my_list)
    self.my_label = QLabel("")

    vbox = QVBoxLayout()
    vbox.addWidget(self.my_combo_box)
    vbox.addWidget(self.my_label)

    self.setLayout(vbox)
    self.my_combo_box.currentIndexChanged.connect(self.update_ui)
  def __init__(self):
    super().__init__()
    vbox = QVBoxLayout()
    self.my_lineedit = QLineEdit("Search for an image")
    self.my_lineedit.setMinimumWidth(250)
    self.my_lineedit.selectAll()
    self.my_btn = QPushButton("Submit")
    self.my_lbl = QLabel('')
    self.my_btn.clicked.connect(self.on_submit)
    self.my_lineedit.returnPressed.connect(self.on_submit)
    vbox.addWidget(self.my_lineedit)
    vbox.addWidget(self.my_btn)
    vbox.addWidget(self.my_lbl)
    self.setLayout(vbox)

  @Slot()
  def on_submit(self):
    # self.img_win = NewWindow()
    your_img = self.my_lineedit.text()
    self.my_lbl.setText(f'You searched for {your_img}.')
    self.setWindowTitle('Image')
    self.label = QLabel(self)
    # self.browser = QWebEnginePage()
    # self.browser.setUrl(QUrl(data['hits'][0]['largeImageURL']))
    self.pixmap = QPixmap()
    self.getAndSetImageFromURL(data['hits'][0]['largeImageURL'])
    self.resize(self.pixmap.width(),self.pixmap.height())
    screenSize = QScreen.availableGeometry(QApplication.primaryScreen())
    frmX = (screenSize.width () - self.width ())/2
    frmY = (screenSize.height() - self.height())/2
    self.move(frmX, frmY)
    self.show() 

    # above code was borrowed from https://stackoverflow.com/questions/68104165/display-image-from-url
    


  @Slot()
  def update_ui(self):
    my_text = self.my_combo_box.currentText()
    my_index = self.my_combo_box.currentIndex()
    self.my_label.setText(f'You chose {self.my_list[my_index]}.')


  def getAndSetImageFromURL(self,imageURL):
        request = requests.get(imageURL)
        self.pixmap.loadFromData(request.content)
        self.label.setPixmap(self.pixmap)



app = QApplication([])
my_win = MyWindow()
my_win.show()
app.exec_()




# This application was unable to run, I had tried to understand extracting the data from the API, and while I did, I could not understand how to display said image link in either the same window or new window. However, I was able to understand 
# retrieving the data from the API which was a huge leap for me. I had gotten stuck here and was unable to complete the aspect of color manipulation.
