string = "Some important text about crysis and global warming and war and pandemic and so on"


def func(string):
    list = []
    list = string.split()
    max_len = 0
    times_used = 0
    most_used = " "

    for i in list:
        if len(i) > max_len:
            max_len = len(i)
    print("Number of letters in the longest word =", str(max_len))
    for i in list:
        if list.count(i) > times_used:
            times_used = list.count(i)
            most_used = i
    print("Most used word - ", most_used)


func(string)
