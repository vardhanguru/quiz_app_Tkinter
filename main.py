from question_model import Question
from data import question_data
from ui import *
import html
from quiz_brain import QuizBrain

question_bank = []

#converting each question and each answer and appending the object to the question bank
for question in question_data:
    #html unescape is used to escape special characters like " thos things
    question_text = html.unescape(question["question"])
    question_answer = html.unescape(question["correct_answer"])
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
#calling the quiz ui
quiz_ui=QuizInterface(quiz)
# quiz_ui.questions(question_bank)


# quiz_ui.main_canvas()
# while quiz.still_has_questions():
#     quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
