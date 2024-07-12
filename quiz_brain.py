class QuestionBrain:
    '''hello'''
    def __init__(self, q_list):

        self.question_number = 0
        self.question_list = q_list
        self.score = 0
        #跟 Angela 不一樣，他這邊不是直接 call question_bank，而是把它寫在 class 內 __init__(self, q_list)
        # 解答!! 因為我在調用 quesion_bank 這個 list 的時候又多加一個 [] 在外面，所以變成list 中的 list [[.....]]

    def still_has_questions(self):
        return self.question_number < len(self.question_list)
        # 這一行等同以下4行
        # if self.question_number > len(self.question_list):
        #     return False
        # else:
        #     return True
    def next_question(self):
        current_q = self.question_list[self.question_number]
        user_ans = input(f"Q.{self.question_number+1}: {current_q.text} (True/False)")
        self.question_number += 1
        self.check_ans(user_ans, current_q.answer)

    def check_ans(self, user_ans, correct_ans):
        if user_ans.lower() == correct_ans.lower():
            print("You are right!")
            self.score += 1

        else:
            print("You are wrong")

        print(f"the correct ans: {correct_ans}.")
        print(f"your score: {self.score}, current question number {self.question_number}")
        print("\n")

