class QuizBrain:

    def __init__(self, questions) -> None:
        self.question_number = 0
        self.user_score = 0
        self.question_list = questions

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(
            f'Q.{self.question_number}: {question.text} (True/False)?: ')
        self.check_answer(answer, question.answer)

    def still_has_questions(self) -> bool:
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print('You got it right!')
            self.user_score += 1
            print(
                f'Your current score is: {self.user_score}/{self.question_number}')
        else:
            print('Sorry that is wrong.')
        print(f'The correct answer was: {correct_answer}')
        print("\n")