# ---------------- QUIZ PROJECT ---------------- #

# Question class
class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer


# QuizBrain class
class QuizBrain:
    def __init__(self, questions):
        self.question_number = 0
        self.score = 0
        self.questions = questions

    def still_has_questions(self):
        return self.question_number < len(self.questions)

    def next_question(self):
        current_question = self.questions[self.question_number]
        self.question_number += 1
        user_answer = input(
            f"Q.{self.question_number}: {current_question.text} (True/False): "
        )
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("✅ Correct!")
        else:
            print("❌ Wrong!")

        print(f"Correct answer: {correct_answer}")
        print(f"Score: {self.score}/{self.question_number}")
        print("-" * 30)


# Question data
question_data = [
    {"question": "Python is a programming language.", "answer": "True"},
    {"question": "HTML is used for backend development.", "answer": "False"},
    {"question": "Lists are mutable in Python.", "answer": "True"},
    {"question": "Tuples can be changed after creation.", "answer": "False"},
    {"question": "Python supports Object Oriented Programming.", "answer": "True"}
]


# Creating question objects
question_bank = []
for q in question_data:
    question = Question(q["question"], q["answer"])
    question_bank.append(question)


# Running the quiz
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("🎉 Quiz Completed!")
print(f"Your final score: {quiz.score}/{len(question_bank)}")
