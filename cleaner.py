import os
import shutil

def limpar_pasta(caminho):
    deletados = 0
    espaco = 0

    if not os.path.exists(caminho):
        print(f"⚠️  Pasta não encontrada: {caminho}")
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
        except Exception as e:
            print(f"⚠️  Não foi possível deletar {item}: {e}")

    return deletados, espaco


pastas = [
    os.environ.get("TEMP"),
    r"C:\Windows\Temp"
]

total_deletados = 0
total_espaco = 0

print("\n🧹 Iniciando limpeza de cache...\n")

for pasta in pastas:
    print(f"📂 Limpando: {pasta}")
    deletados, espaco = limpar_pasta(pasta)
    total_deletados += deletados
    total_espaco += espaco
    print(f"   ✅ {deletados} itens removidos — {espaco / (1024*1024):.2f} MB liberados\n")

print("─────────────────────────────────")
print(f"Total: {total_deletados} itens removidos")
print(f"Espaço liberado: {total_espaco / (1024*1024):.2f} MB")
print("─────────────────────────────────\n")