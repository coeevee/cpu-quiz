# python 3.11.9
# 2/9/2025
# aurthor: coeevee
# github.com/coeevee/cpu-quiz
i3orr3 = 0
i5orr5 = 0
i7or7 = 0
i9orr9 = 0
# the "final" function is for the end of the quiz and shows the score of the quiz
def final():
    print("you are done with the quiz")
    print("these are the results")
    print("i3 or ryzen 3: " + str(i3orr3))
    print("i5 or ryzen 5: " + str(i5orr5))
    print("i7 or ryzen 7: " + str(i7or7))
    print("i9 or ryzen 9: " + str(i9orr9))
    print("thank you for taking the quiz")
    print("aurthor: coeevee gibhub.com/coeevee/cpu-quiz")
# the "answer" function is for the questions and answers and adds to the score based on the answer
def answer(ans):
    global i3orr3
    global i5orr5
    global i7or7
    global i9orr9
    if ans == "end":
        final()
    elif ans == "a":
        i3orr3 += 1
        return i3orr3
    elif ans == "b":
        i5orr5 += 1
    elif ans == "c":
        i7or7 += 1
        i9orr9 += 1
    else:
        print("please enter a valid answer")
        answer(input("answer: "))
# the quiz itself
print("this is a quiz to see what cpu is best for you")
print("answer the following questions to the best of your ability by choseing a. b. or c.")
print("1. what kind of computer are you building?")
print("a. bugest")
print("b. mid range")
print("c. high end")
answer(input("answer: "))
print("2. what is your main use for the computer?")
print("a. just browsing")
print("b. work")
print("c. gaming")
answer(input("answer: "))
print("3. do you care about power consumption?")
print("a. yes")
print("b. kind of")
print("c. no")
answer(input("answer: "))
print("4. do you care about heat?")
print("a. yes")
print("b. kind of")
print("c. no")
answer(input("answer: "))
print("5. do play intensive games?")
print("a. no")
print("b. sometimes")
print("c. yes")
answer(input("answer: "))
print("6. do you do any video editing?")
print("a. no")
print("b. sometimes")
print("c. yes")
answer(input("answer: "))
print("7. do you do any 3d rendering?")
print("a. no")
print("b. sometimes")
print("c. yes")
answer(input("answer: "))
print("8. do you do any streaming?")
print("a. no")
print("b. sometimes")
print("c. yes")
answer(input("answer: "))
#ends the quiz
answer("end")