# main.py
import logging
import logging_config
import customtkinter as ctk
from gui import ImageClassifierApp

if __name__ == "__main__":
    # Configura o sistema de logging
    logging_config.setup_logging()
    logger = logging.getLogger(__name__)

    logger.info("Iniciando a aplicação Gatinho ou Cachorrinho?")

    # Cria a janela principal da aplicação usando CustomTkinter
    app = ImageClassifierApp()
    app.mainloop() # Inicia o loop principal da GUI

    logger.info("Aplicação encerrada.")