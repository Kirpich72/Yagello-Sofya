# номер 1
def binary_search_range(lst, target):
    first = -1
    last = -1
    left = 0
    right = len(lst)-1
    while left <= right:
        indMid = (left+right)//2
        if lst[indMid] > target:
            right = indMid -1
        elif lst[indMid] < target:
            left = indMid + 1
        else:
            first = indMid
            right = indMid -1
    left = 0
    right = len(lst)-1
    while left <= right:
        indMid = (left+right)//2
        if lst[indMid] > target:
            right = indMid -1
        elif lst[indMid] < target:
            left = indMid + 1
        else:
            last = indMid
            left = indMid + 1
    return (first, last)
        
   
def test_binary_search_range_empty_list_return_no_found():
    res =  binary_search_range([], 1)
    assert res == (-1, -1)
def test_binary_search_range_element_not_in_list_return_no_found():
    res =  binary_search_range([1,2,3], 4)
    assert res == (-1, -1)
def test_binary_search_range_many_element_in_list_return_index_ragnge():
    res =  binary_search_range([1,2,2,2,3], 2)
    assert res == (1, 3)
def test_binary_search_range_all_element_similiar_return_index_range():1
    res =  binary_search_range([2,2,2], 2)
    assert res == (0, 2)
#номер 2 (не исправленный)
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
