from Quiz.each_question import Question
from questions import quiz_questions

still_more_question = True

class QuizBrain:
    def __init__(self, questions_list):
        self.question_number = 0
        self.question_list = questions_list
        self.score = 0

    def next_question(self):
        curr_question = self.question_list[self.question_number]
        self.question_number += 1
        value = input(f'Q {self.question_number}: {curr_question.question}? True/False : ')
        self.check_answer(value, curr_question.answer)

    def check_answer(self, value, answer):
        if answer.lower() == value.lower():
            self.score += 2
            print('You guessed it right, your score is ', self.score)
        else:
            print ('You guessed it wrong.. correct answer is: ', answer)
            self.score -= 1
            print('your score is ', self.score)
        print('---------------- *** ----------------')

    def new_question(self):
        if self.question_number == len(self.question_list):
            print(f'Thank you for playing!, you\'ve scored, {self.score}/{2* len(self.question_list)}')
        return self.question_number < len(self.question_list)

list_of_questions = []
for question in quiz_questions:
    current_question = question['question']
    current_answer = question['correct_answer']
    current_options = question['incorrect_answers']
    new_question = Question(current_question, current_answer, current_options)
    list_of_questions.append(new_question)
quiz = QuizBrain(list_of_questions)

while quiz.new_question():
     quiz.next_question()


