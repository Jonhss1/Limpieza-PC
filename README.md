# Limpieza-PC-Jonathan-Perez-Trujillo  
![image alt](https://github.com/Jonhss1/Limpieza-PC/blob/6dddcd4783be9fe9141b3a55bb4f39ceaa7666d2/Programa.png)
✨ Características  
🔐 Elevación automática a Administrador  
🧠 Detección del usuario real del sistema  
🧹 Limpieza de:  
-Carpetas personales (Descargas, Documentos, Imágenes, etc.)  
-Escritorio  
-Archivos temporales del sistema  
-Caché de navegadores  
🗑 Vaciado completo de la papelera  
🌐 Test automático (internet, teclado, etc.)  
📊 Barra de progreso en tiempo real  
🧾 Logs en vivo dentro de la app  
⚡ Ejecución en hilos (no bloquea la interfaz)  

🖥 Requisitos  
- Windows 10 / 11  
- Python 3.8 o superior  
- Dependencias  
- pip install psutil

 🚀 Instalación  
 - git clone https://github.com/Jonhss1/Limpieza-PC.git
 - cd Limpieza-PC
 - pip install psutil
 - python main.py 

▶️ Uso

Ejecuta el script:

- python main.py  
 
 El programa solicitará permisos de administrador automáticamente. Usa la interfaz gráfica:  
 
💀 LIMPIEZA TOTAL	= Limpieza completa  
🧹 Carpetas	= Limpia documentos y descargas  
⚙ TEMP	= Borra archivos temporales  
🖥 Escritorio	= Limpia el escritorio  
🌐 Navegadores	= Limpia caché  
🗑 Papelera	= Vacía la papelera  
🚀 TEST	= Abre páginas de prueba  

🧠 Cómo funciona  
ctypes → Elevación a administrador  
psutil → Obtiene el usuario real  
os / shutil → Eliminación de archivos  
subprocess → Comandos del sistema  
threading → Ejecución en paralelo  
tkinter → Interfaz gráfica  

⚠️ Advertencia

🚨 Este programa elimina archivos de forma permanente

No hay confirmación antes de borrar
No utiliza la papelera
Puede eliminar datos importantes

!!! Úsalo bajo tu propia responsabilidad.!!!  
 
📄 Licencia

MIT License

⭐ Soporte

Si te gusta el proyecto, dale una estrella ⭐ en GitHub.
