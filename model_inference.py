# model_inference.py
import joblib
import numpy as np
from PIL import Image
import os
import logging
from config import IMAGE_SIZE, CLASS_NAMES

logger = logging.getLogger(__name__)

class ImagePredictor:
    def __init__(self, model_path):
        self.model = None # Inicializa o modelo como None
        self.image_size = IMAGE_SIZE
        self.class_names = CLASS_NAMES
        
        self._load_model(model_path)

    def _load_model(self, model_path):
        """Tenta carregar o modelo treinado."""
        logger.info(f"Tentando carregar modelo do arquivo: {model_path}")
        if not os.path.exists(model_path):
            logger.error(f"Erro: Arquivo do modelo não encontrado: {model_path}")
            return

        try:
            self.model = joblib.load(model_path)
            logger.info("Modelo carregado com sucesso.")
        except Exception as e:
            logger.error(f"Erro ao carregar o modelo de {model_path}: {e}", exc_info=True)

    def preprocess_image(self, image_path):
        """Pré-processa uma única imagem para a previsão."""
        try:
            img = Image.open(image_path).convert('RGB')
            img = img.resize(self.image_size)
            img_array = np.array(img).flatten().reshape(1, -1)
            return img_array
        except FileNotFoundError:
            logger.error(f"Erro: Imagem não encontrada no caminho: {image_path}")
            return None
        except Exception as e:
            logger.error(f"Erro ao pré-processar a imagem {image_path}: {e}", exc_info=True)
            return None

    def predict_image(self, image_path):
        """Realiza a previsão em uma imagem."""
        if self.model is None:
            logger.warning("Erro: Modelo não carregado. Não é possível fazer a previsão.")
            return "Erro: Modelo não carregado", 0.0

        img_array = self.preprocess_image(image_path)
        if img_array is None:
            return "Erro: Falha ao processar imagem", 0.0

        try:
            proba = self.model.predict_proba(img_array)[0]
            indice = np.argmax(proba)
            classe = self.class_names[indice]
            confianca = proba[indice]
            return classe, confianca
        except Exception as e:
            logger.error(f"Erro durante a previsão da imagem {image_path}: {e}", exc_info=True)
            return "Erro na previsão", 0.0