import random

while 1:
    n_char = int(input("how many chars:"))
    n_sym = int(input("how many symbols:"))
    n_num = int(input("how many num:"))

    num_list = [str(i) for i in range(0, 10)]
    char_list = [chr(c) for c in range(65, 91)] + [chr(c) for c in range(97, 123)]
    sym_list = [chr(c) for c in range(35, 44)]
    # print(num_list)
    # print(char_list)
    # print(sym_list)

    # 1 pick the random num for each type
    selectedCharList = [random.choice(char_list) for i in range(n_char)]
    print(selectedCharList)
    selectedSymList = [random.choice(sym_list) for i in range(n_sym)]
    print(selectedSymList)
    selectedNumList = [random.choice(num_list) for i in range(n_num)]
    print(selectedNumList)

    selectedList = selectedNumList + selectedSymList + selectedCharList
    print(f"size of {selectedList} is {len(selectedList)}")
    # 2 fill the new string with the randomize
    password = ""
    while selectedList:
        password += selectedList.pop(random.randint(0, len(selectedList) - 1))
    print(password)
