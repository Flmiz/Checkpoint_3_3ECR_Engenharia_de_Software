from models.cliente_model import Cliente_model

class Cliente_controller():
    def __init__(self):
        print("[controller] chamando controller")
        self.cliente = Cliente_model()

    def salvar(self, nome, email, telefone):
        print("[controller] chamando salvar() do controller")
        if nome is not None and email is not None and telefone is not None:
            self.cliente.salvar(nome, email, telefone)
            print("[controller] controller ok, saindo do controller...")

    def recuperar(self):
        print("[controller] chamando recuperar() do controller")
        res = self.cliente.recuperar()
        print("[controller] controller ok, saindo do controller...")
        return res
