import os
import openai
from PyPDF2 import PdfReader
from pdf2image import convert_from_path
from config import *
from PIL import Image

# FUNZIONI
# openai
def format_text_ai(content):
	# Leggo la API KEY di OpenAI
	openai.api_key = os.getenv("OPENAI_API_KEY")

	# Definisco l'input
	# content = "E' nato prima l'uovo o la gallina?"

	response = chat_completion = openai.ChatCompletion.create(
		model="gpt-3.5-turbo", 
		messages=[
			{"role": "user", "content": content}
		]
	)

	print(response['choices'][0]['message']['content'])
     
# Funzione per estrarre le immagini da tutti i file PDF in una cartella
def extract_images_from_pdfs_in_folder(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            pdf_file = os.path.join(folder_path, filename)
            images = extract_images_from_pdf(pdf_file)
            print(f"Immagini estratte da {filename}:")
            for i, image in enumerate(images):
                image_quality = 70  # Imposta la qualità desiderata (0-100)
                image.save(f"image_{i}.jpg", "JPEG", quality=image_quality, optimize=True)

# Funzione per estrarre le immagini da un file PDF
def extract_images_from_pdf(pdf_file):
    images = convert_from_path(pdf_file)
    return images


extract_images_from_pdfs_in_folder(file_in_path)