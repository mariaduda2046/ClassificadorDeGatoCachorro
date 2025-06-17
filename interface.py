import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from PIL import Image, ImageTk
import numpy as np
import joblib

model = joblib.load('modelo_sklearn_gato_cachorro.joblib')

def prever_imagem(caminho_imagem):
    image_size = (64, 64)
    class_names = ['Gato', 'Cachorro']

    img = Image.open(caminho_imagem).convert('RGB')
    img = img.resize(image_size)
    img_array = np.array(img).flatten().reshape(1, -1)

    proba = model.predict_proba(img_array)[0]
    indice = np.argmax(proba)
    classe = class_names[indice]
    confianca = proba[indice]

    return classe, confianca

def escolher_imagem():
    caminho = filedialog.askopenfilename(
        title="Selecione uma imagem",
        filetypes=[("Arquivos de imagem", "*.jpg *.jpeg *.png *.bmp")]
    )
    if caminho:
        img = Image.open(caminho)
        img.thumbnail((300, 300))
        img_tk = ImageTk.PhotoImage(img)
        label_imagem.config(image=img_tk)
        label_imagem.image = img_tk

        classe, confianca = prever_imagem(caminho)
        label_resultado.config(
            text=f"{classe}\n({confianca:.2%} de certeza)"
        )

        # Atualiza barra de progresso
        barra_progresso['value'] = confianca * 100

janela = tk.Tk()
janela.title("Gatinho ou Cachorrinho?")
janela.geometry("500x750")
janela.configure(bg="#0d1b2a")

# Adicionar ícone
try:
    janela.iconbitmap('gato.ico')  # Substitua pelo seu ícone
except:
    print("Ícone não encontrado. Ignorando...")

# Título
titulo = tk.Label(janela, text="Classificador de Imagem", 
                  font=("Arial", 22, "bold"), 
                  bg="#0d1b2a", fg="#ffffff")
titulo.pack(pady=20)

# Separador
sep = tk.Frame(janela, bg="#ffffff", height=2, width=300)
sep.pack(pady=10)

# Texto acima do botão
texto_instrucao = tk.Label(janela, text="Escolha a foto da sua feiurinha:", 
                           font=("Arial", 14), 
                           bg="#0d1b2a", fg="#cccccc")
texto_instrucao.pack(pady=10)

# Botão estilizado
def on_enter(e):
    btn_escolher['background'] = '#42a5f5'
def on_leave(e):
    btn_escolher['background'] = '#2196F3'

btn_escolher = tk.Button(janela, text="Escolher Imagem", 
                         command=escolher_imagem, 
                         font=("Arial", 14, "bold"),
                         bg="#2196F3", fg="white", 
                         activebackground="#1976D2",
                         relief="flat", padx=20, pady=10,
                         bd=0, highlightthickness=0)
btn_escolher.pack(pady=10)

btn_escolher.bind("<Enter>", on_enter)
btn_escolher.bind("<Leave>", on_leave)

# Label para imagem
label_imagem = tk.Label(janela, bg="#0d1b2a")
label_imagem.pack(pady=10)

# Label para resultado
label_resultado = tk.Label(janela, text="", 
                           font=("Arial", 16, "bold"), 
                           bg="#0d1b2a", fg="#ffffff")
label_resultado.pack(pady=20)

# Barra de progresso
barra_progresso = ttk.Progressbar(janela, orient='horizontal',
                                  length=300, mode='determinate')
barra_progresso.pack(pady=10)

# Botão de sair com hover
def on_enter_exit(e):
    btn_sair['background'] = '#ef5350'
def on_leave_exit(e):
    btn_sair['background'] = '#e53935'

btn_sair = tk.Button(janela, text="Sair", 
                     command=janela.quit, 
                     font=("Arial", 14, "bold"),
                     bg="#e53935", fg="white",
                     activebackground="#c62828",
                     relief="flat", padx=20, pady=10,
                     bd=0, highlightthickness=0)
btn_sair.pack(pady=20)

btn_sair.bind("<Enter>", on_enter_exit)
btn_sair.bind("<Leave>", on_leave_exit)

# Rodar
janela.mainloop()