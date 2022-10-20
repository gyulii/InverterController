import json
import os
import sys

from PySide6.QtCore import QAbstractListModel, Qt
from PySide6.QtGui import QImage
from PySide6.QtWidgets import QApplication, QMainWindow

from MainWindow import Ui_MainWindow

class TodoModel(QAbstractListModel):
    def __init__(self, todos=None):
        super().__init__()
        self.todos = todos or []

    def data(self, index, role):
        if role == Qt.DisplayRole:
            text = self.todos[index.row()]
            return text

        if role == Qt.DecorationRole:
            text = self.todos[index.row()]
            if text is "done":
                return "x"
        #To not be empty during edit
        if role == Qt.EditRole: 
            text = self.todos[index.row()]
            return text
            
    def setData(self, index, value, role):
        if role == Qt.EditRole:
            self.todos[index.row()] = value
            return True

    def rowCount(self, index):
        return len(self.todos)
    
    def flags(self, index):
            return Qt.ItemIsSelectable|Qt.ItemIsEnabled|Qt.ItemIsEditable
    
    
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.model = TodoModel()
        self.MyList.setModel(self.model)
        self.MyPushButtonAdd.pressed.connect(self.add)
        self.MyPushButtonDelete.pressed.connect(self.delete)
        


    def add(self):
        input_text =  self.MyEditLine.text()
        input_text = input_text.strip()
        if input_text:  # Don't add empty strings.
            # Access the list via the model.
            self.model.todos.append(input_text)
            # Trigger refresh.
            self.model.layoutChanged.emit()
            # Empty the input
            self.MyEditLine.setText("")

    def delete(self):
        indexes = self.MyList.selectedIndexes()
        if indexes:
            for index in indexes:
                del self.model.todos[index.row()]
            self.model.layoutChanged.emit()
            self.MyList.clearSelection()

    


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()