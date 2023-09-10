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
import tkinter as tk
from PIL import Image, ImageTk

class FlashcardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Flashcard App")

        self.current_flashcard = 0
        self.showing_answer = False

        self.flashcard_image = self.load_and_resize_image(flashcards[self.current_flashcard]["pregunta"])
        self.flashcard_label = tk.Label(root, image=self.flashcard_image)
        self.flashcard_label.pack()

        self.flashcard_image2 = self.load_and_resize_image("F:/programacion/flashcards/images/NotasPentagrama/Cuadrado.png")
        self.flashcard_label2 = tk.Label(root, image=self.flashcard_image2)
        self.flashcard_label2.pack()
       
        

        self.show_answer_button = tk.Button(root, text="Mostrar Respuesta", command=self.show_answer)
        #self.show_answer_button.place(x=10, y=810)  # Posición fija para el botón
        self.show_answer_button.pack()

        self.next_question_button = tk.Button(root, text="Siguiente Pregunta", command=self.next_question)
        #self.next_question_button.place(x=150, y=810)  # Posición fija para el botón
        self.next_question_button.pack()

    def load_and_resize_image(self, image_path):
        original_image = Image.open(image_path)
        resized_image = original_image.resize((400, 400), Image.ANTIALIAS)
        return ImageTk.PhotoImage(resized_image)
    def load_and_resize_image2(self, image_path):
        original_image = Image.open(image_path)
        resized_image = original_image.resize((400, 400), Image.ANTIALIAS)
        return ImageTk.PhotoImage(resized_image)

    def show_answer(self):
        self.flashcard_image = self.load_and_resize_image2(flashcards[self.current_flashcard]["pregunta"])
        self.flashcard_label.config(image=self.flashcard_image)
                
        self.flashcard_image2 = self.load_and_resize_image2(flashcards[self.current_flashcard]["respuesta"])
        self.flashcard_label2.config(image=self.flashcard_image2)


        self.showing_answer = True

    def next_question(self):
        
            self.showing_answer = False
            self.flashcard_image2 = self.load_and_resize_image("F:/programacion/flashcards/images/NotasPentagrama/Cuadrado.png")

            self.flashcard_label2.config(image=self.flashcard_image2)
            
            self.current_flashcard += 1
            if self.current_flashcard >= len(flashcards):
                self.current_flashcard = 0
            self.flashcard_image = self.load_and_resize_image(flashcards[self.current_flashcard]["pregunta"])
            self.flashcard_label.config(image=self.flashcard_image)
            

if __name__ == "__main__":
    root = tk.Tk()
    app = FlashcardApp(root)
    root.mainloop()