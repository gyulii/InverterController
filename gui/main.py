import json
import os
import sys
import random
import time
import uuid


from PySide6.QtCore import (
    QObject,
    QRunnable,
    QThreadPool,
    QTimer,
    Signal,
    Slot,
)

from PySide6.QtCore import QAbstractListModel, Qt
from PySide6.QtGui import QImage
from PySide6.QtWidgets import QApplication, QMainWindow

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from MainWindow import Ui_MainWindow
import pyqtgraph as pg




class GraphSignals(QObject):
    """
    Defines the signals available from a running worker thread.

    data
        tuple data point (worker_id, x, y)
    """

    data = Signal(tuple)  # <1> Name , value ,time??    
    pause = Signal(bool)


class GraphThread(QRunnable):
    """
    Worker thread

    Inherits from QRunnable to handle worker thread setup, signals
    and wrap-up.
    """

    def __init__(self):
        super().__init__()
        self.worker_id = uuid.uuid4().hex  # Unique ID for this worker.
        self.signals = GraphSignals()
        
         

    @Slot()
    def run(self):
        
        
        while self.signals.pause:
            time.sleep(0)  # <1>
            
        total_n = 1000
        y2 = random.randint(0, 10)
        delay = random.random() / 100  # Random delay value.
        value = 0

        for n in range(total_n):
            # Dummy calculation, each worker will produce different values,
            # because of the random y & y2 values.
            y = random.randint(0, 10)
            value += n * y2 - n * y

            self.signals.data.emit((self.worker_id, n, value))  # <2>
            time.sleep(delay)



    def pause(self):
        self.is_paused = True

    def resume(self):
        self.is_paused = False


class TodoModel(QAbstractListModel):
    def __init__(self, todos_list=None):
        super().__init__()
        self.todos_list = todos_list or []

    def data(self, index, role):
        if role == Qt.DisplayRole:
            text = self.todos_list[index.row()]
            return text

        if role == Qt.EditRole: 
            text = self.todos_list[index.row()]
            return text
            
    def setData(self, index, value, role):
        if role == Qt.EditRole:
            self.todos_list[index.row()] = value
            return True

    def rowCount(self, index):
        return len(self.todos_list)
    
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
        self.DebugButton.pressed.connect(self.graph_function)
        
        self.StartGraph.pressed.connect(self.worker.resume)
        self.PauseGraph.pressed.connect(self.worker.pause)

        self.threadpool = QThreadPool() # Threading 
        """
        Variables for the graphing
        """
        self.x = {}  # Keep timepoints.
        self.y = {}  # Keep data.
        self.lines = {}  # Keep references to plotted lines, to update.



    def graph_function(self):
        worker = GraphThread()
        worker.signals.data.connect(self.receive_data)
        # Execute
        self.threadpool.start(worker)
        
    def receive_data(self, data):
        worker_id, x, y = data  # <3>
  
        if worker_id not in self.lines:
            self.x[worker_id] = [x]
            self.y[worker_id] = [y]

            # Generate a random color.
            pen = pg.mkPen(
                width=2,
                color=(
                    random.randint(100, 255),
                    random.randint(100, 255),
                    random.randint(100, 255),
                ),
            )
            self.lines[worker_id] = self.MyGraph.plot(
                self.x[worker_id], self.y[worker_id], pen=pen
            )
            

        # Update existing plot/data
        self.x[worker_id].append(x)
        self.y[worker_id].append(y)

        self.lines[worker_id].setData(
            self.x[worker_id], self.y[worker_id]
        )


    def add(self):
        input_text =  self.MyEditLine.text()
        input_text = input_text.strip()
        if input_text:  # Don't add empty strings.
            # Access the list via the model.
            self.model.todos_list.append(input_text)
            # Trigger refresh.
            self.model.layoutChanged.emit()
            # Empty the input
            self.MyEditLine.setText("")

    def delete(self):
        indexes = self.MyList.selectedIndexes()
        if indexes:
            for index in indexes:
                del self.model.todos_list[index.row()]
            self.model.layoutChanged.emit()
            self.MyList.clearSelection()


    


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()