# Integrated Project

Este projeto integra modelos de visão computacional e processamento de linguagem natural para análise e inferência em imagens.

# Estrutura do Projeto

integration.py: Script principal para executar o pipeline de integração.
test_images/: Pasta contendo imagens de teste para validação do modelo.
README.md: Documentação do projeto.

# Objetivo

O objetivo deste projeto é demonstrar a integração de modelos multimodais para realizar inferência sobre imagens, incluindo processamento visual e geração de respostas.

# Requisitos

Python 3.8+
PyTorch
Transformers
Outras dependências listadas em requirements.txt

# Instalação

Clone este repositório:
git clone https://github.com/gp-debora/IS_Project.git
cd IS_Project/integrated_project
Recomenda-se criar um ambiente virtual e instalar as dependências:
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate  # Windows

pip install -r requirements.txt

# Uso

Para executar o pipeline de integração, rode:

python integration.py --image-path test_images/seu_arquivo.jpg --query "Sua pergunta sobre a imagem"
Altere --image-path para o caminho da imagem desejada e --query para a pergunta que deseja realizar.

# Estrutura do Código

O script principal carrega a imagem e realiza a inferência combinando os modelos multimodais.
Os resultados são processados e exibidos no terminal (ou salvos em arquivo, dependendo da implementação).

# Contribuições

Contribuições são bem-vindas! Por favor, abra um issue ou pull request para sugerir melhorias ou corrigir problemas.


## Instruções para Configuração do Projeto IS_Project

Este projeto inclui dois submódulos principais, Groma e JiuTian-LION, que contêm as implementações centrais. Para garantir o correto funcionamento e evitar o upload de ficheiros pesados, estes submódulos estão organizados como repositórios Git separados dentro do repositório principal.

### Clonagem do Repositório

Para clonar o projeto corretamente com todos os submódulos, utilize o seguinte comando:

git clone --recurse-submodules https://github.com/gp-debora/IS_Project.git
Se já clonou o repositório sem os submódulos, execute:

git submodule update --init --recursive

### Configuração do Ambiente

Crie um ambiente virtual Python (recomendado):
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
Instale as dependências do projeto:
pip install -r requirements.txt

### Configuração do VSCode

No VSCode, a configuração já inclui as pastas Groma e JiuTian-LION/ram como caminhos adicionais para o Python, evitando erros de importação.

### Executar

Agora pode executar os scripts de cada módulo normalmente, com as dependências instaladas e submódulos carregados.


