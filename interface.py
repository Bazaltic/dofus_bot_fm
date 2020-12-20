from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from utils_ui import *


class InterfaceFM(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("Dofus - Bot xp fm")
        self.setFixedSize(800, 210)
        self.stats = []
        self.box_y = 0
        self._create_settings_panel()
        self._create_run_button()
        self._create_item_panel()

        self.number_of_stats = 0

    def _create_settings_panel(self):
        self._create_settings_title()
        self._create_settings_number_of_stats()
        self._create_settings_number_of_damage_line()
        self._create_settings_number_of_rune()
        self._create_settings_allow_rune_pa()
        self._create_settings_allow_rune_ra()

    def _create_settings_title(self):
        settings_label = QLabel("SETTINGS", self)
        settings_label.setAlignment(Qt.AlignCenter)
        settings_label.setFixedSize(800, 30)
        settings_label.setFont(TITLE_FONT)
        settings_label.move(0, self.box_y)
        settings_label.setStyleSheet(TITLE_STYLESHEET)
        self.box_y = self.box_y + 30

    def _create_settings_number_of_stats(self):
        self.nos_label = QLabel("Number of stats line: ", self)
        self.nos_label.setFixedSize(400, 20)
        self.nos_label.move(0, self.box_y)
        self.nos_label.setAlignment(Qt.AlignCenter)
        self.nos_label.setStyleSheet(STYLESHEET_DARK_0)

        self.nos_cpt = QLineEdit(self)
        self.nos_cpt.setValidator(QIntValidator())
        self.nos_cpt.setAlignment(Qt.AlignCenter)
        self.nos_cpt.setFixedSize(400, 20)
        self.nos_cpt.move(400, self.box_y)
        self.nos_cpt.setStyleSheet(STYLESHEET_DARK_0)

        self.box_y = self.box_y + 20

    def _create_settings_number_of_damage_line(self):
        self.nodl_label = QLabel("Number of damage line : ", self)
        self.nodl_label.setFixedSize(400, 20)
        self.nodl_label.move(0, self.box_y)
        self.nodl_label.setAlignment(Qt.AlignCenter)
        self.nodl_label.setStyleSheet(STYLESHEET_DARK_1)
        self.nodl_cpt = QLineEdit(self)
        self.nodl_cpt.setValidator(QIntValidator())
        self.nodl_cpt.setAlignment(Qt.AlignCenter)
        self.nodl_cpt.setFixedSize(400, 20)
        self.nodl_cpt.move(400, self.box_y)
        self.nodl_cpt.setStyleSheet(STYLESHEET_DARK_1)
        self.box_y = self.box_y + 20

    def _create_settings_number_of_rune(self):
        self.nor_label = QLabel("How many rune : ", self)
        self.nor_label.setFixedSize(400, 20)
        self.nor_label.move(0, self.box_y)
        self.nor_label.setAlignment(Qt.AlignCenter)
        self.nor_label.setStyleSheet(STYLESHEET_DARK_0)
        self.nor_cpt = QLineEdit(self)
        self.nor_cpt.setValidator(QIntValidator())
        self.nor_cpt.setAlignment(Qt.AlignCenter)
        self.nor_cpt.setFixedSize(400, 20)
        self.nor_cpt.move(400, self.box_y)
        self.nor_cpt.setStyleSheet(STYLESHEET_DARK_0)
        self.box_y = self.box_y + 20

    def _create_settings_allow_rune_pa(self):
        self.arp_label = QLabel("Allow rune Pa : ", self)
        self.arp_label.setFixedSize(400, 20)
        self.arp_label.move(0, self.box_y)
        self.arp_label.setAlignment(Qt.AlignCenter)
        self.arp_label.setStyleSheet(STYLESHEET_DARK_1)
        self.arp_cpt = QCheckBox(self)
        self.arp_cpt.setFixedSize(400, 20)
        self.arp_cpt.move(400, self.box_y)
        self.arp_cpt.setStyleSheet(STYLESHEET_DARK_1)
        self.box_y = self.box_y + 20

    def _create_settings_allow_rune_ra(self):
        self.arr_label = QLabel("Allow rune Ra : ", self)
        self.arr_label.setFixedSize(400, 20)
        self.arr_label.move(0, self.box_y)
        self.arr_label.setAlignment(Qt.AlignCenter)
        self.arr_label.setStyleSheet(STYLESHEET_DARK_0)
        self.arr_cpt = QCheckBox(self)
        self.arr_cpt.setFixedSize(400, 20)
        self.arr_cpt.move(400, self.box_y)
        self.arr_cpt.setStyleSheet(STYLESHEET_DARK_0)
        self.box_y = self.box_y + 20

    def _create_item_panel(self):
        self._create_item_title()
        self._create_item_stat_header()
        self.box_y_base = self.box_y
        for i in range(50):
            self._create_item_line(STYLESHEET_DARK_0 if i % 2 == 0 else STYLESHEET_DARK_1)

    def _create_item_title(self):
        self.item_label = QLabel("ITEM", self)
        self.item_label.setAlignment(Qt.AlignCenter)
        self.item_label.setFixedSize(800, 30)
        self.item_label.setFont(TITLE_FONT)
        self.item_label.move(0, self.box_y)
        self.item_label.setStyleSheet(TITLE_STYLESHEET)
        self.box_y = self.box_y + 30

    def _create_item_stat_header(self):
        self.minimum_label_header = QLabel("Minimum", self)
        self.minimum_label_header.setFixedSize(115, 25)
        self.minimum_label_header.move(0, self.box_y)
        self.minimum_label_header.setAlignment(Qt.AlignCenter)
        self.minimum_label_header.setStyleSheet(STYLESHEET_HEADER)

        self.maximum_label_header = QLabel("Maximum", self)
        self.maximum_label_header.setFixedSize(115, 25)
        self.maximum_label_header.move(115, self.box_y)
        self.maximum_label_header.setAlignment(Qt.AlignCenter)
        self.maximum_label_header.setStyleSheet(STYLESHEET_HEADER)

        self.effect_label_header = QLabel("Current", self)
        self.effect_label_header.setFixedSize(115, 25)
        self.effect_label_header.move(230, self.box_y)
        self.effect_label_header.setAlignment(Qt.AlignCenter)
        self.effect_label_header.setStyleSheet(STYLESHEET_HEADER)

        self.modify_label_header = QLabel("Modify", self)
        self.modify_label_header.setFixedSize(115, 25)
        self.modify_label_header.move(345, self.box_y)
        self.modify_label_header.setAlignment(Qt.AlignCenter)
        self.modify_label_header.setStyleSheet(STYLESHEET_HEADER)

        self.base_label_header = QLabel("Rune base", self)
        self.base_label_header.setFixedSize(115, 25)
        self.base_label_header.move(460, self.box_y)
        self.base_label_header.setAlignment(Qt.AlignCenter)
        self.base_label_header.setStyleSheet(STYLESHEET_HEADER)

        self.pa_label_header = QLabel("Rune Pa", self)
        self.pa_label_header.setFixedSize(115, 25)
        self.pa_label_header.move(575, self.box_y)
        self.pa_label_header.setAlignment(Qt.AlignCenter)
        self.pa_label_header.setStyleSheet(STYLESHEET_HEADER)

        self.ra_label_header = QLabel("Rune Ra", self)
        self.ra_label_header.setFixedSize(115, 25)
        self.ra_label_header.move(690, self.box_y)
        self.ra_label_header.setAlignment(Qt.AlignCenter)
        self.ra_label_header.setStyleSheet(STYLESHEET_HEADER)
        self.box_y = self.box_y + 25

    def _create_item_line(self, style):
        minimum_label = QLabel("21", self)
        minimum_label.setFixedSize(115, 20)
        minimum_label.move(0, self.box_y)
        minimum_label.setAlignment(Qt.AlignCenter)
        minimum_label.setStyleSheet(style)

        maximum_label = QLabel("50", self)
        maximum_label.setFixedSize(115, 20)
        maximum_label.move(115, self.box_y)
        maximum_label.setAlignment(Qt.AlignCenter)
        maximum_label.setStyleSheet(style)

        effect_label = QLabel("42", self)
        effect_label.setFixedSize(115, 20)
        effect_label.move(230, self.box_y)
        effect_label.setAlignment(Qt.AlignCenter)
        effect_label.setStyleSheet(style)

        modify_label = QLabel("+5", self)
        modify_label.setFixedSize(115, 20)
        modify_label.move(345, self.box_y)
        modify_label.setAlignment(Qt.AlignCenter)
        modify_label.setStyleSheet(style)

        base_label = QLabel("True", self)
        base_label.setFixedSize(115, 20)
        base_label.move(460, self.box_y)
        base_label.setAlignment(Qt.AlignCenter)
        base_label.setStyleSheet(style)

        pa_label = QLabel("True", self)
        pa_label.setFixedSize(115, 20)
        pa_label.move(575, self.box_y)
        pa_label.setAlignment(Qt.AlignCenter)
        pa_label.setStyleSheet(style)

        ra_label = QLabel("True", self)
        ra_label.setFixedSize(115, 20)
        ra_label.move(690, self.box_y)
        ra_label.setAlignment(Qt.AlignCenter)
        ra_label.setStyleSheet(style)

        self.stats.append(
            {
                "minimum": minimum_label,
                "maximum": maximum_label,
                "effect": effect_label,
                "modify": modify_label,
                "rune_base": base_label,
                "rune_pa": pa_label,
                "rune_ra": ra_label
            }
        )

        self.box_y = self.box_y + 20

    def _create_run_button(self):
        self.run_button = QPushButton("Run", self)
        self.run_button.setFixedSize(800, 25)
        self.run_button.move(0, self.box_y)
        self.run_button.setStyleSheet(STYLESHEET_BUTTON)
        self.run_button.clicked.connect(self.run)
        self.box_y = self.box_y + 25

    def run(self):
        try:
            self.number_of_stats = int(self.nos_cpt.text())
            if self.number_of_stats < 0:
                self.nos_cpt.setText("0")
                self.number_of_stats = 0
            elif self.number_of_stats > 14:
                self.number_of_stats = 14
                self.nos_cpt.setText("14")
        except:
            self.number_of_stats = 0
        self.box_y = self.box_y_base
        self.setFixedSize(800, self.box_y)
        for i in range(self.number_of_stats):
            self.box_y = self.box_y + 20
            self.setFixedSize(800, self.box_y)

