# gui.py
import customtkinter as ctk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os
import logging
from model_inference import ImagePredictor
from config import MODEL_PATH, GUI_ICON_PATH, WINDOW_TITLE, WINDOW_GEOMETRY, GUI_THEME, IMAGE_SIZE, CLASS_NAMES

logger = logging.getLogger(__name__)

class ImageClassifierApp(ctk.CTk): # Herda de CTk
    def __init__(self, master=None):
        super().__init__()
        
        self.title(WINDOW_TITLE)
        self.geometry(WINDOW_GEOMETRY)
        ctk.set_default_color_theme(GUI_THEME) # Define o tema
        ctk.set_appearance_mode("dark") # Ou "light" ou "system"

        self.predictor = ImagePredictor(MODEL_PATH)
        self.current_image_path = None # Para armazenar o caminho da última imagem selecionada
        
        self.load_icon()
        self._create_widgets()
        
        if self.predictor.model is None:
            messagebox.showerror("Erro de Carregamento", "Não foi possível carregar o modelo de classificação. A aplicação pode não funcionar corretamente.")
            self.predict_button.configure(state="disabled") # Desabilita o botão
            logger.error("Falha ao carregar o modelo no início da aplicação.")

    def load_icon(self):
        """Carrega e define o ícone da janela."""
        try:
            if os.path.exists(GUI_ICON_PATH):
                # CustomTkinter usa set_icon_photo ou set_icon_bitmap
                # Dependendo do sistema, set_icon_photo com PIL pode ser mais universal
                icon_image = Image.open(GUI_ICON_PATH)
                self.iconphoto(True, ImageTk.PhotoImage(icon_image))
            else:
                logger.warning(f"Ícone não encontrado em: {GUI_ICON_PATH}")
        except Exception as e:
            logger.error(f"Erro ao carregar ícone: {e}")

    def _create_widgets(self):
        """Cria e organiza os widgets da interface."""
        # Frame principal para organização
        main_frame = ctk.CTkFrame(self, fg_color="transparent")
        main_frame.pack(pady=20, padx=20, fill="both", expand=True)

        # Título
        title_label = ctk.CTkLabel(main_frame, text="Classificador de Imagem", 
                                   font=ctk.CTkFont(size=24, weight="bold"))
        title_label.pack(pady=(0, 20))

        # Texto de instrução
        instruction_label = ctk.CTkLabel(main_frame, text="Selecione uma imagem para prever:", 
                                         font=ctk.CTkFont(size=16))
        instruction_label.pack(pady=10)

        # Botão para escolher imagem
        choose_image_button = ctk.CTkButton(main_frame, text="Escolher Imagem", 
                                            command=self._choose_image,
                                            font=ctk.CTkFont(size=16, weight="bold"),
                                            height=40,
                                            corner_radius=8)
        choose_image_button.pack(pady=10)

        # Label para exibir a imagem
        self.image_display_label = ctk.CTkLabel(main_frame, text="", bg_color="transparent")
        self.image_display_label.pack(pady=10)

        # Botão de previsão (separado para controle)
        self.predict_button = ctk.CTkButton(main_frame, text="Prever", 
                                            command=self._perform_prediction,
                                            font=ctk.CTkFont(size=16, weight="bold"),
                                            height=40,
                                            fg_color="green", hover_color="darkgreen",
                                            state="disabled", # Desabilitado por padrão até uma imagem ser escolhida
                                            corner_radius=8)
        self.predict_button.pack(pady=10)

        # Separador visual
        separator = ctk.CTkFrame(main_frame, height=2, fg_color="gray", corner_radius=1)
        separator.pack(fill="x", padx=20, pady=20)

        # Label para o resultado da previsão
        self.result_label = ctk.CTkLabel(main_frame, text="", 
                                          font=ctk.CTkFont(size=18, weight="bold"))
        self.result_label.pack(pady=10)

        # Barra de progresso (para confiança)
        self.confidence_progressbar = ctk.CTkProgressBar(main_frame, orientation="horizontal", 
                                                         width=300, height=15, corner_radius=8)
        self.confidence_progressbar.set(0) # Inicia em 0
        self.confidence_progressbar.pack(pady=10)

        # Botão de sair
        exit_button = ctk.CTkButton(main_frame, text="Sair", 
                                    command=self.quit,
                                    font=ctk.CTkFont(size=16, weight="bold"),
                                    height=40,
                                    fg_color="red", hover_color="darkred",
                                    corner_radius=8)
        exit_button.pack(pady=20)

    def _choose_image(self):
        """Abre a caixa de diálogo para seleção de imagem e a exibe."""
        self.current_image_path = filedialog.askopenfilename(
            title="Selecione uma imagem",
            filetypes=[("Arquivos de imagem", "*.jpg *.jpeg *.png *.bmp")]
        )
        if self.current_image_path:
            logger.info(f"Imagem selecionada: {self.current_image_path}")
            try:
                img = Image.open(self.current_image_path)
                img.thumbnail((300, 300)) # Redimensiona para exibição
                img_tk = ImageTk.PhotoImage(img)
                self.image_display_label.configure(image=img_tk, text="")
                self.image_display_label.image = img_tk # Mantém referência para evitar garbage collection
                self.predict_button.configure(state="normal") # Habilita o botão de previsão
                self.result_label.configure(text="") # Limpa resultado anterior
                self.confidence_progressbar.set(0) # Reseta barra
            except Exception as e:
                messagebox.showerror("Erro ao Abrir Imagem", f"Não foi possível abrir a imagem: {e}")
                logger.error(f"Erro ao abrir imagem {self.current_image_path}: {e}")
                self.image_display_label.configure(image=None, text="Erro ao carregar imagem")
                self.predict_button.configure(state="disabled")
        else:
            logger.info("Seleção de imagem cancelada.")
            self.predict_button.configure(state="disabled") # Garante que está desabilitado se não escolheu

    def _perform_prediction(self):
        """Realiza a previsão da imagem selecionada."""
        if self.current_image_path:
            logger.info(f"Realizando previsão para: {self.current_image_path}")
            # Desabilita o botão enquanto processa para evitar cliques múltiplos
            self.predict_button.configure(state="disabled", text="Prevendo...")
            
            # Aqui, para operações mais longas, você usaria threading para evitar congelamento
            # Por simplicidade, faremos diretamente para este exemplo com SVM
            classe, confianca = self.predictor.predict_image(self.current_image_path)
            
            self.predict_button.configure(state="normal", text="Prever") # Reabilita

            if "Erro" in classe:
                self.result_label.configure(text=f"Erro: {classe}", text_color="red")
                self.confidence_progressbar.set(0)
                logger.error(f"Erro na previsão: {classe}")
            else:
                self.result_label.configure(text=f"{classe}\n({confianca:.2%} de certeza)", text_color="white")
                self.confidence_progressbar.set(confianca) # Atualiza a barra
                logger.info(f"Previsão: {classe} com {confianca:.2%} de certeza.")
        else:
            messagebox.showwarning("Nenhuma Imagem", "Por favor, selecione uma imagem primeiro.")
            logger.warning("Tentativa de previsão sem imagem selecionada.")