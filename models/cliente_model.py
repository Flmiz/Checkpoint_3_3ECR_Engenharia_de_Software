import sqlite3
import pathlib

class Cliente_model():
    def __init__(self):
        self.connection = sqlite3.connect("/" + str(pathlib.Path(__file__).parents[1]).replace("\\", "/") + '/projetinho.db')
        self.cursor = self.connection.cursor()

    def salvar(self, nome, email, telefone):
        try:
            print("[model] salvando...")
            query = "CREATE TABLE IF NOT EXISTS clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, email TEXT, telefone TEXT)"
            self.cursor.execute(query)
            query = "INSERT INTO clientes (nome, email, telefone) VALUES ('"+str(nome)+"', '"+str(email)+"', '"+str(telefone)+"')"
            self.cursor.execute(query)
            self.connection.commit()
            print("[model] salvou no model!")
        except sqlite3.Error as erro:
            print("[model] Algo deu errado: ", erro)

    def recuperar(self):
        try:
            print("[model] recuperando...")
            query = "SELECT * FROM clientes"
            res = self.cursor.execute("SELECT * FROM clientes")
            print("[model] dados recuperados!")
            return res.fetchall()
        except sqlite3.Error as erro:
            print("[model] Algo deu errado: ", erro)


