# -*- coding: utf-8 -*-
from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QLineEdit, QPushButton, QWidget)
import sys

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(580, 433)

        # QLineEdit (Nombre)
        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(230, 100, 113, 21))

        # QComboBox (Rol)
        self.comboBox = QComboBox(Dialog)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(230, 160, 113, 24))
        self.comboBox.addItems(["Alumno", "Profe", "Invitado"])

        # QCheckBox (Acepto normas)
        self.checkBox = QCheckBox(Dialog)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(230, 210, 120, 20))

        # QPushButton (Enviar)
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(230, 270, 113, 24))

        self.retranslateUi(Dialog)
        QMetaObject.connectSlotsByName(Dialog)

        # --- Conexión del botón con la validación ---
        self.pushButton.clicked.connect(self.enviar)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Formulario", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"Nombre", None))
        self.checkBox.setText(QCoreApplication.translate("Dialog", u"Acepto normas", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Enviar", None))

    def enviar(self):
        nombre = self.lineEdit.text()
        rol = self.comboBox.currentText()
        acepta = self.checkBox.isChecked()

        if not nombre or not acepta:
            print("Faltan datos")
        else:
            print(f"Nombre: {nombre} | Rol: {rol} | Acepta: Sí")


# --- Programa principal ---
if __name__ == "__main__":
    app = QApplication(sys.argv)
    Dialog = QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())