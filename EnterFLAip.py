#!/bin/env/python
# An introduction sample source code for some basic statistics
# Assignment 1 in ME7863: Design and Analysis of Experiments
# Taught By Dr. Jeremy Daily
# Orignially assigned Fall 2017
#
# This is a gentle introduction to programming using Python, numpy, scipy, and PyQt5
#Import 
import sys
from PyQt5.QtWidgets import (QMainWindow,
                             QComboBox,
                             QWidget,
                             QFileDialog,
                             QMessageBox,
                             QLabel, 
                             QCheckBox, 
                             QVBoxLayout, 
                             QHBoxLayout, 
                             QApplication, 
                             QPushButton,
                             QGroupBox,
                             QLineEdit)
from PyQt5.QtCore import Qt,QCoreApplication
from PyQt5.QtGui import QIntValidator,QIcon

class DiscoverFLAs(QMainWindow):

    #The init function always runs upon instantiation
    def __init__(self):
        super().__init__() #initializes the inherited class
        self.setWindowIcon(QIcon('synerconlogo.ico'))
        # Upon startup, run a user interface routine
        self.init_ui()
              
    def init_ui(self):
        #Builds GUI
        #self.setGeometry(200,200,300,100)
        #self.statusBar().showMessage("Specify Forensic Link Adapter Connection")
        self.ip_validator = QIntValidator(0, 255, self)
        #ip_box = QGroupBox("FLA IP Address:")
        ip_widget = QWidget()
        h_layout = QHBoxLayout()
        ip_widget.setLayout(h_layout)
        default_ip = ['192','168','7','2']
        self.ip_entry=[]
        for position in range(4):
            self.ip_entry.append(QLineEdit())
            self.ip_entry[position].setText(default_ip[position])
            self.ip_entry[position].setFixedWidth(30)
            self.ip_entry[position].setValidator(self.ip_validator)
            #self.ip_entry[position].setSizeAdjustPolicy(QSizePoliy.Fixed)
            h_layout.addWidget(self.ip_entry[position])
            if position < 3:
                h_layout.addWidget(QLabel('.'))
        
        set_button = QPushButton("Set FLA IP Address for RP1210",self)
        set_button.clicked.connect(self.write_ini_file)
        # self.fla_combo_box = QComboBox()
        # self.fla_combo_box.setInsertPolicy(QComboBox.NoInsert)
        # self.fla_combo_box.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        # self.fla_combo_box.activated.connect(self.write_ini_file)
        
        self.connection_label = QLabel("Forensic Link Adapter IP Address:",self)
        
        v_layout = QVBoxLayout()
        
        v_layout.addWidget(self.connection_label)
        v_layout.addWidget(ip_widget)
        v_layout.addWidget(set_button)
        main_widget = QWidget()
        main_widget.setLayout(v_layout)
        self.setCentralWidget(main_widget)
        
        self.setWindowTitle('FLA')
        self.show()
 
    def write_ini_file(self): 
        ip_and_port_text = ''
        for field in self.ip_entry:
            ip_and_port_text += field.text()
            ip_and_port_text +='.'
        ip_and_port_text = ip_and_port_text[:-1] + ':7777\n'
        print(ip_and_port_text)
        file_text = '''[VendorInformation]
;--------------------------------------------------------------------------------
; Synercon Technologies, LLC - RP1210 Vendor INI File for the Forensic Adapter
;-------------------------------------------------------------------------------
;
; Author:     Kenneth DeGrant
; Date:       July 17, 2017
; Version:    1.0
;
;-------------------------------------------------------------------------------
Name=Forensic Link Adapter - Synercon Technologies, Inc.
Address1=125 West Third Street
Address2=
City=Tulsa
State=OK
Country=USA
Postal=74103
Telephone=937-238-4907
Fax=
VendorURL=http://www.synercontechnologies.com
MessageString=RP1210_MSG
ErrorString=RP1210_ERR

;-------------------------------------------------------------------------------
; Timestamp weight of 1000 microseconds (1ms)
;-------------------------------------------------------------------------------
TimestampWeight=1000

;-------------------------------------------------------------------------------
; The device defined in this INI file is "auto-detect" capable
;-------------------------------------------------------------------------------
AutoDetectCapable=Yes

;-------------------------------------------------------------------------------
; This INI file version/revision
;-------------------------------------------------------------------------------
Version=1.0

;-------------------------------------------------------------------------------
; This INI file is RP1210 C Compliant
;-------------------------------------------------------------------------------
RP1210=C
 
;-------------------------------------------------------------------------------
; This adapter does not have a 64-bit DLL.
;-------------------------------------------------------------------------------
DLLName64Bit=

;-------------------------------------------------------------------------------
; When a connecting "Baud=Auto", the amount of time DLL waits for a baud rate.
;   Default to 4 seconds.
;-------------------------------------------------------------------------------
AutoBaudCANConnectTimeout=4000

;-------------------------------------------------------------------------------
; Force CAN Auto Baud Rate detection (1=TRUE, 0=FALSE).
;-------------------------------------------------------------------------------
AutoBaudCANByDefault=0
 
;-------------------------------------------------------------------------------
; Synercon Supports API Level Debugging (Levels 0 - 4)
;
; To use API level debugging, modify the DebugLevel variable to:
;
; 0 = No debugging to be accomplished (default).
; 1 = Only Connect/Disconnect/Error Messages.
; 2 = Add RP1210_SendCommand calls.
; 3 = Add all Sent Messages (with filtering).
; 4 = Add all Received Messages (with filtering).
;
; The variable DebugFile is the file where you want to write the information.
;
; The DebugFileSize variable is how many 1k chunks you will allow the API to
; write before it begins to write over previously written entries. A value
; of 1024 is 1 megabyte (default).
;
; The DebugMode variable describes how the API will interact with the DebugFile.
; Should it overwrite (value = 0) any previous entries or should it append
; entries (value = 1) to the end of the file.
;-------------------------------------------------------------------------------
DebugLevel=4
DebugFile=c:\Synercon\Logs\FLA_RP1210.txt
DebugMode=0
DebugFileSize=1024

;-------------------------------------------------------------------------------
; This allows the lowest level of debugging. 0 = Off, 1 = On
;-------------------------------------------------------------------------------
HWDebugLevel=0
HWDebugFile=c:\Synercon\Logs\FLA_HW.txt

;-------------------------------------------------------------------------------
; Synercon Supports 1 concurrent RTS/CTS session and BAM session per client.
;-------------------------------------------------------------------------------
NumberOfRTSCTSSessions=1
 
;-------------------------------------------------------------------------------
; Synercon Supports standard connect as well as Baud=X, Channel=X.
;
; Format 1 =
;   fpchProtocol="CAN:Baud=X,SampleLocation=Y,SJW=Z,IDSize=S"
; Format 2 =
;   fpchProtocol="CAN:Baud=X,PROP_SEG=A,PHASE_SEG1=B,PHASE_SEG2=C,SJW=Z,IDSize=SS"
; Format 3 =
;   fpchProtocol="CAN:Baud=X,TSEG1=D,TSEG2=E,SJW=Z,IDSize=SS"
; Format 4 =
;   fpchProtocol="CAN"
; Format 5 =
;   fpchProtocol="CAN:Baud=X" (including "Baud=Auto")
;-------------------------------------------------------------------------------
CANFormatsSupported=4,5

;-------------------------------------------------------------------------------
; Synercon Supports standard connect as well as Baud=X, Channel=X.
;
; Format 1 =
;   fpchProtocol="J1939:Baud=X" (including "Baud=Auto")
; Format 2 =
;   fpchProtocol="J1939"
; Format 3 =
;   fpchProtocol="J1939:Baud=X,SampleLocation=Y,SJW=Z,IDSize=S"
; Format 4 =
;   fpchProtocol="J1939:Baud=X,PROP_SEG=A,PHASE_SEG1=B,PHASE_SEG2=C,SJW=Z,IDSize=SS"
; Format 5 =
;   fpchProtocol="J1939:Baud=X,TSEG1=D,TSEG2=E,SJW=Z,IDSize=SS"
;-------------------------------------------------------------------------------
J1939FormatsSupported=1,2
 
;-------------------------------------------------------------------------------
; Synercon supports protection of 1 J1939 address.
;-------------------------------------------------------------------------------
J1939Addresses=1

;-------------------------------------------------------------------------------
; This API supports CAN auto baud rate detection.
;-------------------------------------------------------------------------------
CANAutoBaud=TRUE

;-------------------------------------------------------------------------------
; Synercon Supports only J1708 at 9600 (default) - Format 2
;
; Format 1 =
;   fpchProtocol="J1708:Baud=X"
; Format 2 =
;   fpchProtocol="J1708"
;-------------------------------------------------------------------------------
J1708FormatsSupported=2

;-------------------------------------------------------------------------------
; Synercon Supports all 2 ISO15765 connect formats.
;
; Format 1 =
;   fpchProtocol="ISO15765:Baud=X" (including "Baud=Auto")
; Format 2 =
;   fpchProtocol="ISO15765"
;-------------------------------------------------------------------------------
ISO15765FormatsSupported=1,2

;-------------------------------------------------------------------------------
; Synercon Has 1 device, USB
;-------------------------------------------------------------------------------
Devices=1

;-------------------------------------------------------------------------------
; Synercon Supports all 10 RP1210 Protocols at various speeds.
;-------------------------------------------------------------------------------
Protocols=1,3,4,5

;--------------------------------------------------------------------------------
; Synercon Has 1 Device
;
; 1 Synercon Forensic Adapter
;-------------------------------------------------------------------------------
[DeviceInformation1]
DeviceID=1
DeviceDescription=Synercon Forensic Adapter
DeviceName=Synercon Forensic Adapter
DeviceParams='''
        file_text += ip_and_port_text
        file_text += '''MultiCANChannels=2
MultiJ1939Channels=2
MultiISO15765Channels=2

;--------------------------------------------------------------------------------
; Synercon Supports the following RP1210 Protocols at the Listed Speeds
;
; Y  1 = CAN      at 125k, 250k, 500k, 666k, 1000k, Auto Bitrate Detect
; N  2 = J2284    at 125k, 250k, 500k, 666k, 1000k, Auto Bitrate Detect
; Y  3 = J1939    at 125k, 250k, 500k, 666k, 1000k, Auto Bitrate Detect
; Y  4 = ISO15765 at 125k, 250k, 500k, 666k, 1000k, Auto Bitrate Detect
; Y  5 = J1708    at 9600, 19200, 38400, 57600, 115200, Auto Bitrate Detect
; N  6 = PLC      at 9600
; N  7 = J1850VPW at 10.4k
; N  8 = J1850PWM at 41.6k
; N  9 = ISO9141  at 10.4k
; N 10 = ISO14230 at 10.4k
;
;-------------------------------------------------------------------------------

[ProtocolInformation1]
ProtocolString=CAN
ProtocolDescription=CAN Network Protocol
ProtocolSpeed=125,250,500,666,1000,All,Auto
ProtocolParams=N/A
Devices=1

[ProtocolInformation2]
ProtocolString=J2284
ProtocolDescription=SAE J2284 Network Protocol (CAN @500k Baud)
ProtocolSpeed=125,250,500,666,1000,All,Auto
ProtocolParams=N/A
Devices=1

[ProtocolInformation3]
ProtocolString=J1939
ProtocolDescription=SAE J1939 Protocol
ProtocolSpeed=125,250,500,666,1000,All,Auto
ProtocolParams=N/A
Devices=1

[ProtocolInformation4]
ProtocolString=ISO15765
ProtocolDescription=ISO15765 Vehicle Protocol
ProtocolSpeed=125,250,500,666,1000,All,Auto
ProtocolParams=N/A
Devices=1

[ProtocolInformation5]
ProtocolString=J1708
ProtocolDescription=SAE J1708 Protocol
ProtocolSpeed=9600,19200,38400,57600,115200,All, Auto
ProtocolParams=N/A
Devices=1

[ProtocolInformation6]
ProtocolString=PLC
ProtocolDescription=Power Line Carrier (PLC4TRUCKS) Protocol
ProtocolSpeed=9600
ProtocolParams=N/A
Devices=1
 
[ProtocolInformation7]
ProtocolString=J1850PWM
ProtocolDescription=SAE J1850 Vehicle Protocol (PWM)
ProtocolSpeed=41.6
ProtocolParams=N/A
Devices=1

[ProtocolInformation8]
ProtocolString=J1850VPW
ProtocolDescription=SAE J1850 Vehicle Protocol (VPW)
ProtocolSpeed=10.4
ProtocolParams=N/A
Devices=1

[ProtocolInformation9]
ProtocolString=ISO9141
ProtocolDescription=Generic ISO9141
ProtocolSpeed=10.4
ProtocolParams=N/A
Devices=1

[ProtocolInformation10]
ProtocolString=ISO14230
ProtocolDescription=Generic ISO14230
ProtocolSpeed=10.4
ProtocolParams=N/A
Devices=1

;-------------------------------------------------------------------------------
; Synercon - RP1210 Vendor INI File
;-------------------------------------------------------------------------------
'''
        print(file_text)
        try:
            with open('c:\\windows\\synercon.ini','w') as ini_file:
                ini_file.write(file_text)
            success_dialog = QMessageBox()
            success_dialog.setIcon(QMessageBox.Information)
            success_dialog.setWindowTitle("File Written")
            success_dialog.setText("RP1210 INI File Successfully Written.")
            success_dialog.setWindowModality(Qt.ApplicationModal)
            success_dialog.exec_()
            self.close()
        except Exception as e:
            print(e)
            error_dialog = QMessageBox()
            error_dialog.setIcon(QMessageBox.Critical)
            error_dialog.setWindowTitle("File Error")
            error_dialog.setText("There was an error writing the synercon.ini file.\nTry running as an administrator.")
            error_dialog.setWindowModality(Qt.ApplicationModal)
            error_dialog.exec_()
            self.close()

# This is the main loop that starts the program. It stays at the end.
if __name__ == '__main__':
    #Start the program this way according to https://stackoverflow.com/questions/40094086/python-kernel-dies-for-second-run-of-pyqt5-gui
    app = QCoreApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
    execute = DiscoverFLAs()
    sys.exit(app.exec_())
