import tkinter
from PIL import Image, ImageTk


image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "imgs")

imagemLogo          = ImageTk.PhotoImage(Image.open(os.path.join(image_path, "Logo.png")).resize((200,100), Image.Resampling.LANCZOS))
imagemConexao       = ImageTk.PhotoImage(Image.open(os.path.join(image_path, "Conexao.png")).resize((50,50), Image.Resampling.LANCZOS))
imagemTelemetria    = ImageTk.PhotoImage(Image.open(os.path.join(image_path, "Telemetria.png")).resize((50,50), Image.Resampling.LANCZOS))
imagemLog           = ImageTk.PhotoImage(Image.open(os.path.join(image_path, "Log.png")).resize((50,50), Image.Resampling.LANCZOS))
imagemBorracha      = ImageTk.PhotoImage(Image.open(os.path.join(image_path, "Borracha.png")).resize((30,30), Image.Resampling.LANCZOS))
imagemFreio         = ImageTk.PhotoImage(Image.open(os.path.join(image_path, "Freio.png")).resize((50,50), Image.Resampling.LANCZOS))
imagemTemperatura   = ImageTk.PhotoImage(Image.open(os.path.join(image_path, "Temperatura.png")).resize((50,50), Image.Resampling.LANCZOS))
imagemBateria       = ImageTk.PhotoImage(Image.open(os.path.join(image_path, "Bateria.png")).resize((50,50), Image.Resampling.LANCZOS))
imagemVelocidade    = ImageTk.PhotoImage(Image.open(os.path.join(image_path, "Velocidade.png")).resize((50,50), Image.Resampling.LANCZOS))
imagemRpm           = ImageTk.PhotoImage(Image.open(os.path.join(image_path, "Rpm.png")).resize((50,50), Image.Resampling.LANCZOS))
imagemConectar      = ImageTk.PhotoImage(Image.open(os.path.join(image_path, "Conectar.png")).resize((25,25), Image.Resampling.LANCZOS))
