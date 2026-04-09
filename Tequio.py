import os
import shutil
import subprocess
import ctypes
import tkinter as tk
from tkinter import ttk
import threading
import time
import stat
import psutil

# ==========================
# 🔐 ADMIN
# ==========================
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if not is_admin():
    ctypes.windll.shell32.ShellExecuteW(None, "runas", "python", __file__, None, 1)
    exit()

# ==========================
# 🧠 USUARIO REAL (FIX)
# ==========================
def obtener_usuario_real():
    try:
        for proc in psutil.process_iter(['name', 'username']):
            if proc.info['name'] == 'explorer.exe':
                username = proc.info['username']
                if username:
                    return username.split("\\")[-1]
    except:
        pass
    return os.environ.get("USERNAME")

def ruta_usuario():
    return os.path.join("C:\\Users", obtener_usuario_real())

# ==========================
# 📊 CONTADOR
# ==========================
total_items = 0
procesados = 0

# ==========================
# UI HELPERS
# ==========================
def set_progress(value):
    root.after(0, lambda: progress.set(value))

def log(msg):
    root.after(0, lambda: (log_box.insert(tk.END, msg + "\n"), log_box.see(tk.END)))

def set_status(msg):
    root.after(0, lambda: status.set(msg))

# ==========================
# 🔪 CERRAR PROCESOS
# ==========================
def cerrar_procesos():
    procesos = [
        "chrome.exe", "brave.exe", "msedge.exe",
        "opera.exe", "firefox.exe"
    ]
    for p in procesos:
        subprocess.call(f"taskkill /f /im {p} >nul 2>&1", shell=True)
    time.sleep(1)

# ==========================
# 🔒 BORRADO REAL (FIX)
# ==========================
def borrar_contenido(rutas):
    global procesados
    procesados = 0

    for ruta in rutas:
        if not os.path.exists(ruta):
            continue

        for root_dir, dirs, files in os.walk(ruta, topdown=False):
            for name in files:
                path = os.path.join(root_dir, name)
                try:
                    os.chmod(path, stat.S_IWRITE)
                    os.remove(path)
                except:
                    pass
                procesados += 1
                actualizar_ui()

            for name in dirs:
                path = os.path.join(root_dir, name)
                try:
                    shutil.rmtree(path, ignore_errors=True)
                except:
                    pass
                procesados += 1
                actualizar_ui()

    set_progress(100)

# ==========================
# 📊 UI
# ==========================
def actualizar_ui():
    set_status(f"{procesados} archivos eliminados")

# ==========================
# 🧹 LIMPIEZA
# ==========================
def limpiar_carpetas():
    cerrar_procesos()
    user = ruta_usuario()

    rutas = [
        "Downloads","Documents","Pictures","Music","Videos",
        "Descargas","Documentos","Imágenes","Música","Videos"
    ]

    rutas_full = [os.path.join(user, r) for r in rutas]

    rutas_full += [
        os.path.join(user, "OneDrive", "Desktop"),
        os.path.join(user, "OneDrive", "Documents"),
        os.path.join(user, "OneDrive", "Pictures"),
    ]

    borrar_contenido(rutas_full)
    log("✔ Carpetas limpiadas")

def limpiar_escritorio():
    user = ruta_usuario()

    rutas = [
        os.path.join(user, "Desktop"),
        os.path.join(user, "Escritorio"),
        os.path.join(user, "OneDrive", "Desktop")
    ]

    borrar_contenido(rutas)
    log("✔ Escritorio limpio")

def limpiar_temp():
    cerrar_procesos()
    user = ruta_usuario()

    rutas = [
        os.path.join(user, "AppData", "Local", "Temp"),
        os.path.join(user, "AppData", "Local", "Microsoft", "Windows", "INetCache"),
        os.path.join(user, "AppData", "Local", "CrashDumps"),
        "C:\\Windows\\Temp"
    ]

    borrar_contenido(rutas)
    log("✔ Temp limpiado")

def limpiar_navegadores():
    cerrar_procesos()
    user = ruta_usuario()

    rutas = [
        os.path.join(user,"AppData","Local","Google","Chrome","User Data","Default","Cache"),
        os.path.join(user,"AppData","Local","Microsoft","Edge","User Data","Default","Cache"),
        os.path.join(user,"AppData","Local","BraveSoftware","Brave-Browser","User Data","Default","Cache"),
        os.path.join(user,"AppData","Local","Mozilla","Firefox","Profiles"),
    ]

    borrar_contenido(rutas)
    log("✔ Navegadores limpiados")

# ==========================
# 🗑 PAPELERA (FIX REAL)
# ==========================
def vaciar_papelera():
    log("🗑 Vaciando papelera...")

    try:
        subprocess.run("powershell -Command Clear-RecycleBin -Force", shell=True)
    except:
        pass

    try:
        subprocess.run("rd /s /q C:\\$Recycle.Bin", shell=True)
    except:
        pass

    log("✔ Papelera vaciada")

# ==========================
# 🌐 NAVEGADOR DEFAULT
# ==========================
def abrir_url(url):
    subprocess.Popen(f'start "" "{url}"', shell=True)

# ==========================
# 🚀 TEST
# ==========================
def test():
    urls = [
        "https://www.onlinemictest.com/es/prueba-de-teclado/",
        "https://www.speedtest.net/es",
        "https://prepaenlinea.sep.gob.mx/",
        "https://www.youtube.com/watch?v=tRTidhrmoxE"
    ]

    for url in urls:
        abrir_url(url)
        time.sleep(2)

# ==========================
# THREAD
# ==========================
def run_task(func):
    def wrapper():
        set_progress(0)
        set_status("Ejecutando...")
        func()
        set_status("✔ Completado")
    threading.Thread(target=wrapper).start()

# ==========================
# UI
# ==========================
root = tk.Tk()
root.title("LIMPIEZA COMPUTADORAS")
root.geometry("650x900")
root.configure(bg="#020617")

tk.Label(root, text="LIMPIEZA COMPUTADORAS",
         font=("Segoe UI", 24, "bold"),
         fg="#ff0000", bg="#020617").pack(pady=15)

frame = tk.Frame(root, bg="#020617")
frame.pack()

def btn(texto, cmd, color):
    return tk.Button(frame, text=texto, bg=color,
                     fg="white", width=35, height=2,
                     command=lambda: run_task(cmd))

btn("💀 LIMPIEZA TOTAL", limpiar_carpetas, "#ef4444").pack(pady=8)
btn("🧹 Carpetas", limpiar_carpetas, "#22c55e").pack(pady=5)
btn("⚙ TEMP", limpiar_temp, "#f59e0b").pack(pady=5)
btn("🖥 Escritorio", limpiar_escritorio, "#3b82f6").pack(pady=5)
btn("🌐 Navegadores", limpiar_navegadores, "#0ea5e9").pack(pady=5)
btn("🗑 Papelera", vaciar_papelera, "#8b5cf6").pack(pady=5)
btn("🚀 TEST", test, "#14b8a6").pack(pady=10)

progress = tk.IntVar()
ttk.Progressbar(root, length=500, variable=progress).pack(pady=10)

status = tk.StringVar(value="Esperando...")
tk.Label(root, textvariable=status, fg="#94a3b8", bg="#020617").pack()

log_box = tk.Text(root, height=15, bg="#020617", fg="#22c55e")
log_box.pack(padx=10, pady=10, fill="both")

root.mainloop()