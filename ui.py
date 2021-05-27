import sys
from PyQt5.QtWidgets import QApplication, QFileDialog, QWidget, QPushButton, QDesktopWidget, QListWidget, QLineEdit, QGridLayout, QLabel
from push_pics import push_pics

class push_pics_ui(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # init arguments
        self.filenames = None
        self.device = None
        self.channel = None

        # set size and location
        self.setGeometry(300, 300, 350, 250)
        self.center()

        # setup elements
        # labels
        self.push_status = QLabel("")

        # buttons
        # file select
        self.dir_select_button = QPushButton("Select Folder")
        self.dir_select_button.clicked.connect(self.get_files)
        # push
        self.push_button = QPushButton("Push")
        self.push_button.clicked.connect(self.execute_push)

        # line edits
        self.dir_select_edit = QLineEdit()

        # lists
        self.file_list = QListWidget()

        # grid
        self.grid = QGridLayout()
        self.grid.setSpacing(5)

        # arrange grid
        self.grid.addWidget(self.dir_select_button, 1, 0)
        self.grid.addWidget(self.file_list, 1, 1)
        self.grid.addWidget(self.push_button, 2, 0)
        self.grid.addWidget(self.push_status, 2, 1)
        self.setLayout(self.grid)

        # show
        self.setWindowTitle("PushPics")
        self.show()

    def center(self):
        self_rect = self.frameGeometry()
        screen_center = QDesktopWidget().availableGeometry().center()
        self_rect.moveCenter(screen_center)
        self.move(self_rect.topLeft())

    def get_files(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFiles)
        if file_dialog.exec_():
            self.filenames = file_dialog.selectedFiles()
            filenames_nobrackets = str(self.filenames).replace("[", "").replace("]", "").replace("'", "")
            self.file_list.addItems(self.filenames)

    def execute_push(self):
        push_pics(self.filenames, self.device, self.channel)
        self.push_status.setText("Pushed!")


def main():
    app = QApplication(sys.argv)
    ui_obj = push_pics_ui()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()