import sys
#from PuQt5.Qtwidgets impo
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout 
from PyQt5.QtCore import QTimer, Qt, QTime


class DC(QWidget):
    def __init__ (self):
        super().__init__()
        self.time_label = QLabel(self)
        self.timer = QTimer(self)
        self.initUI() 

    def initUI(self):  
        self.setWindowTitle("Digital Clock")
        self.setGeometry(600, 400, 300, 100)

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignCenter)

        self.time_label.setStyleSheet("font-size: 80px;"
                                      "font-family: Arial;"
                                      "color: #6AB6F3;")  # Sky blue
        self.setStyleSheet("background-color: #141512;")

        self.timer.timeout.connect(self.Update_time)
        self.timer.start(1000)
        
        self.Update_time()

    def Update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        self.time_label.setText(current_time)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = DC()
    clock.show()
    sys.exit(app.exec_())
