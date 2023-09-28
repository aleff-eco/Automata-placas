from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import Qt
from interfaz import Ui_Dialog


transiciones = [('Q0', 'Q1', 'K'), ('Q0', 'Q2', 'L'), ('Q0', 'Q3', 'M'),
                ('Q1', 'Q4', 'LMNÑOPQRSTUVWXYZ'), ('Q2', 'Q4', 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'), ('Q3', 'Q4', 'ABCDEFGHIJKLMNÑOPQRS'),
                ('Q4', 'Q5', '-'), ('Q5', 'Q6', '0'), ('Q5', 'Q10', '123456789'),
                ('Q10', 'Q11', '0123456789'), ('Q6', 'Q7', '0'),('Q11', 'Q12', '0123456789'),('Q12', 'Q9', '0123456789'), ('Q6', 'Q11', '0123456789'),
                ('Q7', 'Q13', '123456789'), ('Q13', 'Q9', '0123456789'), ('Q7', 'Q8', '0'),
                ('Q8', 'Q9', '1'), ('Q9', 'Q14', '-'), ('Q14', 'Q15', 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ')]

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.verificar_placa)

    def mostrar_mensaje(self, mensaje):
        QMessageBox.information(self, "Validacion de la Placa", mensaje)

    def verificar_placa(self):
            placa = self.ui.lineEdit.text()
            estado = 'Q0'
            mensaje = f"Inicio: Estado {estado}\n\n"

            for i, c in enumerate(placa):
                estado_anterior = estado
                nueva_transicion = None
                transicion_realizada = False

                for transicion in transiciones:
                    if transicion[0] == estado and c in transicion[2]:
                        estado = transicion[1]
                        nueva_transicion = transicion
                        transicion_realizada = True
                        break

                if transicion_realizada:
                    print(f"Transicion: {nueva_transicion[0]} -> {nueva_transicion[1]}")
                    mensaje += f"Caracter {c}: Transicion {nueva_transicion[0]} -> {nueva_transicion[1]}\n"
                else:
                    print(f"No se puede realizar transición desde el estado {estado_anterior} con el caracter {c}")
                    print(f"La placa {placa} no es valida.")
                    mensaje += f"Caracter {c}: No se puede realizar transición desde el estado {estado_anterior} con el caracter {c}\n"
                    mensaje += f"\nLa placa {placa} no cumple."
                    mensaje += f"\nEl estado final es: {estado} ."
                    self.ui.listWidget_invalidas.addItem(placa)
                    self.mostrar_mensaje(mensaje)
                    return

            if estado == 'Q15':
                print(f"La placa {placa} SI sirve.")
                mensaje += f"\nLa placa {placa} es valida."
                mensaje += f"\nEl estado final es: {estado} ."
                self.mostrar_mensaje(mensaje)
                self.ui.listWidget_validas.addItem(placa)

if __name__ == "__main__":
    app = QApplication([])
    window = MyApp()
    window.show()
    app.exec_()
