from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


def get_questions():
    questions = []
    for question in question_data:
        questions.append(
            Question(question['text'], question['answer']))
    return questions


def main():
    question_bank = get_questions()
    quiz = QuizBrain(question_bank)
    while quiz.still_has_questions():
        quiz.next_question()
    print('You\'ve completed the quiz.')
    print(f'Your final score was: {quiz.user_score}/{quiz.question_number}')


if __name__ == "__main__":
    main()
