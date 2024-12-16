from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class Screen:
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz

        # --------------------------------- Create Window ------------------------------------------##

        self.window = Tk()
        self.window.title("Quiz Brian")
        self.window.config(background=THEME_COLOR, pady=50, padx=50,)

        # --------------------------------- Create Lables --------------------------------------##

        self.score = Label(text=f"Score: {quiz.score}", font=("Arial", 15, "italic", "bold"),background=THEME_COLOR, fg="green" )
        self.score.grid(row=0, column=3,)
        self.score.config(pady=20)

        self.display_count_questions = Label(text=f"Q: {quiz.number}", font=("Arial", 15, "italic", "bold"),background=THEME_COLOR, fg="red")
        self.display_count_questions.grid(row=0, column=1)

        # --------------------------------- Create Canvas -------------------------------------------##

        self.canvas = Canvas(width=400,height=400, background="white")
        self.canvas.grid(row=1, column=1, columnspan=3)
        self.rounded_rectangle(10, 10, 390, 390, radius=80, fill="green", )

        self.display_q = self.canvas.create_text(200, 200, text="", font=("Arial", 15, "italic"), width=380)

        # ---------------------------------- Create Buttons_True -----------------------------------------##

        self.read_photo_ture = PhotoImage(file="images/true.png")
        self.button_ture = Button(image=self.read_photo_ture,
                                  highlightthickness=0,
                                  background=THEME_COLOR,
                                  command=self.check_ture)
        self.button_ture.grid(row=2, column=1)

        # --------------------------------------- Create Button False --------------------------------------##

        self.read_photo_false = PhotoImage(file="images/false.png")
        self.button_false = Button(image=self.read_photo_false,
                                   highlightthickness=0,
                                   background=THEME_COLOR,
                                   command=self.check_false)
        self.button_false.grid(row=2, column=3, pady=30)

        self.display_question()
        self.window.mainloop()

    # ------------------------------------- Creat Function For Display Question ---------------------------##

    def display_question(self):
        self.canvas.config(background="white")
        if self.quiz.still_has_questions():

            self.score.config(text=f"Score: {self.quiz.score}")
            q_question = self.quiz.next_question()
            self.canvas.itemconfig(self.display_q, text=q_question)
            self.display_count_questions.config(text=f"Q: {self.quiz.number}")

        else:
            self.button_ture.config(state="disabled")
            self.button_false.config(state="disabled")

            if self.quiz.check_number():
                self.rounded_rectangle(10, 10, 390, 390, radius=80, fill="green", )

                self.canvas.itemconfig(self.display_q, text="Sorry You Loss")
                self.canvas.config(background="red")
            else:
                self.rounded_rectangle(10, 10, 390, 390, radius=80, fill="red", )

                self.canvas.itemconfig(self.display_q, text="Congratulation You Win")
                self.canvas.config(background="green")

    # -------------------------------------- Create Functions For Check Answer ----------------------------##

    def check_ture(self):
        is_right = self.quiz.check_answer("True")
        self.feedback(is_right)

    def check_false(self):
        is_right = self.quiz.check_answer("False")
        self.feedback(is_right)

    def feedback(self, is_right):
        if is_right:
            self.canvas.config(background="green")
        else:
            self.canvas.config(background="red")

        self.window.after(500, self.display_question)

    def rounded_rectangle(self, x1, y1, x2, y2, radius=25, **kwargs):
        if 'fill' not in kwargs:
            kwargs['fill'] = "black"

        self.canvas.create_arc(x1, y1, x1 + radius * 2, y1 + radius * 2, start=90, extent=90, style="arc", **kwargs)
        self.canvas.create_arc(x2 - radius * 2, y1, x2, y1 + radius * 2, start=0, extent=90, style="arc", **kwargs)
        self.canvas.create_arc(x2 - radius * 2, y2 - radius * 2, x2, y2, start=270, extent=90, style="arc", **kwargs)
        self.canvas.create_arc(x1, y2 - radius * 2, x1 + radius * 2, y2, start=180, extent=90, style="arc", **kwargs)

        self.canvas.create_line(x1 + radius, y1, x2 - radius, y1, **kwargs)
        self.canvas.create_line(x1 + radius, y2, x2 - radius, y2, **kwargs)
        self.canvas.create_line(x1, y1 + radius, x1, y2 - radius, **kwargs)
        self.canvas.create_line(x2, y1 + radius, x2, y2 - radius, **kwargs)



