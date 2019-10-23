def get_file_path(test_name, i):
    pattern = "/question-"
    extension = ".txt"
    str_path = str(test_name) + str(pattern) + str((i+1)) + extension

    return str_path
    
def get_answers(test_name, numQuestions):
    for i in range(numQuestions):
        with open (get_file_path(test_name, i), "r") as file:
            lines=file.readlines()

            for line in lines:
                print(line, end='')
    