def binary_search_range(lst, target):
    answer = [-1, -1]
    if target in lst:
        first = -1
        last = -1
        for i in range(len(lst)):
            if lst[i] == target:
                if first == -1:
                    first = i
                last = i
                if (last - first) > (answer[1] - answer[0]):
                    answer[0] = first
                    answer[1] = last
            else: first = -1
    return [answer[0], answer[1]]
print(binary_search_range([1, 2, 2, 2, 3], 2))
print(binary_search_range([2, 2, 2], 2))
print(binary_search_range([1, 2, 3], 4))
print(binary_search_range([], 1))

def is_balanced_brackets(s):
    # ( - 1, [ - 2, { - 3
    count1 = 0
    count2 = 0
    count3 = 0
    for i in s:
        if i in ['(', ')', '[', ']', '{', '}']:
            if i == '(':
                count1 +=1
            elif i == ')':
                count1 -= 1
            elif i == '[':
                count2 += 1
            elif i == ']':
                count2 -= 1
            elif i == '{':
                count3 +=1
            else:
                count3 -= 1
        else: continue
    if count1 == count2 == count3 == 0:
        return True
    else:
        return False
# print(is_balanced_brackets("()[]{}"))
# print(is_balanced_brackets("([{}])"))
# print(is_balanced_brackets(""))
# print(is_balanced_brackets("(]"))
print(is_balanced_brackets("([)]"))
# print(is_balanced_brackets("("))
# print(is_balanced_brackets("a(b)c"))
