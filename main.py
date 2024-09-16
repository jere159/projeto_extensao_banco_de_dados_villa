import tkinter as tk
from models.pedido import Pedido
from models.estoque import Estoque

def realizar_pedido():
    cliente = entry_cliente.get()
    prato = entry_prato.get()
    quantidade = int(entry_quantidade.get())

    # Criar um novo pedido e salvar no banco
    novo_pedido = Pedido(cliente, prato, quantidade)
    novo_pedido.salvar()

    # Atualizar o estoque
    estoque = Estoque(prato, quantidade)
    estoque.atualizar_estoque(quantidade)

    label_status.config(text="Pedido realizado com sucesso!")

# Interface Gráfica usando Tkinter
root = tk.Tk()
root.title("Sistema de Pedidos - Villa das Massas")

tk.Label(root, text="Cliente:").grid(row=0, column=0)
entry_cliente = tk.Entry(root)
entry_cliente.grid(row=0, column=1)

tk.Label(root, text="Prato:").grid(row=1, column=0)
entry_prato = tk.Entry(root)
entry_prato.grid(row=1, column=1)

tk.Label(root, text="Quantidade:").grid(row=2, column=0)
entry_quantidade = tk.Entry(root)
entry_quantidade.grid(row=2, column=1)

btn_pedido = tk.Button(root, text="Realizar Pedido", command=realizar_pedido)
btn_pedido.grid(row=3, column=0, columnspan=2)

label_status = tk.Label(root, text="")
label_status.grid(row=4, column=0, columnspan=2)

root.mainloop()