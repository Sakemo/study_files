# Exercicio 1

# - Gabriel é o cliente de uma livraria online que acaba
# de comprar 01 livro com o título lógica de programação por R$79,30
# o vendedor Marcos recebeu uma comissão de R$30,00 pela venda.

# "Olá, (Gabriel) sua compra de (01) qtd do livro 
# (lógica de programação) por R$(79,30) foi efetuada com sucesso!".
# "Olá, (Marcos) você acaba de receber uma comissão de R$(30,00) 
# pela compra realizada pelo(a) cliente (Gabriel)".

import tkinter as tk

def get_name():
    comprador = name_entry.get()
    login.destroy()
    livros = [
        ("Logica de Programação", 79.30), 
        ("Senhor dos Anéis", 59.99),
        ("Harry Potter e a Pedra Filosofal", 39.90),
        ("O Pequeno Príncipe", 29.99),
        ("A Culpa é das Estrelas", 49.90),
        ("1984", 34.50),
        ("O Hobbit", 44.99),
        ("O Código Da Vinci", 54.80),
        ("A Menina que Roubava Livros", 27.99),
        ("O Nome do Vento", 64.00),
        ("A Dança dos Dragões", 89.90),
        ("O Festim dos Corvos", 79.90),
        ("Anne de Green Gables", 23.99)
        ]

    vendedor = "Marcos"

    root = tk.Tk()
    root.title(f'Loja de Livros do {vendedor}')
    root.geometry("300x600")

    label = tk.Label(root, text=f"Loja de Livros do {vendedor}")
    label.pack()
    table = tk.Frame(root)
    table.pack()

    def select_row(row):
        global selected_row
        selected_row = row
        print(selected_row)
        for i,(livro,preco) in enumerate(livros):
            if selected_row == i:
                comissao = (preco*0.3)
                mesage = tk.Tk()
                mesage.title('Sucesso')
                mesage.geometry('500x50')
                print_label = tk.Label(mesage, text=f'Olá {comprador}! Sua compra do livro {livro} por R${preco} foi efetuada com sucesso')
                print_label.pack(pady=5)
                print(f"Olá {vendedor}! Você recebeu sua comissão de R${comissao} pela compra do cliente {comprador} do livro {livro} por R${preco}")

    for i,(livro, preco) in enumerate(livros):
        tk.Label(table, text=livro).grid(row=i, column=0)
        tk.Label(table, text=f"R$ {preco:.2f}").grid(row=i, column=1)
        tk.Button(table, text="Comprar", command=lambda row=i: select_row(row)).grid(row=i, column=2, padx=5, pady=10)

login = tk.Tk()
login.geometry('150x100')
login.title('Login')
name_label = tk.Label(login, text='Insira seu nome:')
name_label.pack(pady=5)
name_entry = tk.Entry(login)
name_entry.pack()
button = tk.Button(login, text='Login', command=get_name)
button.pack(pady=5)

login.mainloop()
