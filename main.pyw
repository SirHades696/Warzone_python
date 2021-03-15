from SimpleWarzoneStatsTracker import *
import sys
from stats import WarzoneStats
class Warzone(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.psn.clicked.connect(self.psn_control)
        self.ui.xbox.clicked.connect(self.xbox_control)
        self.ui.steam.clicked.connect(self.steam_control)
        self.ui.battle.clicked.connect(self.battle_control)
        self.ui.search.clicked.connect(self.warzone_stats)
        self.platform = None
        self.error= QtWidgets.QErrorMessage()
    
    def warzone_stats(self):
        gt = self.ui.gametag.text()
        if self.platform == None:
            self.messagebox('Select a platform')
        elif self.ui.gametag.text() == '':
            self.messagebox('Enter a Gametag')
        elif self.platform == 'Battle.net' and '#' not in gt:
            self.messagebox('Enter a Gametag with #XXXX')
        elif self.platform == 'Battle.net' and '#' in gt and gt.split('#')[1] == '':
                self.messagebox('Enter a Gametag with this format #XXXX')
        else:
            war = WarzoneStats(gt,self.platform)
            message, battle, battle_wins, plunder, plunder_wins, all_br, all_wins = war.classify_stats()
            if message == None:
                self.ui.warzone.setText(battle)
                self.ui.warzone_wins.setText(battle_wins)
                self.ui.plunder.setText(plunder)
                self.ui.plunder_wins.setText(plunder_wins)
                self.ui.all.setText(all_br)
                self.ui.all_wins.setText(all_wins)
            else:
                self.ui.warzone.setText("")
                self.ui.warzone_wins.setText("")
                self.ui.plunder.setText("")
                self.ui.plunder_wins.setText("")
                self.ui.all.setText("")
                self.ui.all_wins.setText("")
                self.messagebox(message)

    def psn_control(self):
        self.ui.psn.setCheckable(True)
        self.ui.psn.toggle()
        if self.ui.psn.isChecked():
            self.platform = "PlayStation"
            self.ui.gametag.setPlaceholderText("Gametag")
            self.ui.psn.setStyleSheet("QPushButton#psn{background-color: #001039;}")
            self.ui.xbox.setStyleSheet("QPushButton#xbox{background-color: #001854;}")
            self.ui.steam.setStyleSheet("QPushButton#steam{background-color: #001854;}")
            self.ui.battle.setStyleSheet("QPushButton#battle{background-color: #001854;}")
    
    def xbox_control(self):
        self.ui.xbox.setCheckable(True)
        self.ui.xbox.toggle()
        if self.ui.xbox.isChecked():
            self.platform = "Xbox Live"
            self.ui.gametag.setPlaceholderText("Gametag")
            self.ui.xbox.setStyleSheet("QPushButton#xbox{background-color: #001039;}")
            self.ui.psn.setStyleSheet("QPushButton#psn{background-color: #001854;}")
            self.ui.steam.setStyleSheet("QPushButton#steam{background-color: #001854;}")
            self.ui.battle.setStyleSheet("QPushButton#battle{background-color: #001854;}")
    
    def steam_control(self):
        self.ui.steam.setCheckable(True)
        self.ui.steam.toggle()
        if self.ui.steam.isChecked():
            self.platform = "Steam"
            self.ui.gametag.setPlaceholderText("Gametag")
            self.ui.steam.setStyleSheet("QPushButton#steam{background-color: #001039;}")
            self.ui.psn.setStyleSheet("QPushButton#psn{background-color: #001854;}")
            self.ui.xbox.setStyleSheet("QPushButton#xbox{background-color: #001854;}")
            self.ui.battle.setStyleSheet("QPushButton#battle{background-color: #001854;}")

    def battle_control(self):
        self.ui.battle.setCheckable(True)
        self.ui.battle.toggle()
        if self.ui.battle.isChecked():
            self.platform = "Battle.net"
            self.ui.gametag.setPlaceholderText("Gametag#1234")
            self.ui.battle.setStyleSheet("QPushButton#battle{background-color: #001039;}")
            self.ui.psn.setStyleSheet("QPushButton#psn{background-color: #001854;}")
            self.ui.xbox.setStyleSheet("QPushButton#xbox{background-color: #001854;}")
            self.ui.steam.setStyleSheet("QPushButton#steam{background-color: #001854;}")

    def messagebox(self,text):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.setText("Warning")
        msg.setInformativeText(text)
        msg.setWindowTitle("Simple Warzone Stats Tracker")
        msg.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = Warzone()
    MainWindow.show()
    sys.exit(app.exec_())
