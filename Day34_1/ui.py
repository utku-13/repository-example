THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain


class QuizInterface():
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz_brain = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=100,pady=20,bg=THEME_COLOR)
        self.window.minsize(500,500)

        self.score_label = Label(text="score:0",fg="white",bg=THEME_COLOR)
        self.score_label.grid(row=0,column=1)

        self.canvas = Canvas(width=300,height=300,bg="white")
        self.question_text1 = self.canvas.create_text(150,150,text="Question",fill=THEME_COLOR,font=("Arial",20,"italic"),width=280)
        self.canvas.grid(row=1,column=0,columnspan=2)
        
        self.score = 0

        true_image = PhotoImage(file="images/true.png")
        self.button_true = Button(image=true_image,command=self.chechk_answer_true)
        self.button_true.grid(row=2,column=0,padx=10,pady=10)
        
        false_image = PhotoImage(file="images/false.png")
        self.button_false = Button(image=false_image,command=self.check_answer_false)
        self.button_false.grid(row=2,column=1,padx=10,pady=10)
        
        self.show_next()

        
        self.window.mainloop()
    
    def show_next(self):
        self.canvas.config(bg="white")
        if self.quiz_brain.still_has_questions():
            question = self.quiz_brain.next_question()
            self.canvas.itemconfig(self.question_text1, text=question)
        else: 
            self.canvas.itemconfig(self.question_text1, text="You have reached the final.")
            self.button_false.config(state="disabled")
            self.button_true.config(state="disabled")

    def chechk_answer_true(self):
        is_it_correct = self.quiz_brain.check_answer("True")
        if is_it_correct:
            self.score += 1
            self.score_label.config(text=f"score:{self.score}")
            self.canvas.config(bg="green")
            self.window.after(3000, self.show_next)
        else: 
            self.canvas.config(bg="red")
            self.window.after(1000, self.show_next)
    def check_answer_false(self):
        is_it_false = self.quiz_brain.check_answer("False")
        if is_it_false:
            self.score += 1
            self.score_label.config(text=f"score:{self.score}")
            self.canvas.config(bg="green")
            self.window.after(3000, self.show_next)
        else: 
            self.canvas.config(bg="red")
            self.window.after(1000, self.show_next)   
        
        

            
       




       


        

        

