def solution(my_string, is_suffix):
    a = len(is_suffix)
    if my_string[-a:] == is_suffix:
        return 1
    else:
        return 0