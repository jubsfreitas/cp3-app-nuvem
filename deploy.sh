#!/bin/bash

# ==========================================
# INOVA TRÔNICA - DEPLOY AZURE APP SERVICE
# RM96253
# ==========================================

RESOURCE_GROUP="rg-web-app"
LOCATION="eastus"
PLAN_NAME="plan-web-app"
APP_NAME="web-app-RM96253"
RUNTIME="PYTHON:3.12"

echo "=========================================="
echo " INOVA TRÔNICA - DEPLOY AUTOMATIZADO"
echo "=========================================="

echo ""
echo "1. Criando Resource Group..."
az group create \
  --name $RESOURCE_GROUP \
  --location $LOCATION

echo ""
echo "2. Criando App Service Plan..."
az appservice plan create \
  --name $PLAN_NAME \
  --resource-group $RESOURCE_GROUP \
  --location $LOCATION \
  --sku F1 \
  --is-linux

echo ""
echo "3. Criando Serviço de Aplicativo..."
az webapp create \
  --name $APP_NAME \
  --resource-group $RESOURCE_GROUP \
  --plan $PLAN_NAME \
  --runtime $RUNTIME

echo ""
echo "4. Criando aplicação Flask..."

cat > app.py <<'PY'
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
PY

echo ""
echo "5. Criando requirements.txt..."

cat > requirements.txt <<'EOF'
Flask
gunicorn
EOF

echo ""
echo "6. Habilitando instalação automática das dependências..."

az webapp config appsettings set \
  --resource-group $RESOURCE_GROUP \
  --name $APP_NAME \
  --settings SCM_DO_BUILD_DURING_DEPLOYMENT=true

echo ""
echo "7. Configurando inicialização da aplicação..."

az webapp config set \
  --resource-group $RESOURCE_GROUP \
  --name $APP_NAME \
  --startup-file "gunicorn --bind=0.0.0.0 --timeout 600 app:app"

echo ""
echo "8. Criando pacote da aplicação..."

zip -r app.zip app.py requirements.txt

echo ""
echo "9. Realizando deploy..."

az webapp deploy \
  --resource-group $RESOURCE_GROUP \
  --name $APP_NAME \
  --src-path app.zip \
  --type zip

echo ""
echo "=========================================="
echo " DEPLOY CONCLUÍDO!"
echo "=========================================="

APP_URL="https://$APP_NAME.azurewebsites.net"

echo ""
echo "Aplicação disponível em:"
echo "$APP_URL"
echo ""
