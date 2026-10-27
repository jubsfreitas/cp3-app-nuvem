# CP3 - Aplicação Web no Azure

## Integrantes

- RM96253 - Anna Júlia de Freitas Machado

## Objetivo

Desenvolver um processo automatizado de implantação de uma aplicação web na nuvem utilizando o Microsoft Azure e Azure CLI.

O projeto foi desenvolvido seguindo a proposta do CP3 da disciplina, utilizando um script para provisionar os recursos necessários e realizar o deploy da aplicação sem depender de configurações manuais pelo Portal do Azure.

## Tecnologias utilizadas

- Microsoft Azure
- Azure CLI
- Azure App Service
- Linux
- Python
- Flask
- Gunicorn
- Git e GitHub

## Recursos provisionados

Os recursos foram criados automaticamente pelo script `deploy.sh`.

| Recurso | Nome |
|---|---|
| Resource Group | `rg-web-app` |
| App Service Plan | `plan-web-app` |
| Serviço de Aplicativo | `web-app-RM96253` |
| Sistema operacional | Linux |
| Plano | F1 |
| Região | East US |

## Aplicação

A aplicação foi desenvolvida em Flask e possui uma página web simples para demonstrar que o deploy foi realizado com sucesso.

A aplicação está disponível publicamente em:

https://web-app-RM96253.azurewebsites.net

## Deploy automatizado

O arquivo `deploy.sh` realiza automaticamente as seguintes etapas:

1. Criação do Resource Group;
2. Criação do App Service Plan;
3. Criação do Serviço de Aplicativo;
4. Configuração das dependências da aplicação;
5. Configuração da inicialização com Gunicorn;
6. Criação do pacote da aplicação;
7. Deploy da aplicação no Azure.

Para executar o processo novamente, utilize:

```bash
chmod +x deploy.sh
./deploy.sh

