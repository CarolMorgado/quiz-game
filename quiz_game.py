answer = 0

# question one
print('Question 1: What is the capital of Germany?')
print('a) Paris')
print('b) Berlin')
print('c) Lisbon')
# user answer
answer1 = input('Your answer: ').lower()
# evaluate question one
if answer1 == 'b':
    print('Correct!')
    answer += 1
else:
    print('Incorrect!')


# question two
print('Question 2: What is the capital of Portugal?')
print('a) Paris')
print('b) Berlin')
print('c) Lisbon')
# user answer
answer2 = input('Your answer: ').lower()
# evaluate question two
if answer2 == 'c':
    print('Correct!')
    answer += 1
else:
    print('Incorrect!')


# question three
print('Question 3: What is the capital of France?')
print('a) Paris')
print('b) Berlin')
print('c) Lisbon')
# user answer
answer3 = input('Your answer: ').lower()
# evaluate question two
if answer3 == 'a':
    print('Correct!')
    answer += 1
else:
    print('Incorrect!')


# total score
Total_score = input(
    f'Your score: {answer} / 3')
