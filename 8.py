def sorter(string):
    """
    The function accepts a string and sorts it character by character.
    :param string: string
    :return: sorted string
    """

    lst = list(string)
    lst.sort(key=str.lower)
    string = ''.join(lst)

    return string


string = input()
res = sorter(string)
print(res)
