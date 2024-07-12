from question_model import Question
from data import question_data
from quiz_brain import QuestionBrain

question_bank = []

for dict_question in question_data:
    #把問題和解答建立成一個個的 Object 儲存在question_bank 這個數列中
    text = dict_question["text"]
    answer = dict_question["answer"]
    question_temp = Question(text, answer)
    question_bank.append(question_temp)

#取出text的方式，因為是 object 後面要加上 ```.text``` 才能叫出問題
# print(question_bank[0])
# print(question_bank[0].text)

test = QuestionBrain(question_bank)

while test.still_has_questions():
    #測試 class 的 method 是否正常運作
    # print(test.still_has_questions())
    test.next_question()
    # print(test.question_list[test.question_number].answer)

print("That's all! Have a nive one ☺️")
print(f"Your final score is {test.score}, goode job!")

