# write a program to reverse a string and array

def ReverseStrArrWithSlice(data):
    print(data[::-1])

def ReverseStrArrWithLoop(data):
    newStr = ""
    newArr = []
    if data == type(str):
        for l in data:
            newStr += l
        print(str(newStr))
    else:
        for ele in data:
            newArr.insert(0,ele)
        print(newArr)

str = "python"
arr = [3,5,2,6,8,7,6,34,23]
ReverseStrArrWithSlice(arr)
ReverseStrArrWithLoop(str)

