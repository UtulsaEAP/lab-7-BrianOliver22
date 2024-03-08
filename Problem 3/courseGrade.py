""""
name: Brian Oliver
date: 3/7/2024 7:00
"""
def courseGrade():    
    # TODO: Declare any necessary variables here. 
    file_comp = str(input())
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
    num = file_comp.split("fo")
    num2 = num[1].split(".")
    if num2[0] == "":
        num3 = ""
    elif num2[0] == "2":
        num3 = "2"
    elif num2[0] == "1":
        num3 = "1"
    else:
        num3 = "error"
      
    # TODO: Read a file name from the user and read the tsv file here. 
    with open(file_comp,"r") as inputs:
        "./Problem 3/"
        inputs = inputs.read().split()
        
    
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
    with open("./Problem 3/report"+num3+".txt",'w+') as file:
        for i in range(len(first)):
            file.write( first[i] + "\t" + last[i] + "\t" + str(midterm1[i]) + "\t" + str(midterm2[i]) + "\t" + str(final[i]) + "\t" + letter_grade[i]+"\n")
        file.write("\n" + "Averages: midterm1 " + str(f'{midterm1_avg:.2f}') + ", midterm2 " + str(f'{midterm2_avg:.2f}') + ", final " + str(f'{final_average:.2f}'))
        file.close()
    
    return

if __name__ == "__main__":
    courseGrade()    
    