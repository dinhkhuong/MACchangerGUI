from PyQt5 import QtWidgets, QtGui

from MACchangerGUI import Ui_Dialog
from MACchangerModular import *
import netifaces
import sys

    
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    # copy the __main__ section from GUI .py file
    # use an Ui_Dialog object to handle GUI functionality

    # netifaces return all network interfaces in current machine
    net = netifaces.interfaces()
    ulist = ui.comboBox_intfce
    for i in net:
        ulist.addItem(i)
    
    #netifaces when MAC not detected, return KeyError 18 and Abort Trap 6, try to bypass them:
    #https://stackoverflow.com/questions/42405072/python-network-interface-scan
    def showM(uItem):
        curM = netifaces.ifaddresses(uItem)
        try:
            ui.label_curent_MAC.setText(curM[netifaces.AF_LINK][0]['addr'])
        except KeyError:
            ui.label_curent_MAC.setText('No MAC available for '+ uItem)
        
    def GUIchangeMAC():
        text = ui.textEdit.toPlainText()
        
        #call functions from Modular
        if isValidMACAddress(text):             

        # Linux
            if sys.platform == "linux" or sys.platform == "linux2":
                change_linuxMAC(ulist.itemText(ulist.currentIndex()),text)
        # MAC os X
            elif sys.platform == "darwin":
                change_macMAC(ulist.itemText(ulist.currentIndex()),text)
        # Windows
            elif sys.platform == "win32":
                change_windowsMAC(ulist.itemText(ulist.currentIndex()),text)
                ui.label_curent_MAC.setText("<font color='Green'>Restart your computer for change to take effect</font>")
            elif sys.platform == "win64":
                change_windowsMAC(ulist.itemText(ulist.currentIndex()),text)
                ui.label_curent_MAC.setText("<font color='Green'>Restart your computer for change to take effect</font>")
        else:
            ui.label_curent_MAC.setText("<font color='Red'>MAC address contains <b>12 hexadecimal</b> digits <br>Please input a valid MAC address</font>")
    def GUIresetMAC():
        text = ui.textEdit.toPlainText()
        if sys.platform == "win32":
            reset_windowsMAC(ulist.itemText(ulist.currentIndex()),text)
            ui.label_curent_MAC.setText("<font color='Green'>Restart your computer for change to take effect</font>")
        if sys.platform == "win64":
            reset_windowsMAC(ulist.itemText(ulist.currentIndex()),text)
            ui.label_curent_MAC.setText("<font color='Green'>Restart your computer for change to take effect</font>")
    #use lambda to keep scaning network functions concurrent with GUI     
    ulist.currentIndexChanged.connect(lambda: showM(ulist.itemText(ulist.currentIndex())))
    
    ui.pushButton1.clicked.connect(lambda: GUIchangeMAC())
    ui.pushButton2.clicked.connect(lambda: GUIresetMAC())
     
    Dialog.show()
    sys.exit(app.exec_())


