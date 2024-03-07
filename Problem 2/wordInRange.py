def wordInRange():
    #Type your code here
    file_comp = str(input())
    min_word = str(input())
    max_word = str(input())
    range_list = []
    with open("./Problem 2/input1.txt", 'r') as inputs:
        inputs = inputs.read().split()
        lens = int(len(inputs))
        for i in range (len(inputs)):
            if (inputs[i]<= max_word):
                if min_word >= min_word:
                    range_list.append(" - in range")
            elif inputs[i] >= max_word:
                range_list.append(" - not in range")
            elif (inputs[i] <= max_word):
                range_list.append(" - not in range")
        for i in range(len(inputs)):
            print(inputs[i]+range_list[i])
    return
if __name__ == '__main__':
    wordInRange()