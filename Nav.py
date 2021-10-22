import sys
from PyQt5.QtWidgets import QMainWindow,QLineEdit,QPushButton, QApplication,QToolBar
from PyQt5.QtGui import QIcon,QFont
from PyQt5.QtCore import QSize,QUrl
from PyQt5.QtWebEngineWidgets import QWebEnginePage, QWebEngineView


class Window(QMainWindow):
    def __init__(self):
       super().__init__()
       

       self.setWindowTitle("Navegador")
       self.setWindowIcon(QIcon("icons/python.png"))
       self.setGeometry(200,200,900,600)

       toolbar=QToolBar()
       self.addToolBar(toolbar)
       
       #Boton de Retroceso(Atras)
       self.backButton= QPushButton()
       self.backButton.setIcon(QIcon("icons/back.png"))
       self.backButton.setIconSize(QSize(36,36))
       self.backButton.clicked.connect(self.backBTN)
       toolbar.addWidget(self.backButton)
       
       #Boton Retroceder(Adelante)
       self.forwardButton= QPushButton()
       self.forwardButton.setIcon(QIcon("icons/forward.png"))
       self.forwardButton.setIconSize(QSize(36,36))
       self.forwardButton.clicked.connect(self.forwardBTN)
       toolbar.addWidget(self.forwardButton)

       #Boton de Reinicio
       self.reloadButton= QPushButton()
       self.reloadButton.setIcon(QIcon("icons/reload.png"))
       self.reloadButton.setIconSize(QSize(36,36))
       self.reloadButton.clicked.connect(self.reloadBTN)
       toolbar.addWidget(self.reloadButton)
       
       #Boton de inicio
       self.HomeButton= QPushButton()
       self.HomeButton.setIcon(QIcon("icons/Home.png"))
       self.HomeButton.setIconSize(QSize(36,36))
       self.HomeButton.clicked.connect(self.homeBTN)
       toolbar.addWidget(self.HomeButton)


       #Barra de lineas
       self.addressLineEdit=QLineEdit()
       self.addressLineEdit.setFont(QFont("Sanserif", 15))
       self.addressLineEdit.returnPressed.connect(self.searchBTN)
       
       toolbar.addWidget(self.addressLineEdit)


       #Boton de Carga
       self.searchButton= QPushButton()
       self.searchButton.setIcon(QIcon("icons/whts.PNG"))
       self.searchButton.setIconSize(QSize(36,36))
       self.searchButton.clicked.connect(self.searchBTN)
       toolbar.addWidget(self.searchButton)


       #Web Engine
       self.webEngineView=QWebEngineView()
       self.setCentralWidget(self.webEngineView)
       initialURL= "https://google.com"
       self.addressLineEdit.setText(initialURL)
       self.webEngineView.load(QUrl(initialURL))


    def searchBTN(self):
      self.webEngineView.load(QUrl("https://web.whatsapp.com/"))
    
    def backBTN(self):
        self.webEngineView.back()
    
    def forwardBTN(self):
        self.webEngineView.forward()
    
    def reloadBTN(self):
        self.webEngineView.reload()
    
    def homeBTN(self):
        self.webEngineView.load(QUrl("https://google.com"))


app=QApplication(sys.argv)
window=Window()
window.show()
sys.exit(app.exec_())
     