import sys
from PySide6.QtCore import QCoreApplication, QMetaObject, QRect, QTimer, Qt
from PySide6.QtWidgets import (
    QApplication, QDialog, QProgressBar, QPushButton, QTimeEdit,
    QListWidget, QListWidgetItem
)


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName("Dialog")
        Dialog.resize(613, 498)

        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setGeometry(QRect(240, 230, 79, 24))

        self.progressBar = QProgressBar(Dialog)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setGeometry(QRect(220, 270, 300, 23))
        self.progressBar.setValue(0)
        self.progressBar.setRange(0, 100)

        self.timeEdit = QTimeEdit(Dialog)
        self.timeEdit.setObjectName("timeEdit")
        self.timeEdit.setGeometry(QRect(220, 310, 118, 23))

        # Añadimos la QListWidget
        self.listWidget = QListWidget(Dialog)
        self.listWidget.setObjectName("listWidget")
        # colocación y tamaño (ajusta si quieres)
        self.listWidget.setGeometry(QRect(220, 50, 300, 150))

        self.retranslateUi(Dialog)
        QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", "Repaso 3", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", "Iniciar", None))


class Dialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # Estado de la simulación
        self._progress_value = 0

        # QTimer para simular la descarga/avanzar la barra
        self.timer = QTimer(self)
        self.timer.setInterval(50)  # 50 ms por tick -> ajusta velocidad
        self.timer.timeout.connect(self._on_timeout)

        # Conectar botón
        self.pushButton.clicked.connect(self.start_progress)

        # Rellenar la lista con 3 tareas
        for i in range(1, 4):
            item = QListWidgetItem(f"Tarea {i}")
            self.listWidget.addItem(item)

        # Conectar doble clic (signal: doubleClicked -> QModelIndex)
        self.listWidget.doubleClicked.connect(self.on_task_double_clicked)

    def start_progress(self):
        """Inicia la animación de la barra desde 0 hasta 100."""
        # Si ya estamos en marcha, no reiniciamos
        if self.timer.isActive():
            return

        # Reiniciar estado
        self._progress_value = 0
        self.progressBar.setValue(0)
        # Desactivar botón mientras avanza
        self.pushButton.setEnabled(False)
        # Iniciar timer
        self.timer.start()

    def _on_timeout(self):
        """Handler llamado por cada tick del QTimer."""
        # Incremento simple: 1% por tick (ajustable)
        self._progress_value += 1
        if self._progress_value > 100:
            self._progress_value = 100

        self.progressBar.setValue(self._progress_value)

        if self._progress_value >= 100:
            # Detener timer y reactivar botón
            self.timer.stop()
            self.pushButton.setEnabled(True)
            # Opcional: imprimir en consola que terminó
            print("Progreso completado (100%).")

    def on_task_double_clicked(self, index):
        """
        index: QModelIndex de la tarea clicada.
        Imprime en consola el texto de la tarea.
        """
        item = self.listWidget.item(index.row())
        if item:
            print(f"Has hecho doble clic en {item.text()}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlg = Dialog()
    dlg.show()
    sys.exit(app.exec())