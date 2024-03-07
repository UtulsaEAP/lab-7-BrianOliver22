""""
name: Brian Oliver
date: 3/7/2024 12:00
"""
def courseGrade():
    
    # TODO: Declare any necessary variables here. 
    file_comp = input()
    first = []
    last = []
    midterm1 = []
    midterm2 = []
    final = []
    averages = []
    letter_grade = []
    midterm1_avg = 0
    midterm2_avg = 0
    final_average = 0

      
    # TODO: Read a file name from the user and read the tsv file here. 
    with open("./Problem 3/"+ file_comp,'r') as inputs:
        inputs = inputs.read().split()
        
        """"
        print(input_len)
        print(inputs)
        """
    
        for i in range(0,int(len(inputs)),5):
            first.append(inputs[i])
            last.append(inputs[i+1])
            midterm1.append(inputs[i+2])
            midterm2.append(inputs[i+3])
            final.append(inputs[i+4])
        
   
    # TODO: Compute student grades and exam averages, then output results to a text file here. 
    for i in range(len(first)):
        avg = (int(midterm1[i]) + int(midterm2[i]) + int(final[i]))/3
        averages.append(avg)
    for i in range(len(first)):
        if averages[i] >= 90:
            letter_grade.append("A")
        elif (averages[i] < 90) and (averages[i] >= 80):
            letter_grade.append("B")
        elif (averages[i] < 80) and (averages[i] >= 70):
            letter_grade.append("C")
        elif (averages[i] < 70) and (averages[i] >= 60):
            letter_grade.append("D")
        elif (averages[i] < 60):
            letter_grade.append("F")
    for i in range(len(first)):
        midterm1_avg += int(midterm1[i]) 
    midterm1_avg = midterm1_avg/len(first)
    for i in range(len(first)):
        midterm2_avg += int(midterm2[i]) 
    midterm2_avg = midterm2_avg/len(first)
    for i in range(len(first)):
        final_average += int(final[i]) 
    final_average = final_average/len(first)
    for i in range(len(first)):
        print(first[i] + "   " + last[i] + "   " + str(midterm1[i]) + "   " + str(midterm2[i]) + "   " + str(final[i]) + "   " + letter_grade[i])
    print("Averages: midterm1 " + str(f'{midterm1_avg:.2f}') + ", midterm2 " + str(f'{midterm1_avg:.2f}') + ", final " + str(f'{final_average:.2f}'))
    return

if __name__ == "__main__":
    courseGrade()
    
    