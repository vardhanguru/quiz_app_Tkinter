class Question:
    #each time a new object creates that have a question and answer to it.
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer
