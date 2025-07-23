#Integrated Project

Este projeto integra modelos de visão computacional e processamento de linguagem natural para análise e inferência em imagens.

#Estrutura do Projeto

integration.py: Script principal para executar o pipeline de integração.
test_images/: Pasta contendo imagens de teste para validação do modelo.
README.md: Documentação do projeto.

#Objetivo

O objetivo deste projeto é demonstrar a integração de modelos multimodais para realizar inferência sobre imagens, incluindo processamento visual e geração de respostas.

#Requisitos

Python 3.8+
PyTorch
Transformers
Outras dependências listadas em requirements.txt

#Instalação

Clone este repositório:
git clone https://github.com/gp-debora/IS_Project.git
cd IS_Project/integrated_project
Recomenda-se criar um ambiente virtual e instalar as dependências:
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate  # Windows

pip install -r requirements.txt

#Uso

Para executar o pipeline de integração, rode:

python integration.py --image-path test_images/seu_arquivo.jpg --query "Sua pergunta sobre a imagem"
Altere --image-path para o caminho da imagem desejada e --query para a pergunta que deseja realizar.

#Estrutura do Código

O script principal carrega a imagem e realiza a inferência combinando os modelos multimodais.
Os resultados são processados e exibidos no terminal (ou salvos em arquivo, dependendo da implementação).

#Contribuições

Contribuições são bem-vindas! Por favor, abra um issue ou pull request para sugerir melhorias ou corrigir problemas.


