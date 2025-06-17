# model_training.py
import os
import numpy as np
from PIL import Image
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report
import joblib
import logging
from config import IMAGE_SIZE, DATASET_DIR, MODEL_PATH, TEST_SIZE, RANDOM_STATE, CLASS_LABELS, CLASS_NAMES

logger = logging.getLogger(__name__)

class ImageClassifierTrainer:
    def __init__(self):
        self.image_size = IMAGE_SIZE
        self.dataset_dir = DATASET_DIR
        self.model_output_path = MODEL_PATH
        self.class_labels = CLASS_LABELS # Nomes das pastas no dataset
        self.class_names_for_report = CLASS_NAMES # Nomes para o relatório de classificação

    def load_and_preprocess_data(self):
        """Carrega e pré-processa as imagens do dataset."""
        X = []
        y = []

        logger.info(f"Iniciando carregamento de dados do diretório: {self.dataset_dir}")
        
        if not os.path.isdir(self.dataset_dir):
            logger.error(f"Diretório do dataset não encontrado: {self.dataset_dir}")
            return None, None

        for label, class_name in enumerate(self.class_labels):
            class_dir = os.path.join(self.dataset_dir, class_name)
            if not os.path.isdir(class_dir):
                logger.warning(f"Diretório da classe '{class_name}' não encontrado: {class_dir}. Pulando.")
                continue

            for file in os.listdir(class_dir):
                img_path = os.path.join(class_dir, file)
                try:
                    img = Image.open(img_path).convert('RGB')
                    img = img.resize(self.image_size)
                    img_array = np.array(img).flatten()
                    X.append(img_array)
                    y.append(label)
                except Exception as e:
                    logger.error(f"Erro ao processar imagem {img_path}: {e}")
        
        if not X:
            logger.error("Nenhuma imagem carregada. Verifique o caminho do dataset e as permissões.")
            return None, None

        logger.info(f"Dados carregados: {len(X)} imagens encontradas.")
        return np.array(X), np.array(y)

    def train_model(self, X_train, y_train):
        """Treina o modelo SVM."""
        logger.info("Iniciando treinamento do modelo SVC...")
        model = SVC(probability=True, random_state=RANDOM_STATE)
        try:
            model.fit(X_train, y_train)
            logger.info("Treinamento do modelo concluído com sucesso.")
            return model
        except Exception as e:
            logger.error(f"Erro durante o treinamento do modelo: {e}")
            return None

    def evaluate_model(self, model, X_test, y_test):
        """Avalia o modelo e imprime o relatório de classificação."""
        if model is None:
            logger.warning("Não é possível avaliar o modelo: modelo é None.")
            return None
        
        logger.info("Avaliando o modelo...")
        try:
            y_pred = model.predict(X_test)
            report = classification_report(y_test, y_pred, target_names=self.class_names_for_report)
            logger.info(f"\nRelatório de Classificação:\n{report}")
            return report
        except Exception as e:
            logger.error(f"Erro durante a avaliação do modelo: {e}")
            return None

    def save_model(self, model):
        """Salva o modelo treinado em um arquivo."""
        if model is None:
            logger.warning("Não é possível salvar o modelo: modelo é None.")
            return

        os.makedirs(os.path.dirname(self.model_output_path), exist_ok=True)
        try:
            joblib.dump(model, self.model_output_path)
            logger.info(f"Modelo salvo com sucesso em: {self.model_output_path}")
        except Exception as e:
            logger.error(f"Erro ao salvar o modelo em {self.model_output_path}: {e}")

    def run_training_pipeline(self):
        """Executa todo o pipeline de treinamento."""
        logger.info("Iniciando pipeline de treinamento do classificador de imagens.")
        X, y = self.load_and_preprocess_data()
        
        if X is None or y is None:
            logger.error("Não foi possível carregar os dados para o treinamento. Abortando.")
            return

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=TEST_SIZE, random_state=RANDOM_STATE)
        logger.info(f"Dados divididos: Treino={len(X_train)} amostras, Teste={len(X_test)} amostras.")

        model = self.train_model(X_train, y_train)
        if model:
            self.evaluate_model(model, X_test, y_test)
            self.save_model(model)
        else:
            logger.error("Treinamento falhou, modelo não foi salvo.")

# Para executar o treinamento diretamente a partir deste arquivo
if __name__ == "__main__":
    from logging_config import setup_logging
    setup_logging()
    
    trainer = ImageClassifierTrainer()
    trainer.run_training_pipeline()