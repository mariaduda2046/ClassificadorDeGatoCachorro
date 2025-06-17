🐾 Classificador de Imagens: Gatinho ou Cachorrinho?
Um aplicativo desktop simples e divertido construído com Python (Tkinter/CustomTkinter) e Scikit-learn para classificar imagens como "Gato" ou "Cachorro". Este projeto demonstra a modularização de um pipeline de Machine Learning (treinamento e inferência) e uma interface gráfica de usuário amigável.
✨ Funcionalidades
Classificação de Imagens: Preveja se uma imagem contém um gato ou um cachorro.
Modelo de Machine Learning: Utiliza um modelo SVM (Support Vector Machine) treinado com Scikit-learn.
Interface Gráfica Intuitiva: Desenvolvida com CustomTkinter para uma experiência de usuário moderna e agradável.
Modularização: Código organizado em módulos lógicos para fácil manutenção e escalabilidade.
Sistema de Logs: Registro detalhado de operações e erros para depuração.
🚀 Como Usar
Siga os passos abaixo para configurar e executar o projeto em sua máquina.
Pré-requisitos
Certifique-se de ter o Python 3.x instalado. As bibliotecas necessárias serão instaladas via pip.
1. Clonar o Repositório (ou Baixar o Projeto)
git clone <URL_DO_SEU_REPOSITORIO>
cd seu_projeto


Se você baixou os arquivos manualmente, certifique-se de que a estrutura de pastas esteja como a descrita abaixo.
2. Estrutura do Projeto
Certifique-se de que seu projeto tem a seguinte estrutura de pastas e arquivos:
seu_projeto/
├── main.py                     # Ponto de entrada da aplicação GUI
├── gui.py                      # Lógica da interface gráfica (CustomTkinter)
├── model_inference.py          # Lógica para carregar o modelo e fazer previsões
├── model_training.py           # Lógica para carregar dados, treinar e salvar o modelo
├── config.py                   # Arquivo de configuração global
├── logging_config.py           # Configurações do sistema de log
├── assets/
│   ├── gato.ico                # Ícone da aplicação (necessário)
│   └── modelo_sklearn_gato_cachorro.joblib # O modelo treinado será salvo aqui
├── dataset/                    # Sua pasta com as imagens de treino
│   ├── gato/                   # Imagens de gatos
│   │   └── imagem_gato_1.jpg
│   │   └── ...
│   └── cachorro/               # Imagens de cachorros
│       └── imagem_cachorro_1.png
│       └── ...
└── logs/                       # Pasta para armazenar os arquivos de log (criada automaticamente)
    └── app.log


3. Criar e Ativar um Ambiente Virtual (Recomendado)
python -m venv venv
# No Windows:
.\venv\Scripts\activate
# No macOS/Linux:
source venv/bin/activate


4. Instalar as Dependências
Com o ambiente virtual ativado, instale as bibliotecas necessárias:
pip install numpy pillow scikit-learn joblib customtkinter


5. Preparar o Dataset
Crie as pastas dataset/gato e dataset/cachorro dentro do diretório seu_projeto/dataset/.
Coloque suas imagens de gatos na pasta gato/ e imagens de cachorros na pasta cachorro/. Certifique-se de ter um número razoável de imagens em ambas as categorias para um bom treinamento.
6. Treinar o Modelo
O modelo SVM precisa ser treinado antes de ser usado pela interface.
Execute o script de treinamento:
python model_training.py


Este script irá:
Carregar e pré-processar as imagens do dataset/.
Dividir os dados em conjuntos de treino e teste.
Treinar um modelo SVM.
Imprimir um relatório de classificação no console.
Salvar o modelo treinado em assets/modelo_sklearn_gato_cachorro.joblib.
Você também verá mensagens de log no terminal e no arquivo logs/app.log.
7. Executar a Aplicação GUI
Após o treinamento bem-sucedido e o salvamento do modelo, você pode iniciar a interface:
python main.py


A janela do aplicativo será aberta. Clique em "Escolher Imagem", selecione uma imagem de gato ou cachorro e veja a previsão!
🛠️ Tecnologias Utilizadas
Python 3.x
Scikit-learn: Para o algoritmo de Machine Learning (SVM).
Pillow (PIL): Para manipulação e pré-processamento de imagens.
NumPy: Para operações numéricas e arrays de dados.
CustomTkinter: Para a criação da interface gráfica moderna e responsiva.
Joblib: Para serializar e deserializar o modelo treinado.
📁 Estrutura de Módulos
O projeto é modularizado da seguinte forma:
main.py: Ponto de entrada principal da aplicação GUI.
gui.py: Contém a classe principal da interface gráfica (ImageClassifierApp), gerenciando os widgets e as interações do usuário.
model_inference.py: Abstrai a lógica de carregamento do modelo e realização de previsões em novas imagens.
model_training.py: Contém a lógica completa para o pipeline de treinamento do modelo, desde o carregamento dos dados até a avaliação e salvamento.
config.py: Centraliza todas as configurações e parâmetros do projeto (caminhos, tamanhos, nomes de classes, etc.).
logging_config.py: Configura o sistema de log da aplicação para melhor depuração e monitoramento.
📈 Melhorias Futuras (Ideias)
Integração de Modelos Mais Complexos: Suporte a modelos de Deep Learning (ex: TensorFlow/Keras) para maior precisão.
Multi-threading: Executar a previsão em uma thread separada para manter a GUI responsiva durante operações demoradas.
Configurações de Hiperparâmetros: Interface para ajustar os hiperparâmetros do modelo.
Feedback de Treinamento: Adicionar uma barra de progresso visual para o processo de treinamento (se este fosse integrado à GUI).
Galeria de Imagens: Uma funcionalidade para navegar por várias imagens do dataset ou resultados de previsões.
🤝 Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.
📄 Licença
Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
