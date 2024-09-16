from db_connection import connect

class Pedido:
    def __init__(self, cliente, prato, quantidade):
        self.cliente = cliente
        self.prato = prato
        self.quantidade = quantidade

    def salvar(self):
        conn = connect()
        if conn is not None:
            cur = conn.cursor()
            cur.execute("""
                INSERT INTO pedidos (cliente, prato, quantidade)
                VALUES (%s, %s, %s)
            """, (self.cliente, self.prato, self.quantidade))
            conn.commit()
            cur.close()
            conn.close()
            print("Pedido salvo com sucesso!")