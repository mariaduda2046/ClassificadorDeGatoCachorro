# logging_config.py
import logging
import os
from config import LOG_DIR, LOG_FILE_NAME

def setup_logging(level=logging.INFO):
    """
    Configura o sistema de logging para a aplicação.
    Logs serão salvos em um arquivo e também exibidos no console.
    """
    os.makedirs(LOG_DIR, exist_ok=True) # Garante que a pasta de logs existe
    log_path = os.path.join(LOG_DIR, LOG_FILE_NAME)

    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_path), # Salva logs em arquivo
            logging.StreamHandler()        # Exibe logs no console
        ]
    )
    # Opcional: configurar loggers específicos para suprimir mensagens de bibliotecas
    logging.getLogger('PIL').setLevel(logging.WARNING)
    logging.getLogger('matplotlib').setLevel(logging.WARNING) # Se fosse usar matplotlib