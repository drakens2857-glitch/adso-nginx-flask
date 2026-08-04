from flask import Flask, request, render_template, redirect
import mysql.connector


sample = Flask(__name__)


def conectar():
    return mysql.connector.connect(
        host="servidor-bd",
        user="root",
        password="123456",
        database="adso_db"
    )


@sample.route("/")
def main():

    db = conectar()
    cursor = db.cursor(dictionary=True)

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


@sample.route("/registrar", methods=["POST"])
def registrar():

    nombre = request.form["nombre"]
    documento = request.form["documento"]
    ficha = request.form["ficha"]


    db = conectar()
    cursor = db.cursor()


    cursor.execute("""
        INSERT INTO aprendices
        (nombre_completo, numero_documento, ficha)
        VALUES (%s, %s, %s)
    """,
    (
        nombre,
        documento,
        ficha
    ))


    db.commit()

    cursor.close()
    db.close()


    return redirect("/")


if __name__ == "__main__":
    sample.run(
        host="0.0.0.0",
        port=5050,
        debug=True
    )
