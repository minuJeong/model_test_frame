
from PyQt5 import QtWidgets

from tool.ui import toolwidget


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    mainwin = QtWidgets.QMainWindow()
    tool = toolwidget.ToolWidget(mainwin)
    mainwin.setCentralWidget(tool)
    mainwin.show()
    app.exec()
