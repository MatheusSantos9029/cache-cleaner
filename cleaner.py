import os
import shutil
import tkinter as tk
from tkinter import ttk
import threading

def limpar_pasta(caminho, log):
    deletados = 0
    espaco = 0

    if not os.path.exists(caminho):
        log(f"⚠️  Pasta não encontrada: {caminho}\n")
        return deletados, espaco

    for item in os.listdir(caminho):
        item_path = os.path.join(caminho, item)
        try:
            tamanho = os.path.getsize(item_path)
            if os.path.isfile(item_path):
                os.remove(item_path)
                deletados += 1
                espaco += tamanho
            elif os.path.isdir(item_path):
                espaco += tamanho
                shutil.rmtree(item_path)
                deletados += 1
        except Exception:
            pass

    return deletados, espaco


def iniciar_limpeza():
    selecionadas = [caminho for caminho, var in opcoes if var.get()]

    if not selecionadas:
        area_texto.config(state="normal")
        area_texto.delete("1.0", tk.END)
        area_texto.insert(tk.END, "⚠️  Selecione ao menos uma pasta para limpar.\n")
        area_texto.config(state="disabled")
        return

    botao.config(state="disabled")
    area_texto.config(state="normal")
    area_texto.delete("1.0", tk.END)
    barra["value"] = 0

    def executar():
        total_deletados = 0
        total_espaco = 0

        def log(msg):
            area_texto.insert(tk.END, msg)
            area_texto.see(tk.END)

        log("🧹 Iniciando limpeza...\n\n")

        for i, pasta in enumerate(selecionadas):
            log(f"📂 Limpando: {pasta}\n")
            deletados, espaco = limpar_pasta(pasta, log)
            total_deletados += deletados
            total_espaco += espaco
            log(f"   ✅ {deletados} itens removidos — {espaco / (1024*1024):.2f} MB liberados\n\n")
            barra["value"] = ((i + 1) / len(selecionadas)) * 100
            janela.update_idletasks()

        log("─────────────────────────────────\n")
        log(f"Total: {total_deletados} itens removidos\n")
        log(f"Espaço liberado: {total_espaco / (1024*1024):.2f} MB\n")
        log("─────────────────────────────────\n")

        area_texto.config(state="disabled")
        botao.config(state="normal")

    thread = threading.Thread(target=executar)
    thread.start()


# Interface
localappdata = os.environ.get("LOCALAPPDATA") or os.path.expandvars("%LOCALAPPDATA%")

janela = tk.Tk()
janela.title("Cache Cleaner")
janela.geometry("500x540")
janela.resizable(False, False)

titulo = tk.Label(janela, text="🧹 Cache Cleaner", font=("Helvetica", 16, "bold"))
titulo.pack(pady=10)

# Checkboxes
frame_opcoes = tk.LabelFrame(janela, text="Selecione o que limpar", padx=10, pady=8)
frame_opcoes.pack(padx=20, fill="x")

opcoes_definidas = [
    ("Temp do usuário", os.environ.get("TEMP")),
    ("Temp do Windows", r"C:\Windows\Temp"),
    ("Cache do Chrome", os.path.join(localappdata, r"Google\Chrome\User Data\Default\Cache\Cache_Data")),
    ("Code Cache JS", os.path.join(localappdata, r"Google\Chrome\User Data\Default\Code Cache\js")),
    ("Code Cache WASM", os.path.join(localappdata, r"Google\Chrome\User Data\Default\Code Cache\wasm")),
]

opcoes = []
for label, caminho in opcoes_definidas:
    var = tk.BooleanVar(value=False)  # nenhuma pré-selecionada
    cb = tk.Checkbutton(frame_opcoes, text=label, variable=var, anchor="w")
    cb.pack(fill="x")
    opcoes.append((caminho, var))

def selecionar_todos():
    todos_marcados = all(var.get() for _, var in opcoes)
    for _, var in opcoes:
        var.set(not todos_marcados)
    btn_todos.config(text="Desmarcar todos" if not todos_marcados else "Selecionar todos")

btn_todos = tk.Button(frame_opcoes, text="Selecionar todos", command=selecionar_todos,
                      font=("Helvetica", 9), bg="#3498db", fg="white", padx=8, pady=3)
btn_todos.pack(anchor="w", pady=5)

botao = tk.Button(janela, text="Limpar Cache", font=("Helvetica", 12),
                  bg="#e74c3c", fg="white", padx=20, pady=8, command=iniciar_limpeza)
botao.pack(pady=10)

barra = ttk.Progressbar(janela, length=440, mode="determinate")
barra.pack(pady=5)

area_texto = tk.Text(janela, height=12, width=60, font=("Courier", 9),
                     state="disabled", bg="#1e1e1e", fg="#d4d4d4")
area_texto.pack(padx=20, pady=5)

janela.mainloop()