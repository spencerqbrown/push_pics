import sys
from PyQt5.QtWidgets import QApplication, QFileDialog, QWidget, QPushButton, QDesktopWidget, QListWidget, QLineEdit, QGridLayout, QLabel, QMessageBox
from push_pics import push_pics

class push_pics_ui(QWidget):

    config_filename = "config.ini"

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

        # labels
        self.push_status = QLabel("")

        # buttons
        # file select
        self.dir_select_button = QPushButton("Select Folder")
        self.dir_select_button.clicked.connect(self.get_files)
        # push
        self.push_button = QPushButton("Push")
        self.push_button.clicked.connect(self.execute_push)
        # key select
        self.key_select_button = QPushButton("Select Key File")
        self.key_select_button.clicked.connect(self.key_file_select)

        # line edits
        self.dir_select_edit = QLineEdit()
        self.key_line_edit = QLineEdit()

        # lists
        self.file_list = QListWidget()

        # grid
        self.grid = QGridLayout()
        self.grid.setSpacing(5)

        # arrange grid
        self.grid.addWidget(self.dir_select_button, 1, 0)
        self.grid.addWidget(self.file_list, 1, 1)
        self.grid.addWidget(self.key_select_button, 2, 0)
        self.grid.addWidget(self.key_line_edit, 2, 1)
        self.grid.addWidget(self.push_button, 3, 0)
        self.grid.addWidget(self.push_status, 3, 1)
        self.setLayout(self.grid)

        # message boxes
        self.default_message = QMessageBox()

        # init key file location
        with open (self.config_filename, "r") as config_file:
            key_file_line = config_file.readline()
            key_file = key_file_line.split(" ")[-1]
            if key_file == "None":
                self.key_file = None
            else:
                self.key_file = key_file
                self.key_line_edit.setText(key_file)

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
            self.file_list.addItems(self.filenames)

    def key_file_select(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        if file_dialog.exec_():
            self.key_file = file_dialog.selectedFiles()[0]
            self.key_line_edit.setText(self.key_file)
            # attempt to set as default
            self.default_message.question(self, "", "Would you like to set this key file as the default?", self.default_message.Yes | self.default_message.No)
            if self.default_message.Yes:

                with open(self.config_filename, "r") as config_file:
                    data = config_file.readlines()
                
                with open(self.config_filename, "w") as config_file:
                    data[0] = "key_file = " + self.key_file
                    config_file.writelines(data)


    def execute_push(self):
        if self.key_file is None:
            self.push_status.setText("No key file selected!")
        else:
            push_pics(self.filenames, self.key_file, self.device, self.channel)
            self.push_status.setText("Pushed!")


def main():
    app = QApplication(sys.argv)
    ui_obj = push_pics_ui()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()