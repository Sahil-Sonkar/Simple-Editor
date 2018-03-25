import sys
from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow):

    def __init__(self):

        super(Window, self).__init__()

        self.setGeometry(0, 0, 887, 585)
        self.setWindowTitle("My Editor")
        self.setWindowIcon(QtGui.QIcon('newlogo.png'))

        self.menuBar()

        self.statusBar()

        self.home()






    def menuBar(self):

        openFile =QtGui.QAction("&Open File",self)
        openFile.setShortcut("Ctrl+O")
        openFile.setStatusTip('Open file')
        openFile.triggered.connect(self.file_open)



        saveFile =QtGui.QAction("&Save File",self)
        saveFile.setShortcut("Ctrl+S")
        saveFile.setStatusTip('Save file')
        saveFile.triggered.connect(self.file_save)

        QuitAction = QtGui.QAction("&Exit",self)
        QuitAction.setShortcut("Ctrl+Q")
        QuitAction.setStatusTip('Close The Editor')
        QuitAction.triggered.connect(self.close_application)

        mainMenu = QtGui.QMenuBar()
        mainMenu.setNativeMenuBar(False)
        self.setMenuBar(mainMenu)

        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(openFile)
        fileMenu.addAction(saveFile)
        fileMenu.addSeparator()
        fileMenu.addAction(QuitAction)



    def home(self):

        wid = QtGui.QWidget(self)
        self.setCentralWidget(wid)
        self.layout = QtGui.QGridLayout()
        wid.setLayout(self.layout)


        self.text= QtGui.QTextEdit(self)

        self.setCentralWidget(self.text)

        self.text.cursorPositionChanged.connect(self.cursorPosition)

        self.statusbar=self.statusBar()


        self.show()


    def editor(self):

        self.textEdit = QtGui.QTextEdit()
        self.setCentralWidget(self.textEdit)

    def cursorPosition(self):

        cursor = self.text.textCursor()
        line = cursor.blockNumber()+1
        col = cursor.columnNumber()+1
        self.statusbar.showMessage("Line: {} | Column: {}".format(line,col))


    def file_open(self):
        name = QtGui.QFileDialog.getOpenFileName(self, 'Open File')
        file = open(name,'r')

        self.editor()

        with file:
            text = file.read()
            self.textEdit.setText(text)


    def file_save(self):
        name = QtGui.QFileDialog.getSaveFileName(self, 'Save File')
        file = open(name,'w')
        text = self.textEdit.toPlainText()
        file.write(text)
        file.close()


    def close_application(self):
        choice = QtGui.QMessageBox.question(self,'Exit!',"Are You Sure?",
            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)

        if choice == QtGui.QMessageBox.Yes:
            sys.exit()

        else:
            pass




    def closeEvent(self,event):
        choice = QtGui.QMessageBox.question(self,"Exit!","Are You Sure?",
            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)

        if choice == QtGui.QMessageBox.No:
            event.ignore()
        else:
            event.accept()
            sys.exit()



def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

if __name__ == '__main__':
    run()
