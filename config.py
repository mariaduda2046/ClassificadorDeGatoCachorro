# config.py
import os

# Caminho base do projeto (o diretório onde este arquivo está)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# --- Configurações de Paths ---
DATASET_DIR = os.path.join(BASE_DIR, 'dataset')
MODEL_FILENAME = 'modelo_sklearn_gato_cachorro.joblib'
MODEL_PATH = os.path.join(BASE_DIR, 'assets', MODEL_FILENAME)
GUI_ICON_PATH = os.path.join(BASE_DIR, 'assets', 'gato.ico')
LOG_DIR = os.path.join(BASE_DIR, 'logs')
LOG_FILE_NAME = 'app.log'

# --- Configurações do Modelo e Dados ---
IMAGE_SIZE = (64, 64)
CLASS_NAMES = ['Gato', 'Cachorro'] # Para exibição na GUI
CLASS_LABELS = ['gato', 'cachorro'] # Para nomes de pastas do dataset e treinamento

# --- Configurações de Treinamento ---
TEST_SIZE = 0.2
RANDOM_STATE = 42

# --- Configurações da GUI ---
WINDOW_TITLE = "Gatinho ou Cachorrinho? - Classificador de Imagem"
WINDOW_GEOMETRY = "500x750"

# Cores e temas (CustomTkinter)
# https://customtkinter.tomsons.icu/documentation/utility/set_default_color_theme
# Você pode escolher entre "blue", "dark-blue", "green"
GUI_THEME = "dark-blue"