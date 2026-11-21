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
    skobki = {')':'(', ']':'[', '}':'{'}
    ochered = []
    for i in s:
        if i in skobki.values():
            ochered.append(i)
        elif i in skobki:
            if ochered and (ochered[-1] == skobki[i]):
                ochered.pop(-1)
            else: return False
        else: continue
    if not ochered: return True
    else: return False 
    
def test_is_balanced_brackets_empty_str_return_True():
    res = is_balanced_brackets('')
    assert res == True
def test_is_balanced_brackets_skobki_without_pair_return_False():
    res = is_balanced_brackets('(]')
    assert res == False
def test_is_balanced_brackets_skobki_with_near_pair_return_True():
    res = is_balanced_brackets('()[]{}')
    assert res == True
def test_is_balanced_brackets_skobki_with_far_pair_return_True():
    res = is_balanced_brackets('([{}])')
    assert res == True
def test_is_balanced_brackets_skobki_with_trash_return_True():
    res = is_balanced_brackets('a(b)c')
    assert res == True
