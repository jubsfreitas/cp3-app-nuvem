from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return """
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Inova Trônica | Azure Cloud</title>

        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }

            body {
                font-family: Arial, Helvetica, sans-serif;
                min-height: 100vh;
                background: linear-gradient(135deg, #0f172a, #123c69, #1769aa);
                color: white;
                display: flex;
                justify-content: center;
                align-items: center;
                padding: 30px;
            }

            .container {
                width: 100%;
                max-width: 950px;
                background: rgba(255, 255, 255, 0.08);
                border: 1px solid rgba(255, 255, 255, 0.18);
                border-radius: 28px;
                padding: 50px;
                backdrop-filter: blur(15px);
                box-shadow: 0 25px 70px rgba(0, 0, 0, 0.35);
            }

            .topo {
                display: flex;
                justify-content: space-between;
                align-items: center;
                margin-bottom: 55px;
            }

            .logo {
                font-size: 24px;
                font-weight: bold;
            }

            .status {
                background: rgba(34, 197, 94, 0.15);
                border: 1px solid rgba(74, 222, 128, 0.4);
                color: #86efac;
                padding: 9px 16px;
                border-radius: 30px;
                font-size: 14px;
            }

            .hero {
                text-align: center;
            }

            .icone {
                font-size: 55px;
                margin-bottom: 20px;
            }

            h1 {
                font-size: 48px;
                margin-bottom: 18px;
            }

            .destaque {
                color: #60a5fa;
            }

            .descricao {
                color: #dbeafe;
                font-size: 18px;
                line-height: 1.7;
                max-width: 700px;
                margin: 0 auto 40px;
            }

            .cards {
                display: grid;
                grid-template-columns: repeat(3, 1fr);
                gap: 18px;
                margin-top: 45px;
            }

            .card {
                background: rgba(255, 255, 255, 0.09);
                border: 1px solid rgba(255, 255, 255, 0.12);
                border-radius: 18px;
                padding: 25px;
                text-align: center;
                transition: transform 0.2s;
            }

            .card:hover {
                transform: translateY(-5px);
            }

            .card-icon {
                font-size: 30px;
                margin-bottom: 14px;
            }

            .card h3 {
                margin-bottom: 8px;
            }

            .card p {
                color: #bfdbfe;
                font-size: 14px;
                line-height: 1.5;
            }

            .info {
                margin-top: 35px;
                padding-top: 25px;
                border-top: 1px solid rgba(255, 255, 255, 0.12);
                text-align: center;
                color: #bfdbfe;
                font-size: 14px;
            }

            .info strong {
                color: white;
            }

            .rodape {
                text-align: center;
                margin-top: 35px;
                color: #93c5fd;
                font-size: 13px;
            }

            @media (max-width: 700px) {
                .container {
                    padding: 30px 20px;
                }

                h1 {
                    font-size: 34px;
                }

                .topo {
                    margin-bottom: 35px;
                }

                .cards {
                    grid-template-columns: 1fr;
                }
            }
        </style>
    </head>

    <body>

        <div class="container">

            <div class="topo">
                <div class="logo">⚡ Inova Trônica</div>
                <div class="status">● Aplicação online</div>
            </div>

            <div class="hero">

                <div class="icone">☁️</div>

                <h1>
                    Deploy realizado
                    <span class="destaque">com sucesso!</span>
                </h1>

                <p class="descricao">
                    Esta aplicação foi provisionada e publicada automaticamente
                    na nuvem utilizando Microsoft Azure e Azure CLI.
                </p>

            </div>

            <div class="cards">

                <div class="card">
                    <div class="card-icon">☁️</div>
                    <h3>Azure App Service</h3>
                    <p>
                        Aplicação hospedada na nuvem através do
                        Serviço de Aplicativo do Azure.
                    </p>
                </div>

                <div class="card">
                    <div class="card-icon">⚙️</div>
                    <h3>Azure CLI</h3>
                    <p>
                        Recursos provisionados e configurados
                        automaticamente por script.
                    </p>
                </div>

                <div class="card">
                    <div class="card-icon">🐍</div>
                    <h3>Python + Flask</h3>
                    <p>
                        Aplicação web desenvolvida em Python
                        utilizando o framework Flask.
                    </p>
                </div>

            </div>

            <div class="info">
                <strong>RM96253</strong>
                &nbsp; • &nbsp;
                Linux F1
                &nbsp; • &nbsp;
                Microsoft Azure
            </div>

            <div class="rodape">
                FIAP • Aplicativos em Nuvem • CP3
            </div>

        </div>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

