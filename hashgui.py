from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import sys
import hashlib

BLOCKSIZE = 65536


class Tela(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(Tela, self).__init__(*args, **kwargs)

        self.titulo = "Calculadora de Hash com PyQT5"
        self.esquerda = 10
        self.topo = 10
        self.largura = 630
        self.altura = 480

        self.lb_arquivo = QLabel("Arquivo", self)
        self.lb_arquivo.move(10, 10)
        self.lb_arquivo.resize(610, 30)
        self.lb_arquivo.setAlignment(Qt.AlignCenter)

        bt_arquivo = QPushButton("File Browser", self)
        bt_arquivo.move(10,40)
        bt_arquivo.resize(100, 30)
        bt_arquivo.pressed.connect(self.openFileNameDialog)

        self.le_arquivo = QLineEdit(self)
        self.le_arquivo.move(120, 40)
        self.le_arquivo.resize(500, 30)

        ############### Funções de Hash ###################

        self.lb_funcoes = QLabel("Funções de Hash", self)
        self.lb_funcoes.move(10, 90)
        self.lb_funcoes.resize(610, 30)
        self.lb_funcoes.setAlignment(Qt.AlignCenter)

        bt_md5 = QPushButton("md5", self)
        bt_md5.move(10, 120)
        bt_md5.resize(110, 30)
        # bt_md4.pressed.connect(lambda: self.lb_hash.setText(self.calcula_hash("md4")))
        bt_md5.pressed.connect(lambda: self.calcula_hash("md5"))

        bt_sha1 = QPushButton("SHA-1", self)
        bt_sha1.move(134, 120)
        bt_sha1.resize(110, 30)
        bt_sha1.pressed.connect(lambda: self.calcula_hash("sha1"))

        bt_sha224 = QPushButton("SHA-224", self)
        bt_sha224.move(258, 120)
        bt_sha224.resize(110, 30)
        bt_sha224.pressed.connect(lambda: self.calcula_hash("sha224"))

        bt_sha256 = QPushButton("SHA-256", self)
        bt_sha256.move(382, 120)
        bt_sha256.resize(110, 30)
        bt_sha256.pressed.connect(lambda: self.calcula_hash("sha256"))

        bt_sha384 = QPushButton("SHA-384", self)
        bt_sha384.move(506, 120)
        bt_sha384.resize(110, 30)
        bt_sha384.pressed.connect(lambda: self.calcula_hash("sha384"))

        bt_sha512 = QPushButton("SHA-512", self)
        bt_sha512.move(10, 164)
        bt_sha512.resize(110, 30)
        bt_sha512.pressed.connect(lambda: self.calcula_hash("sha512"))

        bt_sha3224 = QPushButton("SHA3-224", self)
        bt_sha3224.move(134, 164)
        bt_sha3224.resize(110, 30)
        bt_sha3224.pressed.connect(lambda: self.calcula_hash("sha3_224"))

        bt_sha3256 = QPushButton("SHA3-256", self)
        bt_sha3256.move(258, 164)
        bt_sha3256.resize(110, 30)
        bt_sha3256.pressed.connect(lambda: self.calcula_hash("sha3_256"))

        bt_sha3384 = QPushButton("SHA3-384", self)
        bt_sha3384.move(382, 164)
        bt_sha3384.resize(110, 30)
        bt_sha3384.pressed.connect(lambda: self.calcula_hash("sha3_384"))

        bt_sha3512 = QPushButton("SHA3-512", self)
        bt_sha3512.move(506, 164)
        bt_sha3512.resize(110, 30)
        bt_sha3512.pressed.connect(lambda: self.calcula_hash("sha3_512"))

        ################ Informações do hash ################

        self.lb_func = QLabel("Função", self)
        self.lb_func.move(0, 214)
        self.lb_func.resize(210, 30)
        self.lb_func.setAlignment(Qt.AlignCenter)

        self.lb_block = QLabel("Block Size", self)
        self.lb_block.move(210, 214)
        self.lb_block.resize(210, 30)
        self.lb_block.setAlignment(Qt.AlignCenter)

        self.lb_digest = QLabel("Digest Size", self)
        self.lb_digest.move(420, 214)
        self.lb_digest.resize(210, 30)
        self.lb_digest.setAlignment(Qt.AlignCenter)

        self.lb_func_result = QLabel("Função", self)
        self.lb_func_result.move(0, 244)
        self.lb_func_result.resize(210, 30)
        self.lb_func_result.setAlignment(Qt.AlignCenter)

        self.lb_block_result = QLabel(self)
        self.lb_block_result.move(210, 244)
        self.lb_block_result.resize(210, 30)
        self.lb_block_result.setAlignment(Qt.AlignCenter)

        self.lb_block_result = QLabel(self)
        self.lb_block_result.move(210, 244)
        self.lb_block_result.resize(210, 30)
        self.lb_block_result.setAlignment(Qt.AlignCenter)

        self.lb_digest_result = QLabel(self)
        self.lb_digest_result.move(420, 244)
        self.lb_digest_result.resize(210, 30)
        self.lb_digest_result.setAlignment(Qt.AlignCenter)

        self.lb_hash = QLabel("HASH", self)
        self.lb_hash.move(10, 294)
        self.lb_hash.resize(610, 30)
        self.lb_hash.setAlignment(Qt.AlignCenter)

        self.lb_hash_result = QLabel(self)
        self.lb_hash_result.move(10, 324)
        self.lb_hash_result.resize(2000, 30)
        self.lb_hash_result.setAlignment(Qt.AlignCenter)



        self.iniciar_tela()

    def iniciar_tela(self):
        self.setWindowTitle(self.titulo)
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)

        self.show()

    def calcula_hash(self, func):
        hash = hashlib.new(func)
        try:
            with open(self.le_arquivo.text(), 'rb') as arq:
                buf = arq.read(BLOCKSIZE)
                while len(buf) > 0:
                    hash.update(buf)
                    buf = arq.read(BLOCKSIZE)
        except PermissionError:
            print("Você não possui permissão carai!!!!!!!!!!!")

        self.lb_func_result.setText(func)
        self.lb_hash_result.setText(hash.hexdigest())
        self.lb_digest_result.setText(str(hash.digest_size))
        self.lb_block_result.setText(str(hash.block_size))

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            self.le_arquivo.setText(fileName)


app = QApplication(sys.argv)
app.setStyle("Fusion")
window = Tela()
window.show()

sys.exit(app.exec_())
