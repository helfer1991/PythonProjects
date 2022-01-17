from data import question_data
from quiz_model import QuizQuestion
from quiz_brain import QuizBrain

quiz_list = []

for data in question_data:
    quiz_list.append(QuizQuestion(data['text'], data['answer']))
    
quiz = QuizBrain(quiz_list)

while quiz.still_has_questions():
    quiz.next_question()