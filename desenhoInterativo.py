import tkinter as tk
from tkinter import messagebox
from turtle import RawTurtle, ScrolledCanvas
import random

# ===========================
# PROGRAMA DE DESENHO INTERATIVO COM TKINTER + TURTLE
# ===========================

# --------------------------
# Variáveis globais
# --------------------------
forma_selecionada = None
cor_selecionada = None
botoes_forma = {}
botoes_cor = {}

cores_map = {
    "Vermelho": "red",
    "Azul": "blue",
    "Verde": "green",
    "Amarelo": "yellow"
}

# --------------------------
# Função de desenho
# --------------------------
def desenhar():
    if not forma_selecionada or not cor_selecionada:
        messagebox.showwarning("Aviso", "Selecione uma forma e uma cor antes de desenhar.")
        return

    tamanho = scale_tamanho.get()
    turtle.clear()
    turtle.reset()
    turtle.hideturtle()
    turtle.speed(1)
    turtle.pensize(5)
    turtle.color(cores_map[cor_selecionada])
    turtle.fillcolor(cores_map[cor_selecionada])
    turtle.penup()
    turtle.begin_fill()

    if forma_selecionada == "Quadrado":
        turtle.goto(-tamanho//2, tamanho//2)
        turtle.pendown()
        for _ in range(4):
            turtle.forward(tamanho)
            turtle.right(90)

    elif forma_selecionada == "Triângulo":
        turtle.goto(-tamanho//2, -tamanho//3)
        turtle.pendown()
        for _ in range(3):
            turtle.forward(tamanho)
            turtle.left(120)

    elif forma_selecionada == "Círculo":
        turtle.goto(0, -tamanho//2)
        turtle.pendown()
        turtle.circle(tamanho // 2)

    turtle.end_fill()
    turtle.penup()

# --------------------------
# Função "Desenho Surpresa"
# --------------------------
def desenho_surpresa():
    forma = random.choice(["Quadrado", "Triângulo", "Círculo"])
    cor = random.choice(list(cores_map.keys()))
    tamanho = random.randint(10, 250)
    selecionar_forma(forma)
    selecionar_cor(cor)
    scale_tamanho.set(tamanho)
    desenhar()

# --------------------------
# Função de limpar
# --------------------------
def limpar_desenho():
    global forma_selecionada, cor_selecionada
    turtle.clear()
    turtle.reset()
    turtle.hideturtle()
    forma_selecionada = None
    cor_selecionada = None
    for btn in botoes_forma.values():
        btn.config(relief="raised", bg="SystemButtonFace")
    for cor, btn in botoes_cor.items():
        btn.config(relief="raised", bg=cores_map[cor])
    atualizar_status()

# --------------------------
# Seleções e feedback
# --------------------------
def selecionar_forma(forma):
    global forma_selecionada
    forma_selecionada = forma
    for f, btn in botoes_forma.items():
        btn.config(relief="sunken" if f == forma else "raised",
                   bg="lightblue" if f == forma else "SystemButtonFace")
    atualizar_status()

def selecionar_cor(cor):
    global cor_selecionada
    cor_selecionada = cor
    for c, btn in botoes_cor.items():
        btn.config(relief="sunken" if c == cor else "raised",
                   bg=cores_map[c] if c == cor else "SystemButtonFace")
    atualizar_status()

def atualizar_status():
    texto = "Selecionado: "
    if forma_selecionada:
        texto += forma_selecionada
    if cor_selecionada:
        texto += f" {cor_selecionada}"
    label_status.config(text=texto)

# --------------------------
# Interface com Tkinter
# --------------------------
janela = tk.Tk()
janela.title("Atividade de Computação Gráfica: Desenho Interativo")
janela.geometry("820x680")
janela.resizable(False, False)

tk.Label(janela, text="Programa de Desenho Interativo", font=("Arial", 14, "bold")).pack(pady=10)

# Formas
tk.Label(janela, text="Escolha uma forma:", font=("Arial", 11)).pack()
frame_formas = tk.Frame(janela)
frame_formas.pack(pady=5)
formas = [("Quadrado", "■"), ("Triângulo", "▲"), ("Círculo", "●")]
for nome, simbolo in formas:
    btn = tk.Button(frame_formas, text=f"{simbolo} {nome}", width=14,
                    command=lambda f=nome: selecionar_forma(f))
    btn.pack(side="left", padx=5)
    botoes_forma[nome] = btn

# Cores
tk.Label(janela, text="Escolha uma cor:", font=("Arial", 11)).pack(pady=10)
frame_cores = tk.Frame(janela)
frame_cores.pack()
for cor in cores_map:
    btn = tk.Button(frame_cores, text=cor, width=14, bg=cores_map[cor],
                    command=lambda c=cor: selecionar_cor(c))
    btn.pack(side="left", padx=5)
    botoes_cor[cor] = btn

# Tamanho
tk.Label(janela, text="Tamanho do desenho:", font=("Arial", 11)).pack(pady=10)
scale_tamanho = tk.Scale(janela, from_=10, to=250, orient="horizontal", length=300)
scale_tamanho.set(150)
scale_tamanho.pack()

# Status
label_status = tk.Label(janela, text="Selecionado: ", font=("Arial", 10, "italic"))
label_status.pack(pady=5)

# Ações
frame_acoes = tk.Frame(janela)
frame_acoes.pack(pady=20)
tk.Button(frame_acoes, text="Desenhar", font=("Arial", 12), command=desenhar).pack(side="left", padx=10)
tk.Button(frame_acoes, text="Limpar", font=("Arial", 12), command=limpar_desenho).pack(side="left", padx=10)
tk.Button(frame_acoes, text="Surpresa", font=("Arial", 12), command=desenho_surpresa).pack(side="left", padx=10)

# Canvas
canvas = ScrolledCanvas(janela, width=780, height=300)
canvas.pack(padx=10, pady=10)
canvas.config(bg="#D3D3D3")
turtle = RawTurtle(canvas)
turtle.hideturtle()
turtle.speed(0)


# Loop principal
tk.mainloop()
