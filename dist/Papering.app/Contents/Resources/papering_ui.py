from PyQt6.QtWidgets import QApplication, QLabel, QPushButton, QWidget, \
     QMainWindow, QVBoxLayout, QHBoxLayout, QComboBox, QMessageBox
from PyQt6.QtGui import QFont, QFontDatabase, QIcon
from PyQt6 import QtCore
from PyQt6.QtGui import QCursor
import sys
from papering_def import openUrl
from papering_database import PaperData


class Main(QMainWindow):
    def __init__(self):
        super().__init__()

        # setting the Vbox layout
        v_layout = QVBoxLayout()
        subject_layout = QVBoxLayout()
        year_layout = QVBoxLayout()
        season_layout = QVBoxLayout()
        paper_layout = QVBoxLayout()
        selection_layout = QHBoxLayout()

        self.setWindowTitle("PAPERING")
        self.setFixedWidth(600)
        self.setFixedHeight(450)
        self.setStyleSheet("background: #F7F6F3;")

        QFontDatabase.addApplicationFont("./fonts/ShareTech-Regular.ttf")
        QFontDatabase.addApplicationFont("./fonts/Audiowide-Regular.ttf")
        self.font = QFont('Share Tech')
        self.h_font = QFont('Audiowide')

        # Display banner
        label = QLabel('Papering')
        label.setFont(self.h_font)
        label.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
        label.setStyleSheet(
            "font-size: 110px;" +
            "margin-top: 40px;" +
            "font-weight: bold;"
        )

        # Display the tagline
        subject = QLabel('subject')
        subject.setFont(self.font)
        subject.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom)
        subject.setStyleSheet(
            "font-size: 30px;" +
            "color: black;"
        )

        year = QLabel('year')
        year.setFont(self.font)
        year.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom)
        year.setStyleSheet(
            "font-size: 30px;" +
            "color: black;"
        )

        season = QLabel('season')
        season.setFont(self.font)
        season.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom)
        season.setStyleSheet(
            "font-size: 30px;" +
            "color: black;"
        )

        paper = QLabel('paper')
        paper.setFont(self.font)
        paper.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom)
        paper.setStyleSheet(
            "font-size: 30px;" +
            "color: black;"
        )

        # Create an SUBJECT WIDGET
        self.subject_list = QComboBox()
        self.subject_list.setFont(self.font)
        self.subject_list.setStyleSheet(
            "QComboBox {"
            "border:5px solid black; "
            "padding:5px;  "  
            "font-size:22px; "
            "font-family:Share tech;"
            "color: black;\n"
            "line-height:24px; }\n"

            "QComboBox:drop-down {"  # 选择箭头样式
            "width:20px;  "
            "height:20px; "
            "border: 0; "
            "margin-right: 5px;"
            "subcontrol-position: right center; "  # 位置
            "subcontrol-origin: padding;}\n"  # 对齐方式
            
            "QComboBox:down-arrow {"  # 选择箭头，继承drop-down
            "border: none; "
            "background: transparent; "
            "image: url(\"./icons/arrow-down-filling.png\");}\n"

            "QComboBox QAbstractItemView {"  # 下拉选项样式
            "color:black; "
            "background: '#ECECEC'; "
            "selection-color: white;"
            "selection-background-color: black;"
            "}\n"

            "QComboBox QAbstractScrollArea QScrollBar:vertical {"  # 滚动条样式
            "width: 10px;\n"
            "height: 100px;"
            "background-color: white;  }\n"

            "QComboBox QAbstractScrollArea QScrollBar::handle:vertical {\n"  # 滚动条样式
            "background: black;}\n"
        )
        self.subject_list.setEditable(True)
        subject_data = PaperData()
        subject_list_arr = subject_data.subject()
        self.subject_list.addItems(subject_list_arr)

        # Create an YEAR WIDGET
        self.year_list = QComboBox()
        self.year_list.setFont(self.font)
        self.year_list.setStyleSheet(
            "QComboBox {"
            "border:5px solid black; "
            "padding:5px;  "
            "font-size:22px; "
            "font-family:Share tech;"
            "color: black;\n"
            "line-height:24px; }\n"

            "QComboBox:drop-down {"  # 选择箭头样式
            "width:20px;  "
            "height:20px; "
            "border: 0; "
            "margin-right: 5px;"
            "subcontrol-position: right center; "  # 位置
            "subcontrol-origin: padding;}\n"  # 对齐方式

            "QComboBox:down-arrow {"  # 选择箭头，继承drop-down
            "border: none; "
            "background: transparent; "
            "image: url(\"./icons/arrow-down-filling.png\");}\n"

            "QComboBox QAbstractItemView {"  # 下拉选项样式
            "color:black; "
            "background: '#ECECEC'; "
            "selection-color: white;"
            "selection-background-color: black;"
            "}\n"

            "QComboBox QAbstractScrollArea QScrollBar:vertical {"  # 滚动条样式
            "width: 10px;\n"
            "height: 100px;"
            "background-color: white;  }\n"

            "QComboBox QAbstractScrollArea QScrollBar::handle:vertical {\n"  # 滚动条样式
            "background: black;}\n"
        )
        self.year_list.setEditable(True)
        year_data = PaperData()
        each_year = year_data.year()
        self.year_list.addItems(each_year)

        # Create an SEASON WIDGET
        self.season_list = QComboBox()
        self.season_list.setFont(self.font)
        self.season_list.setStyleSheet(
            "QComboBox {"
            "border:5px solid black; "
            "padding:5px;  "
            "font-size:22px; "
            "font-family:Share tech;"
            "color: black;\n"
            "line-height:24px; }\n"

            "QComboBox:drop-down {"  # 选择箭头样式
            "width:20px;  "
            "height:20px; "
            "border: 0; "
            "margin-right: 5px;"
            "subcontrol-position: right center; "  # 位置
            "subcontrol-origin: padding;}\n"  # 对齐方式

            "QComboBox:down-arrow {"  # 选择箭头，继承drop-down
            "border: none; "
            "background: transparent; "
            "image: url(\"./icons/arrow-down-filling.png\");}\n"

            "QComboBox QAbstractItemView {"  # 下拉选项样式
            "color:black; "
            "background: '#ECECEC'; "
            "selection-color: white;"
            "selection-background-color: black;"
            "}\n"
        )
        self.season_list.setEditable(True)
        self.season_list.addItems(['summer', 'winter', 'march'])

        # Create an PAPER WIDGET
        self.paper_list = QComboBox()
        self.paper_list.setFont(self.font)
        self.paper_list.setStyleSheet(
            "QComboBox {"
            "border:5px solid black; "
            "padding:5px;  "
            "font-size:22px; "
            "font-family:Share tech;"
            "color: black;\n"
            "line-height:24px; }\n"

            "QComboBox:drop-down {"  # 选择箭头样式
            "width:20px;  "
            "height:20px; "
            "border: 0; "
            "margin-right: 5px;"
            "subcontrol-position: right center; "  # 位置
            "subcontrol-origin: padding;}\n"  # 对齐方式

            "QComboBox:down-arrow {"  # 选择箭头，继承drop-down
            "border: none; "
            "background: transparent; "
            "image: url(\"./icons/arrow-down-filling.png\");}\n"

            "QComboBox QAbstractItemView {"  # 下拉选项样式
            "color:black; "
            "background: '#ECECEC'; "
            "selection-color: white;"
            "selection-background-color: black;"
            "}\n"
        )
        self.paper_list.setEditable(True)
        self.paper_list.addItems(['11', '12', '13', '...'])

        # Create a BUTTON WIDGET
        # 如果由多个object在图像中，需要谨慎加padding， margin。
        button = QPushButton("SEARCH")
        button.setCursor(QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        button.setStyleSheet(
            "*{border: 6px solid '#111111';" +
            "border-radius: 12px;" +
            "font-size: 30px;" +
            "font-weight: semi-bold;"
            "color: 'black';" +
            "padding: 10px 0;" +
            "margin: 0px 5px 35px}" +
            "*:hover{background: '#111111'; color: 'white'}"
        )
        button.clicked.connect(self.search_button)
        # 直接等于函数名字，即可应用函数，不需要加括号

        # add the widget into a vertical layout
        subject_layout.addWidget(subject)
        subject_layout.addWidget(self.subject_list)

        year_layout.addWidget(year)
        year_layout.addWidget(self.year_list)

        season_layout.addWidget(season)
        season_layout.addWidget(self.season_list)

        paper_layout.addWidget(paper)
        paper_layout.addWidget(self.paper_list)

        # put all the widget component into a horizontal layout
        selection_layout.addLayout(subject_layout)
        selection_layout.addLayout(year_layout)
        selection_layout.addLayout(season_layout)
        selection_layout.addLayout(paper_layout)

        # add the widget into main vertical layout
        v_layout.addWidget(label)
        v_layout.addLayout(selection_layout)
        v_layout.addWidget(button)

        main_frame = QWidget()
        self.setCentralWidget(main_frame)
        main_frame.setLayout(v_layout)

    def search_button(self):
        current_subject = self.subject_list.currentText()
        current_year = self.year_list.currentText()
        current_season = self.season_list.currentText()
        current_paper = self.paper_list.currentText()
        # Search for the paper, if not found then return a window that shown error
        if current_paper == "...":
            error = QMessageBox()
            error.setText("Oh, It seems you are not enter a valid paper!")
            error.setFont(self.font)
            error.setIcon(QMessageBox.Icon.Warning)
            error.setStyleSheet(
                "font-size: 18px;"
            )
            error.exec()
        else:
            openUrl(current_subject, current_year, current_season, current_paper)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec())
