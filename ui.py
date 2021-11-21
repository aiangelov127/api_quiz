from tkinter import *
from quiz_brain import QuizBrain


Q_FONT = ("Courier", 24, "bold")
SCORE_FONT = ("Courier", 20, "bold")
TEXT_COLOR = "black"
THEME_COLOR = "#375362"

class UI:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.config(bg=THEME_COLOR, padx=50, pady=50)
        self.window.title("Quiz")
        self.window.minsize(500, 500)

        self.canvas = Canvas(width=400,
                             height=400,
                             highlightthickness=0)
        self.question_text = self.canvas.create_text(200, 200,
                                                     text="some text",
                                                     fill=TEXT_COLOR,
                                                     font=Q_FONT,
                                                     width=380)

        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.label_score = Label(text="Score: 0",
                                 font=SCORE_FONT,
                                 bg=THEME_COLOR,
                                 fg=TEXT_COLOR,
                                 justify=CENTER)
        self.label_score.grid(row=0, column=0, columnspan=2)

        image_true = PhotoImage(file="./images/true.png")
        self.button_true = Button(image=image_true, command=self.answer_true, highlightthickness=0)
        self.button_true.grid(row=2, column=0)

        image_false = PhotoImage(file="./images/false.png")
        self.button_false = Button(image=image_false, command=self.answer_false, highlightthickness=0)
        self.button_false.grid(row=2, column=1)

        self.get_next_q()

        self.window.mainloop()

    def answer_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def answer_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right is True:
            self.canvas.config(bg="green")
        elif is_right is False:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_q)

    def get_next_q(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions() is True:
            q_text = self.quiz.next_question()
            self.label_score.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text = f"You have completed the quiz. \n"
                                                              f"Your score is: {self.quiz.score}")
            self.answer_true.config(state="disabled")
            self.answer_false.config(state="disabled")
