list = []
list.append("a")
list.append("ab")
list.append("abc")
list.append("abcd")
list.append("abcde")
list.append("abcdef")
list.append("abcdefg")


def all_eq(list):
    print("Start list:\n", list)
    list_len = len(list)
    print("len =", str(list_len))
    list.sort(reverse=True)
    print("Sorted list:\n", list)
    longest = len(list[0])
    print("Number of letters in longest = ", longest)
    final_list = []
    for i in list:
        string = i
        num = longest - len(string)
        i = str(i + "_" * num)
        final_list.append(i)
    print("Final version:\n", final_list)


all_eq(list)
