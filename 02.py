import tkinter as tk

janela = tk.Tk()

var_promocoes = tk.IntVar()
checkbox_promocoes = tk.Checkbutton(text='Deseja receber e-mail promocional?', variable = var_promocoes)
checkbox_promocoes.grid(row=0,column=0)

var_politicas = tk.IntVar()
checkbox_politicas = tk.Checkbutton(text='Aceitar termos de uso e Politicas de Privacidade',variable=var_politicas)
checkbox_politicas.grid(row=1,column=0)

def enviar():
    if var_promocoes.get():
        print('Usuário deseja receber promoções')
    else:
        print('Usuário NÂO deseja receber promoções')
    if var_politicas.get():
        print('Usuário concordou com Termos de Uso e Politicas de Privacidade')
    else:
        print('Usuário NÂO concordou')


botao_enviar = tk.Button (text='Enviar', command=enviar)
botao_enviar.grid(row=2,column=0)

janela.mainloop()