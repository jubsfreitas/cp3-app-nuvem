from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return """
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <title>Inova Trônica</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: #f2f5fa;
                text-align: center;
                padding-top: 100px;
            }

            .container {
                background: white;
                max-width: 700px;
                margin: auto;
                padding: 50px;
                border-radius: 16px;
                box-shadow: 0 5px 20px #0001;
            }

            h1 {
                color: #1769aa;
            }
        </style>
    </head>

    <body>
        <div class="container">
            <h1>Inova Trônica</h1>
            <h2>Aplicação implantada no Azure</h2>
            <p>Serviço de Aplicativo criado automaticamente por Azure CLI.</p>
            <p>Deploy realizado com sucesso!</p>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
