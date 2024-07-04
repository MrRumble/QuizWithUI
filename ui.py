from tkinter import *
from quiz_brain import QuizBrain
import time

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):   # <- This asserts that quiz_brain parameter must be of type QuizBrain
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(height=250, width=300, bg = 'white')
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

        self.score_text = "Score: 0"
        self.score_label = Label(text=self.score_text, font=("Arial", 20), anchor="center", bg=THEME_COLOR, fg = "white")
        self.score_label.grid(row=0, column=1)

        self.true_image = PhotoImage(file='images/true.png')
        self.true_button = Button(self.window, image=self.true_image, bd=0, bg=THEME_COLOR, command=self.button_click_true)
        self.true_button.grid(row=2, column=0, pady=10)
        
        self.false_image = PhotoImage(file='images/false.png')
        self.false_button = Button(self.window, image=self.false_image, bd=0, bg=THEME_COLOR, command=self.button_click_false)
        self.false_button.grid(row=2, column=1, pady=10)  # Place in row 2, column 1

        self.question_label = Label(text="", font= ("Arial", 20, 'italic'), anchor='center', wraplength=280, background= 'white')
        self.question_label.grid(row=1, column=0, columnspan=2)

        self.get_next_question()
        self.window.mainloop()
        

    def get_next_question(self):
        self.canvas.config(bg='white')
        self.false_button.config(state=NORMAL)
        self.true_button.config(state=NORMAL)
        if self.quiz.still_has_questions():
            question_text = self.quiz.next_question()
            self.question_label.config(text=question_text)
        else:
            self.canvas.config(bg='gold')
            self.false_button.config(state=DISABLED)
            self.true_button.config(state=DISABLED)
            self.question_label.config(text=self.quiz.final_score())

    def button_click_true(self):
        if self.quiz.current_question.answer == "True":
            self.quiz.score += 1
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.reset_feedback()
        

    def button_click_false(self):
        if self.quiz.current_question.answer == "False":
            self.quiz.score += 1
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.reset_feedback()

    def update_score(self):
        self.score_label.config(text= f'Score: {self.quiz.score}')

    def reset_feedback(self):
        self.true_button.config(state=DISABLED)
        self.false_button.config(state=DISABLED)
        self.update_score()
        self.window.after(1000, lambda: self.canvas.config(bg='white'))
        self.window.after(1000, self.get_next_question)
        
    