from db_connection import connect

class Estoque:
    def __init__(self, produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade

    def atualizar_estoque(self, quantidade_usada):
        conn = connect()
        if conn is not None:
            cur = conn.cursor()
            cur.execute("""
                UPDATE estoque
                SET quantidade = quantidade - %s
                WHERE produto = %s
            """, (quantidade_usada, self.produto))
            conn.commit()
            cur.close()
            conn.close()
            print(f"Estoque atualizado para o produto {self.produto}.")