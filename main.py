print('Buzz Terminal')
test_name = "itrac"

# numQuestions vai pegar dinamicamente do teste;
numQuestions = 1

points = 4*numQuestions

# perguntas vão vir dinamicamente

for i in range(numQuestions):
    with open (str(test_name) + "/question-" + str((i+1))  + ".txt", "r") as file:
        lines=file.readlines()
        
        for line in lines:
            print(line, end='')
