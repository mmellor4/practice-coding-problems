def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    reversed_str = ""
    int_as_str = str(x)
    for i in range(len(int_as_str)-1, -1, -1):
        current = int_as_str[i]
        if current == '-':
            reversed_str = '-' + reversed_str
        else:
            reversed_str = reversed_str + current

    ret_val = int(reversed_str)

    if ret_val > pow(2,31) - 1:
        return 0
    if ret_val < -1 * pow(2,31):
        return 0

    return ret_val


print(reverse(-123))
