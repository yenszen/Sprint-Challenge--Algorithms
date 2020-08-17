'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    str1 = word
    str2 = "th"

    n1 = len(str1)
    n2 = len(str2)

    if n1 == 0 or n1 < n2:
        return 0
    
    if str1[0:n2] == str2:
        return count_th(str1[n2-1:]) + 1
    
    return count_th(str1[n2-1:])