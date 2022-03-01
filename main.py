answr = 'Artificial intelligence wide-ranging branch computer science concerned with building smart machines capable of performing tasks that typically require human intelligence. AI is an interdisciplinary science with multiple approaches, but advancements in machine learning and deep learning are creating a paradigm shift in virtually every sector of the tech industry'
answerlist = answr.split(' ')
name = input('please input name : ')
enterd_answer = input('please input answer : ')
answer = answr.lower()
entered_answer = enterd_answer.lower()
entered_answer = entered_answer.split(" ")
point = 0
for i in range(len(entered_answer)):
    if entered_answer[i] in answerlist:
        point+=1

point = point*10/len(answerlist)
point = round(point, 1)
print(f'Your Answer : {enterd_answer}')
print(f"you've scored {point}")
points=str(point)
with open('marks.json', 'a+') as mrks:
    mrks.write(f'\n"{name}" : {points} from 10')
# with open('marks.json', 'r') as mrks:
#     a = mrks.read()
#     print(a)