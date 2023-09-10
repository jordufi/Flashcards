import tkinter as tk
from PIL import Image, ImageTk

flashcards = [
    {"pregunta": "F:/programacion/flashcards/images/NotasPentagrama/Do.png", "respuesta": "F:/programacion/flashcards/images/NotasPentagrama/R_Do.png"},
    {"pregunta": "F:/programacion/flashcards/images/NotasPentagrama/Re.png", "respuesta": "F:/programacion/flashcards/images/NotasPentagrama/R_Re.png"},
    {"pregunta": "F:/programacion/flashcards/images/NotasPentagrama/Mi.png", "respuesta": "F:/programacion/flashcards/images/NotasPentagrama/R_Mi.png"},
    {"pregunta": "F:/programacion/flashcards/images/NotasPentagrama/Fa.png", "respuesta": "F:/programacion/flashcards/images/NotasPentagrama/R_Fa.png"},
    {"pregunta": "F:/programacion/flashcards/images/NotasPentagrama/Sol.png", "respuesta": "F:/programacion/flashcards/images/NotasPentagrama/R_Sol.png"},
    {"pregunta": "F:/programacion/flashcards/images/NotasPentagrama/La.png", "respuesta": "F:/programacion/flashcards/images/NotasPentagrama/R_La.png"},
    {"pregunta": "F:/programacion/flashcards/images/NotasPentagrama/Si.png", "respuesta": "F:/programacion/flashcards/images/NotasPentagrama/R_Si.png"},
    {"pregunta": "F:/programacion/flashcards/images/NotasPentagrama/Do2.png", "respuesta": "F:/programacion/flashcards/images/NotasPentagrama/R_Do.png"},

]
#flashcards = [
#    {"pregunta": "F:/programacion/flashcards/images/NotasPentagrama/Do.png", "respuesta": "F:/programacion/flashcards/images/NotasPentagrama/A_Do.png"},
#    {"pregunta": "F:/programacion/flashcards/images/NotasPentagrama/Re.png", "respuesta": "F:/programacion/flashcards/images/NotasPentagrama/A_Re.png"},
#    {"pregunta": "F:/programacion/flashcards/images/NotasPentagrama/Mi.png", "respuesta": "F:/programacion/flashcards/images/NotasPentagrama/A_Mi.png"},
#    {"pregunta": "F:/programacion/flashcards/images/NotasPentagrama/Fa.png", "respuesta": "F:/programacion/flashcards/images/NotasPentagrama/A_Fa.png"},
#    {"pregunta": "F:/programacion/flashcards/images/NotasPentagrama/Sol.png", "respuesta": "F:/programacion/flashcards/images/NotasPentagrama/A_Sol.png"},
#    {"pregunta": "F:/programacion/flashcards/images/NotasPentagrama/La.png", "respuesta": "F:/programacion/flashcards/images/NotasPentagrama/A_La.png"},
#    {"pregunta": "F:/programacion/flashcards/images/NotasPentagrama/Si.png", "respuesta": "F:/programacion/flashcards/images/NotasPentagrama/A_Si.png"},
#    {"pregunta": "F:/programacion/flashcards/images/NotasPentagrama/Do2.png", "respuesta": "F:/programacion/flashcards/images/NotasPentagrama/A_Do.png"},
#]

i=0
for e in flashcards: 

        image1 = Image.open(e["pregunta"])
        image2 = Image.open(e["respuesta"])

        image1 = image1.resize((400, 400))
        image2 = image2.resize((400, 400))

        combined_image = Image.new('RGB', (400, 800), (250, 100, 0))
        combined_image.paste(image1, (0, 0))
        combined_image.paste(image2, (0, 400))
        combined_image.save(str(i)+"A_A.png")
        i=i+1
