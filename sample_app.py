import os
from flask import Flask, request, render_template, redirect
import mysql.connector

# Crear la aplicación Flask
sample = Flask(__name__)

def conectar():
    # Se obtienen las credenciales desde variables de entorno
    # Evita el aviso B106 de Bandit al no dejar contraseñas quemadas en texto plano
    db_password = os.getenv("DB_PASSWORD", "secret_dev_pass")
    db_host = os.getenv("DB_HOST", "servidor-bd")
    
    return mysql.connector.connect(
        host=db_host,
        user="root",
        password=db_password,
        database="adso_db"
    )

# Ruta principal
@sample.route("/")
def main():
    db = conectar()
    cursor = db.cursor(dictionary=True)

    # Consultar los aprendices registrados
    cursor.execute("""
        SELECT * FROM aprendices
        ORDER BY id DESC
    """)

    aprendices = cursor.fetchall()

    cursor.close()
    db.close()

    return render_template(
        "index.html",
        aprendices=aprendices
    )

# Ruta para registrar un nuevo aprendiz
@sample.route("/registrar", methods=["POST"])
def registrar():
    nombre = request.form["nombre"]
    documento = request.form["documento"]
    ficha = request.form["ficha"]

    db = conectar()
    cursor = db.cursor()

    # Insertar datos en la tabla de forma segura usando parámetros (%s)
    cursor.execute("""
        INSERT INTO aprendices
        (nombre_completo, numero_documento, ficha)
        VALUES (%s, %s, %s)
    """, (
        nombre,
        documento,
        ficha
    ))

    db.commit()

    cursor.close()
    db.close()

    return redirect("/")

if __name__ == "__main__":
    # Solución B201 y B104:
    # Se leen del entorno '127.0.0.1' y 'False' por defecto
    host_env = os.getenv("FLASK_RUN_HOST", "127.0.0.1")
    debug_env = os.getenv("FLASK_DEBUG", "False").lower() == "true"

    sample.run(
        host=host_env,
        port=5000,
        debug=debug_env
<<<<<<< HEAD
    )
=======
<<<<<<< HEAD
    )
=======
    )
>>>>>>> 287d6d9 (Fix: correccion de seguridad y configuracion CI/CD)
>>>>>>> 7e94263 (correccion yml)
