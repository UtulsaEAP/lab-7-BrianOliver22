""""
name: Brian Oliver
date: 3/7/2024 12:30
"""
def fileNameChange():
    #type your code here
    file_comp = input()
    with open(file_comp, 'r' ) as red:
        lis = red.read().split()
        num = len(lis)
        litic = []
        for i in range(int(len(lis))):
            token = lis[i].split("_")
            if (token[1] == "photo.jpg"):
                litic.append(token[0] + "_info.txt" )
            elif (token[1] == "info.txt"):
                litic.append(lis[i])
    for i in range(len(litic)):
        print(litic[i])
    return

if __name__ == '__main__':
    fileNameChange()