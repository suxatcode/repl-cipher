from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit,
                             QInputDialog, QApplication)
import sys
from cipher import cipher


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        buttons = [
            ["Alphabet 1", self.setAlphabet1],
            ["Alphabet 2", self.setAlphabet2],
            ["plaintext", self.setPlaintext],
            ["ciphertext", self.setCiphertext],
        ]
        self.input_btns = []
        self.input_states = []
        for button, n in zip(buttons, range(len(buttons))):
            offset = (n+1)*2
            self.input_btns.append(QPushButton(button[0], self))
            self.input_btns[-1].move(20, offset*20)
            self.input_btns[-1].clicked.connect(button[1])
            self.input_states.append(QLineEdit(self))
            self.input_states[-1].move(130, offset*22)
        self.encrypt_btn = QPushButton("encrypt", self)
        self.encrypt_btn.clicked.connect(self.encrypt)
        #self.decrypt_btn = QPushButton("decrypt", self)
        self.setGeometry(300, 300, 450, 350)
        self.setWindowTitle('Replacement Cipher')
        self.show()

    def setAlphabet1(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter alphabet 1:')
        if ok:
            self.input_states[0].setText(str(text))

    def setAlphabet2(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter alphabet 2:')
        if ok:
            self.input_states[1].setText(str(text))

    def setPlaintext(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter plaintext:')
        if ok:
            self.input_states[2].setText(str(text))

    def setCiphertext(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter ciphertext:')
        if ok:
            self.input_states[3].setText(str(text))

    def encrypt(self):
        key = [
            self.input_states[0].text(),
            self.input_states[1].text(),
        ]
        plaintext = self.input_states[2].text()
        ciphertext = cipher(key, plaintext)
        self.input_states[3].setText(ciphertext)

def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
