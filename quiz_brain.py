class QuizBrain:

    def __init__(self, q_list):
        #initializes some values
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        #checks if there are questions left. if there are returns true else returns false
        return self.question_number < len(self.question_list)

    #will go to next question if there are questions available
    def next_question(self):
        if self.still_has_questions():
            self.current_question = self.question_list[self.question_number]
            self.question_number += 1

            return f"Q.{self.question_number}: {self.current_question.text} "
        else:
            return "over"
        # user_answer = input()
        # self.check_answer(user_answer)

    #checks the answer and returns 0 or 1
    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return 1
        else:
            return 0

