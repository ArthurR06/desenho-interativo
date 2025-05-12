import tkinter as tk
from tkinter import messagebox
from turtle import RawTurtle, ScrolledCanvas

# ===========================
# PROGRAMA DE DESENHO INTERATIVO INTEGRADO COM TKINTER E TURTLE
# ===========================
# Permite ao usuário desenhar formas geométricas com cor personalizada em uma interface única.
# Utiliza integração entre Tkinter (GUI) e Turtle (desenho) com visual moderno e feedback ao usuário.

# --------------------------
# Variáveis globais de controle
# --------------------------
forma_selecionada = None
cor_selecionada = None
botoes_forma = {}
botoes_cor = {}

# Mapeia o nome em português da cor com o nome reconhecido pelo Turtle
cores_map = {
    "Vermelho": "red",
    "Azul": "blue",
    "Verde": "green",
    "Amarelo": "yellow"
}

# --------------------------
# Função principal de desenho
# --------------------------
def desenhar():
    if not forma_selecionada or not cor_selecionada:
        messagebox.showwarning("Aviso", "Selecione uma forma e uma cor antes de desenhar.")
        return

    turtle.clear()
    turtle.reset()
    turtle.hideturtle()
    turtle.speed(1)
    turtle.pensize(5)  # Define a espessura do contorno (ex: 5 pixels)

    turtle.color(cores_map[cor_selecionada])
    turtle.fillcolor(cores_map[cor_selecionada])
    turtle.penup()

    turtle.begin_fill()
    if forma_selecionada == "Quadrado":
        turtle.goto(-100, 100)
        turtle.pendown()
        for _ in range(4):
            turtle.forward(200)
            turtle.right(90)

    elif forma_selecionada == "Triângulo":
        turtle.goto(-100, -50)
        turtle.pendown()
        for _ in range(3):
            turtle.forward(200)
            turtle.left(120)

    elif forma_selecionada == "Círculo":
        turtle.goto(0, -100)
        turtle.pendown()
        turtle.circle(100)
    turtle.end_fill()
    turtle.penup()

# --------------------------
# Função para limpar o canvas
# --------------------------
def limpar_desenho():
    global forma_selecionada, cor_selecionada

    # Limpa o canvas
    turtle.clear()
    turtle.reset()
    turtle.hideturtle()

    # Reseta seleções
    forma_selecionada = None
    cor_selecionada = None

    # Volta todos os botões para o estado inicial
    for btn in botoes_forma.values():
        btn.config(relief="raised", bg="SystemButtonFace")
    for cor, btn in botoes_cor.items():
        btn.config(relief="raised", bg=cores_map[cor])

    # Atualiza o status na interface
    atualizar_status()


# --------------------------
# Funções de seleção com feedback visual
# --------------------------
def selecionar_forma(forma):
    global forma_selecionada
    forma_selecionada = forma
    for f, btn in botoes_forma.items():
        btn.config(
            relief="sunken" if f == forma else "raised",
            bg="lightblue" if f == forma else "SystemButtonFace"
        )
    atualizar_status()

def selecionar_cor(cor):
    global cor_selecionada
    cor_selecionada = cor
    for c, btn in botoes_cor.items():
        btn.config(
            relief="sunken" if c == cor else "raised",
            bg=cores_map[c] if c == cor else "SystemButtonFace"
        )
    atualizar_status()

# --------------------------
# Interface Gráfica com Tkinter
# --------------------------
janela = tk.Tk()
janela.title("Atividade de Computação Gráfica: Desenho Interativo")
janela.geometry("800x600")
janela.resizable(False, False)

# Título do projeto
tk.Label(janela, text="Programa de Desenho Interativo", font=("Arial", 14, "bold")).pack(pady=10)

# --------------------------
# Seção de seleção de formas geométricas
# --------------------------
tk.Label(janela, text="Escolha uma forma:", font=("Arial", 11)).pack()
frame_formas = tk.Frame(janela)
frame_formas.pack(pady=5)

formas = [
    ("Quadrado", "■"),
    ("Triângulo", "▲"),
    ("Círculo", "●")
]
for nome, simbolo in formas:
    btn = tk.Button(
        frame_formas,
        text=f"{simbolo} {nome}",
        width=14,
        command=lambda f=nome: selecionar_forma(f)
    )
    btn.pack(side="left", padx=5)
    botoes_forma[nome] = btn

# --------------------------
# Seção de seleção de cores
# --------------------------
tk.Label(janela, text="Escolha uma cor:", font=("Arial", 11)).pack(pady=10)
frame_cores = tk.Frame(janela)
frame_cores.pack()
for cor in cores_map:
    btn = tk.Button(
        frame_cores,
        text=cor,
        width=14,
        bg=cores_map[cor],
        command=lambda c=cor: selecionar_cor(c)
    )
    btn.pack(side="left", padx=5)
    botoes_cor[cor] = btn

# --------------------------
# Status da seleção atual
# --------------------------
def atualizar_status():
    texto = "Selecionado: "
    if forma_selecionada:
        texto += forma_selecionada
    if cor_selecionada:
        texto += f" {cor_selecionada}"
    label_status.config(text=texto)

label_status = tk.Label(janela, text="Selecionado: ", font=("Arial", 10, "italic"))
label_status.pack(pady=5)

# --------------------------
# Botões de ação (Desenhar e Limpar)
# --------------------------
frame_acoes = tk.Frame(janela)
frame_acoes.pack(pady=20)

tk.Button(frame_acoes, text="Desenhar", font=("Arial", 12), command=desenhar).pack(side="left", padx=10)
tk.Button(frame_acoes, text="Limpar", font=("Arial", 12), command=limpar_desenho).pack(side="left", padx=10)

# --------------------------
# Área de desenho (canvas Turtle embutido)
# --------------------------
canvas = ScrolledCanvas(janela, width=780, height=300)
canvas.pack(padx=10, pady=10)
canvas.config(bg="#D3D3D3")  # Define o fundo do canvas como cinza claro

turtle = RawTurtle(canvas)
turtle.hideturtle()
turtle.speed(0)

# Inicia o loop principal da interface
tk.mainloop()
