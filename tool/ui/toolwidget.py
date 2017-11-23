
from PyQt5 import QtWidgets
from .. import tool


class ToolWidget(QtWidgets.QWidget):

    __slots__ = ["mainwin", "tool"]

    def __init__(self, mainwin: QtWidgets.QMainWindow) -> None:
        super(ToolWidget, self).__init__()

        self.mainwin = mainwin

        mainlayout = QtWidgets.QVBoxLayout()
        self.setLayout(mainlayout)

        train_btn = QtWidgets.QPushButton("train")
        train_btn.clicked.connect(self.on_click_train)
        mainlayout.addWidget(train_btn)

        exit_btn = QtWidgets.QPushButton("exit")
        exit_btn.clicked.connect(lambda x: self.mainwin.close())
        mainlayout.addWidget(exit_btn)

        self.tool = tool.ToolApplication()

    def on_click_train(self, e=None):
        self.tool.default_train()
