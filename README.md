# 🧹 Cache Cleaner

> *"São pequenos passos que nos fazem trilhar grandes caminhos."*

## 🇧🇷 Português

### Sobre o projeto

Script Python com interface gráfica para limpeza automática de arquivos temporários e cache do Windows. O usuário escolhe quais pastas deseja limpar, confirma a ação e acompanha o resultado em tempo real — incluindo o total de itens removidos e o espaço liberado.

Este projeto foi desenvolvido como parte do meu aprendizado prático em Python, com foco em interface gráfica, manipulação de arquivos e integração com o sistema operacional Windows.

### Funcionalidades

- ☑️ Seleção individual das pastas a limpar via checkboxes
- 🔘 Botão "Selecionar todos" / "Desmarcar todos"
- ⚠️ Confirmação antes de iniciar a limpeza
- 🔒 Solicitação automática de permissão de administrador para pastas protegidas
- 📊 Barra de progresso em tempo real
- 📋 Aba com resumo da última limpeza (data, itens removidos e espaço liberado)

### Pastas suportadas

| Pasta | Requer Admin |
|---|---|
| Temp do usuário (`%TEMP%`) | Não |
| Temp do Windows (`C:\Windows\Temp`) | Não |
| Cache do Chrome | Não |
| Code Cache JS (Chrome) | Não |
| Code Cache WASM (Chrome) | Não |
| Arquivos Recentes | Não |
| Prefetch (`C:\Windows\Prefetch`) | ✅ Sim |
| Windows Update (`SoftwareDistribution\Download`) | ✅ Sim |

### Tecnologias utilizadas

- Python 3.12
- `tkinter` (interface gráfica — nativa do Python)
- `shutil` e `os` (manipulação de arquivos)
- `ctypes` (permissão de administrador)
- `threading` (execução sem travar a interface)

### Pré-requisitos

- Python 3.10 ou superior
- Windows 10 ou superior

### Como usar

**1. Clone o repositório**
```bash
git clone https://github.com/MatheusSantos9029/cache-cleaner.git
cd cache-cleaner
```

**2. Execute o script**
```bash
python cleaner.py
```

**3. Selecione as pastas desejadas, confirme e aguarde o resultado.**

> Para limpar pastas marcadas com **[Admin]**, o programa solicitará automaticamente permissão de administrador.

### Estrutura do projeto

```
cache-cleaner/
│
├── cleaner.py     # Script principal com interface gráfica
└── .gitignore     # Arquivos ignorados pelo Git
```

---

## 🇺🇸 English

### About

A Python script with a graphical interface for automatically cleaning temporary files and cache on Windows. The user selects which folders to clean, confirms the action, and tracks the results in real time — including total items removed and space freed.

This project was developed as part of my hands-on Python learning, focusing on GUI development, file manipulation, and Windows OS integration.

### Features

- ☑️ Individual folder selection via checkboxes
- 🔘 "Select all" / "Deselect all" button
- ⚠️ Confirmation dialog before cleaning
- 🔒 Automatic administrator permission request for protected folders
- 📊 Real-time progress bar
- 📋 Tab showing last cleanup summary (date, items removed, space freed)

### Supported folders

| Folder | Requires Admin |
|---|---|
| User Temp (`%TEMP%`) | No |
| Windows Temp (`C:\Windows\Temp`) | No |
| Chrome Cache | No |
| Chrome JS Code Cache | No |
| Chrome WASM Code Cache | No |
| Recent Files | No |
| Prefetch (`C:\Windows\Prefetch`) | ✅ Yes |
| Windows Update (`SoftwareDistribution\Download`) | ✅ Yes |

### Technologies

- Python 3.12
- `tkinter` (GUI — built into Python)
- `shutil` and `os` (file manipulation)
- `ctypes` (admin permission)
- `threading` (non-blocking execution)

### Requirements

- Python 3.10 or higher
- Windows 10 or higher

### How to use

**1. Clone the repository**
```bash
git clone https://github.com/MatheusSantos9029/cache-cleaner.git
cd cache-cleaner
```

**2. Run the script**
```bash
python cleaner.py
```

**3. Select the folders you want to clean, confirm, and wait for the results.**

> For folders marked **[Admin]**, the program will automatically request administrator privileges.

### Project structure

```
cache-cleaner/
│
├── cleaner.py     # Main script with graphical interface
└── .gitignore     # Git ignored files
```

---

*Developed by [Matheus Santos](https://github.com/MatheusSantos9029)*
