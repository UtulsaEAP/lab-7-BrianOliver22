def fileNameChange():
    #type your code here
    file_comp = input()
    with open(file_comp, 'r' ) as red:
        lis = red.read().split()
        num = len(lis)
        print(num)
        litic = []
        for i in range(int(len(lis))):
            token = lis[i].split("_")
            if (token[1] == "photo.jpg"):
                litic.append(token[0] + "_info.txt" )
    for i in range(len(litic)):
        print(litic[i])
    return

if __name__ == '__main__':
    fileNameChange()