from tkinter import *
THEME_COLOR = "#375362"
name="vardhan"
class QuizInterface:
    def __init__(self,quiz):
        #initilizing the main window and canvas with all the elements
        self.window=Tk()
        self.window.title("Quiz App")
        self.current_question=0
        self.quiz=quiz
        self.window.config(pady=20,padx=20,bg=THEME_COLOR)
        self.canvas=Canvas(width=200,height=200)
        self.score_label=Label(text=f"score: {self.quiz.score}",fg="white",bg=THEME_COLOR)
        self.score_label.grid(row=0,columns=1)
        self.question_text=self.canvas.create_text(90,90,text=self.quiz.next_question(),font=('Arial',11,'italic'),width=120)
        self.canvas.grid(row=1,column=0,columnspan=2,pady=20)
        self.tru_pic=PhotoImage(file="images/true.png")
        self.tru_button=Button(image=self.tru_pic,highlightthickness=0,command=self.questions)
        self.false_pic = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.false_pic,highlightthickness=0,command=self.false_pressed)
        self.tru_button.grid(row=2,column=1,padx=5,pady=5)
        self.false_button.grid(row=2, column=0,pady=5,padx=5)
        self.window.mainloop()

    #this is used to get next question from the question bank. if there are no questions it displays final score and over message
    def get_next_question(self):
        #the below line is used to get back to original color of the canvas after red or green color is blinked
        self.canvas.config(bg="white")
        q_text=self.quiz.next_question()
        if q_text!="over":
            self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            self.tru_button.config(state="disabled")
            self.false_button.config(state="disabled")
            self.canvas.itemconfig(self.question_text, text=f"Quiz has completed, you're final score is {self.quiz.score}")

    #this is called when the true button is got hitted.
    def questions(self):
        #if the answer is true we have to give green colour and score should be increased by one.
        if self.quiz.check_answer("True")==True:
            self.canvas.config(bg="green")
            self.score_label.config(text=f"score: {self.quiz.score}", fg="white", bg=THEME_COLOR)
        #else it give red colour and call the next question
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next_question)


    def false_pressed(self):
        if self.quiz.check_answer("False")==True:
            self.canvas.config(bg="green")
            self.score_label.config(text=f"score: {self.quiz.score}", fg="white", bg=THEME_COLOR)
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next_question)
        # self.canvas.config(bg="white")





