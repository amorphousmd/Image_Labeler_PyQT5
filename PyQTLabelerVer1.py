# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PyQTLabelerVer1.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import os
import numpy as np
import ast
import re

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QPen, QPainter, QColor
from PyQt5.QtCore import Qt, QRectF, QEvent
from PyQt5.QtWidgets import QGraphicsScene, QFileDialog

# YOLOv5 bounding boxes colors
_COLORS = np.array(
    [
        0.000, 0.447, 0.741,
        0.850, 0.325, 0.098,
        0.929, 0.694, 0.125,
        0.494, 0.184, 0.556,
        0.466, 0.674, 0.188,
        0.301, 0.745, 0.933,
        0.635, 0.078, 0.184,
        0.300, 0.300, 0.300,
        0.600, 0.600, 0.600,
        1.000, 0.000, 0.000,
        1.000, 0.500, 0.000,
        0.749, 0.749, 0.000,
        0.000, 1.000, 0.000,
        0.000, 0.000, 1.000,
        0.667, 0.000, 1.000,
        0.333, 0.333, 0.000,
        0.333, 0.667, 0.000,
        0.333, 1.000, 0.000,
        0.667, 0.333, 0.000,
        0.667, 0.667, 0.000,
        0.667, 1.000, 0.000,
        1.000, 0.333, 0.000,
        1.000, 0.667, 0.000,
        1.000, 1.000, 0.000,
        0.000, 0.333, 0.500,
        0.000, 0.667, 0.500,
        0.000, 1.000, 0.500,
        0.333, 0.000, 0.500,
        0.333, 0.333, 0.500,
        0.333, 0.667, 0.500,
        0.333, 1.000, 0.500,
        0.667, 0.000, 0.500,
        0.667, 0.333, 0.500,
        0.667, 0.667, 0.500,
        0.667, 1.000, 0.500,
        1.000, 0.000, 0.500,
        1.000, 0.333, 0.500,
        1.000, 0.667, 0.500,
        1.000, 1.000, 0.500,
        0.000, 0.333, 1.000,
        0.000, 0.667, 1.000,
        0.000, 1.000, 1.000,
        0.333, 0.000, 1.000,
        0.333, 0.333, 1.000,
        0.333, 0.667, 1.000,
        0.333, 1.000, 1.000,
        0.667, 0.000, 1.000,
        0.667, 0.333, 1.000,
        0.667, 0.667, 1.000,
        0.667, 1.000, 1.000,
        1.000, 0.000, 1.000,
        1.000, 0.333, 1.000,
        1.000, 0.667, 1.000,
        0.333, 0.000, 0.000,
        0.500, 0.000, 0.000,
        0.667, 0.000, 0.000,
        0.833, 0.000, 0.000,
        1.000, 0.000, 0.000,
        0.000, 0.167, 0.000,
        0.000, 0.333, 0.000,
        0.000, 0.500, 0.000,
        0.000, 0.667, 0.000,
        0.000, 0.833, 0.000,
        0.000, 1.000, 0.000,
        0.000, 0.000, 0.167,
        0.000, 0.000, 0.333,
        0.000, 0.000, 0.500,
        0.000, 0.000, 0.667,
        0.000, 0.000, 0.833,
        0.000, 0.000, 1.000,
        0.000, 0.000, 0.000,
        0.143, 0.143, 0.143,
        0.286, 0.286, 0.286,
        0.429, 0.429, 0.429,
        0.571, 0.571, 0.571,
        0.714, 0.714, 0.714,
        0.857, 0.857, 0.857,
        0.000, 0.447, 0.741,
        0.314, 0.717, 0.741,
        0.50, 0.5, 0
    ]
).astype(np.float32).reshape(-1, 3)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1207, 840)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 790, 311, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.prev_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.prev_button.setObjectName("prev_button")
        self.horizontalLayout.addWidget(self.prev_button)
        self.next_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.next_button.setObjectName("next_button")
        self.horizontalLayout.addWidget(self.next_button)
        self.image_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.image_label.setText("")
        self.image_label.setObjectName("image_label")
        self.horizontalLayout.addWidget(self.image_label)
        self.graphicsView = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView.setGeometry(QtCore.QRect(10, 40, 971, 741))
        self.graphicsView.setObjectName("graphicsView")
        self.scene = QGraphicsScene()
        self.graphicsView.setScene(self.scene)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 0, 971, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.directory_label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.directory_label.setObjectName("directory_label")
        self.horizontalLayout_2.addWidget(self.directory_label)
        self.directory_tbrowser = QtWidgets.QTextBrowser(self.horizontalLayoutWidget_2)
        self.directory_tbrowser.setObjectName("directory_tbrowser")
        self.horizontalLayout_2.addWidget(self.directory_tbrowser)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(990, 0, 211, 781))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.cd_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.cd_button.setObjectName("cd_button")
        self.verticalLayout.addWidget(self.cd_button)
        self.finish_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.finish_button.setObjectName("finish_button")
        self.verticalLayout.addWidget(self.finish_button)
        self.comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout.addWidget(self.comboBox)
        self.comboBox.setEditable(True)
        self.comboBox.lineEdit().setAlignment(QtCore.Qt.AlignCenter)
        self.comboBox.addItems('Class 0, Class 1, Class 2'.split(","))
        line_edit = self.comboBox.lineEdit()
        line_edit.setAlignment(Qt.AlignCenter)
        line_edit.setReadOnly(True)
        self.bbox_tbrowser = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.bbox_tbrowser.setObjectName("bbox_tbrowser")
        self.verticalLayout.addWidget(self.bbox_tbrowser)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(340, 790, 121, 31))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.goto_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.goto_button.setObjectName("goto_button")
        self.horizontalLayout_3.addWidget(self.goto_button)
        self.index_ledit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.index_ledit.setObjectName("index_ledit")
        self.horizontalLayout_3.addWidget(self.index_ledit)
        font = QtGui.QFont()
        font.setPointSize(8)  # set the font size to 12 points
        self.bbox_tbrowser.setFont(font)

        # Set up general variables that are used for keeping track of annotated images
        self.image_loaded = False
        self.annotated_bboxes = {}
        self.current_file = None
        self.current_class_id = '0'

        # Connections
        self.cd_button.clicked.connect(self.load_image)
        self.comboBox.currentIndexChanged.connect(self.select_class)
        self.bbox_tbrowser.itemClicked.connect(self.item_clicked)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.prev_button.setText(_translate("Dialog", "<< Prev"))
        self.next_button.setText(_translate("Dialog", "Next >>"))
        self.directory_label.setText(_translate("Dialog", "Directory"))
        self.cd_button.setText(_translate("Dialog", "Change Directory"))
        self.finish_button.setText(_translate("Dialog", "Finish"))
        self.goto_button.setText(_translate("Dialog", "Go To"))

    def load_image(self):
        for line in self.dottedLines:
            self.graphicsView.scene().removeItem(line)
        self.dottedLines = []
        # Get the path to the image file using a file dialog
        self.filename, _ = QFileDialog.getOpenFileName(directory="C:/Users/LAPTOP/Desktop/Pics",
                                                       filter="Images (*.png *.xpm *.jpg *.bmp);;All Files (*)")
        if not self.filename:
            return
        self.current_file = str(os.path.basename(self.filename))
        if self.current_file not in self.annotated_bboxes:
            self.annotated_bboxes[self.current_file] = {}

        print(self.annotated_bboxes)
        # Load the image file as a pixmap
        self.graphicsView.scene().clear()
        pixmap = QPixmap(self.filename)
        if pixmap.isNull():
            return
        # Set the pixmap as the background for the QGraphicsView widget
        self.scene.clear()
        self.scene.addPixmap(pixmap)
        self.graphicsView.setSceneRect(QRectF(pixmap.rect()))
        self.graphicsView.fitInView(QRectF(pixmap.rect()), Qt.KeepAspectRatio)
        self.redrawBoundingBox(self.current_file)
        self.image_loaded = True

    def select_class(self, i):
        self.current_class_id = str(i)
        print("Current class index:", i)

    def redrawBoundingBox(self, current_file):
        # iterate over each image file in the dictionary
        for key, value in self.annotated_bboxes[current_file].items():
            for bbox in value:
                x, y, w, h = bbox
                rect = QtCore.QRectF(x, y, w, h)
                item = QtWidgets.QGraphicsRectItem(rect)
                R, G, B = [int(i * 255) for i in _COLORS[int(key)]]
                item.setPen(QtGui.QPen(QtGui.QColor(R, G, B)))
                item.setBrush(QtGui.QBrush(QtGui.QColor(R, G, B, 50)))
                self.scene.addItem(item)

    def redrawBoundingBoxExcept(self, current_file, except_bbox, highlight_class):
        for item in self.scene.items():
            if isinstance(item, QtWidgets.QGraphicsRectItem):
                self.scene.removeItem(item)

        # iterate over each image file in the dictionary
        for key, value in self.annotated_bboxes[current_file].items():
            for bbox in value:
                if bbox == except_bbox:
                    print(bbox, except_bbox)
                    continue
                x, y, w, h = bbox
                rect = QtCore.QRectF(x, y, w, h)
                item = QtWidgets.QGraphicsRectItem(rect)
                R, G, B = [int(i * 255) for i in _COLORS[int(key)]]
                item.setPen(QtGui.QPen(QtGui.QColor(R, G, B)))
                item.setBrush(QtGui.QBrush(QtGui.QColor(R, G, B, 50)))
                self.scene.addItem(item)
        x, y, w, h = except_bbox
        rect = QtCore.QRectF(x, y, w, h)
        item = QtWidgets.QGraphicsRectItem(rect)
        R, G, B = [int(i * 255) for i in _COLORS[int(highlight_class)]]
        item.setPen(QtGui.QPen(QtGui.QColor(R, G, B)))
        item.setBrush(QtGui.QBrush(QtGui.QColor(R, G, B, 150)))
        self.scene.addItem(item)
    def item_clicked(self, item):
        s = item.text()
        tuple_str = re.search(r'\(([\d\.]+),\s*([\d\.]+),\s*([\d\.]+),\s*([\d\.]+)\)', s).group(1, 2, 3, 4)
        bbox = tuple(map(float, tuple_str))
        highlight_class = s.split(' ')[0]
        self.redrawBoundingBoxExcept(self.current_file, bbox, highlight_class)



class MyDialog(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(MyDialog, self).__init__(parent)
        self.setupUi(self)
        self.graphicsView.viewport().installEventFilter(self)
        self.graphicsView.setMouseTracking(True)  # add this line

        # set the initial values for the bounding box
        self.startPos = None
        self.endPos = None
        self.drawnBox = False
        self.isDrawing = False
        self.dottedLines = []  # initialize a list to keep track of the dotted lines


    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_B:
            self.isDrawing = True
            event.accept()  # accept the event to stop it from propagating to other widgets
        else:
            super().keyPressEvent(event)  # call the base class method to handle other key press events

    def eventFilter(self, source, event):
        if event.type() == QtCore.QEvent.MouseMove:
            if not self.image_loaded:
                return super(MyDialog, self).eventFilter(source, event)
            # get the position of the mouse cursor in the scene coordinates
            scenePos = self.graphicsView.mapToScene(event.pos())

            # get the rectangle of the visible area in the view coordinates
            viewRect = self.graphicsView.viewport().rect()

            # clear any existing dotted lines
            try:
                for line in self.dottedLines:
                    self.graphicsView.scene().removeItem(line)
                self.dottedLines = []
            except RuntimeError:
                return super(MyDialog, self).eventFilter(source, event)

            # create a QPen object for the dotted line
            dottedLinePen = QtGui.QPen(QtCore.Qt.DotLine)
            dottedLinePen.setWidth(1)

            # add horizontal and vertical dotted lines intersecting at the cursor position
            horizLine = QtWidgets.QGraphicsLineItem(viewRect.left(), scenePos.y(), viewRect.right(), scenePos.y())
            horizLine.setPen(dottedLinePen)
            self.graphicsView.scene().addItem(horizLine)
            self.dottedLines.append(horizLine)

            vertLine = QtWidgets.QGraphicsLineItem(scenePos.x(), viewRect.top(), scenePos.x(), viewRect.bottom())
            vertLine.setPen(dottedLinePen)
            self.graphicsView.scene().addItem(vertLine)
            self.dottedLines.append(vertLine)

            return super(MyDialog, self).eventFilter(source, event)

        elif event.type() == QtCore.QEvent.MouseButtonPress and event.button() == QtCore.Qt.LeftButton:
            if self.isDrawing:
                if not self.drawnBox:
                    # start drawing
                    pos = self.graphicsView.mapToScene(event.pos())
                    self.startPos = pos
                    self.endPos = pos
                    self.drawnBox = True
                    return True
                else:
                    # finish drawing
                    pos = self.graphicsView.mapToScene(event.pos())
                    self.endPos = pos
                    self.drawnBox = False
                    self.isDrawing = False
                    # Get the x and y coordinates of the upper left corner of the bounding box
                    x = min(self.startPos.x(), self.endPos.x())
                    y = min(self.startPos.y(), self.endPos.y())

                    # Get the width and height of the bounding box
                    w = abs(self.startPos.x() - self.endPos.x())
                    h = abs(self.startPos.y() - self.endPos.y())

                    # Create the tuple with (x, y, w, h) coordinates
                    bbox = (round(x, 2), round(y, 2), round(w, 2), round(h, 2))
                    print(bbox)
                    self.drawBoundingBox()
                    if self.current_class_id not in self.annotated_bboxes[self.current_file]:
                        self.annotated_bboxes[self.current_file][self.current_class_id] = []
                    self.annotated_bboxes[self.current_file][self.current_class_id].append(bbox)
                    self.bbox_tbrowser.addItem(self.current_class_id + ' ' + str(bbox))
                    return True

        return super(MyDialog, self).eventFilter(source, event)

    def drawBoundingBox(self):
        # create a QGraphicsRectItem to represent the bounding box
        rect = QtCore.QRectF(self.startPos, self.endPos)
        item = QtWidgets.QGraphicsRectItem(rect)
        R, G, B = [int(i * 255) for i in _COLORS[int(self.current_class_id)]]  # convert values to integers in range [0, 255]
        item.setPen(QtGui.QPen(QtGui.QColor(R, G, B)))
        item.setBrush(QtGui.QBrush(QtGui.QColor(R, G, B, 50)))
        self.scene.addItem(item)
        self.startPos = None
        self.endPos = None
        self.drawnBox = False




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialog = MyDialog()
    dialog.show()
    sys.exit(app.exec_())

