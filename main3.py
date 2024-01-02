def sonni_qoshish(list):
    num = int(input("Sonni kiriting : "))
    for num in list :
        list.remove(num)
        list.append(num)
        list.append(num)
        print(list)
    else :
        print("Xatolik yuz berdi :")
list = [8,2,4,6,8]
sonni_qoshish(list)
