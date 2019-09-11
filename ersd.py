from PyQt5.QtWidgets import QLabel, QGridLayout, QLineEdit, QPushButton, QHBoxLayout, QMessageBox, QApplication,  QWidget, QVBoxLayout, QGroupBox, QMainWindow, QDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

import sys

#class mainWindow(Q)

class menu(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)

        #text
        greetings = QLabel("hello there...", self)
        greetings2 = QLabel("...wanna play?", self)

        #buttons
        computerUser = QPushButton("Computer -> User", self)
        userComputer = QPushButton("User -> Computer", self)
        end = QPushButton("Exit", self)

        #layout
        menuLayout = QVBoxLayout()
        menuLayout.addWidget(greetings)
        menuLayout.addWidget(greetings2)
        menuLayout.addWidget(computerUser)
        menuLayout.addWidget(userComputer)
        menuLayout.addWidget(end)

        greetings2.setAlignment(Qt.AlignRight)

        #general
        self.setLayout(menuLayout)
        self.setWindowTitle("- call me number -")
        self.setWindowIcon(QIcon('dice.png'))
        self.resize(250, 150)
        self.show()

        #events
        computerUser.clicked.connect(self.menuEvent)
        userComputer.clicked.connect(self.menuEvent)
        end.clicked.connect(self.endMenu)

    def menuEvent(self):
            user = self.sender()

            if user.text() == "Computer -> User":
                computerUserGame()
            else:
                userComputerGame()

    def endMenu(self):
        self.close()

    def closeEvent(self, event):
        answer =  QMessageBox.question(self, '- leaving me...? -', "are you sure?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if answer == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

class computerUserGame(QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)

        # text
        cuInfo = QLabel("hello there...", self)

        # layout
        cuLayout = QVBoxLayout()
        cuLayout.addWidget(cuInfo)

        # general
        self.setLayout(cuLayout)
        self.setWindowTitle("- call me number -")
        self.setWindowIcon(QIcon('dice.png'))
        self.resize(250, 150)
        self.show()

        computerUserGame.exec_()

class userComputerGame(QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)

        self.setWindowTitle("- call me number -")
        self.setWindowIcon(QIcon('dice.png'))
        self.resize(250, 150)
        self.show()

        userComputerGame.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = menu()

    sys.exit(app.exec())
