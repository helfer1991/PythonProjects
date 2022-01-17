class QuizBrain:
    def __init__(self, questions_list):
        self.question_number = 0
        self.score = 0
        self.questions_list = questions_list
    
    def still_has_questions(self):
        return self.question_number < len(self.questions_list)
    
    def increment_score(self):
        self.score += 1
    
    def is_answer_right(self, answer, right_answer):
        if answer == right_answer:
            self.increment_score()
    
    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {current_question.text}\nTrue or false?: ")
        self.is_answer_right(answer, current_question.answer)

        if self.question_number == len(self.questions_list):
            self.print_score()

        return answer
    
    def print_score(self):
        print(f"\nYour score was: {self.score} points\n")