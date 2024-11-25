# 🚀 Minha Jornada de Aprendizado em Python

Bem-vindo ao meu repositório! Este espaço é dedicado ao registro da minha trajetória no aprendizado da linguagem Python. Aqui, compartilho exercícios, projetos, e anotações enquanto exploro o universo da programação.

---

## 📦 Configuração do Ambiente

Para facilitar o desenvolvimento, estou utilizando um container Docker configurado diretamente no [GitHub Codespaces](https://github.com/features/codespaces). O ambiente já inclui:

- Python configurado no container.
- Extensões do VS Code para Python.
- Dependências gerenciadas pelo arquivo `requirements.txt`.

### Como foi configurado o container:

O arquivo `.devcontainer/devcontainer.json` contém as configurações básicas do ambiente. Ele utiliza uma imagem base oficial do Python, garantindo que todas as ferramentas necessárias estejam disponíveis.

Exemplo do arquivo:

```json
{
  "name": "Python Codespace",
  "image": "mcr.microsoft.com/devcontainers/python:3.10",
  "customizations": {
    "vscode": {
      "extensions": [
        "ms-python.python",
        "ms-python.vscode-pylance"
      ]
    }
  },
  "postCreateCommand": "pip install -r requirements.txt"
}