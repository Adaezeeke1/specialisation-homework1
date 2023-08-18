# Recursive solution:
def num_in_seq_r(n):
    if n < 1:
        return None

    if n == 1:
        return 8
    else:
        return num_in_seq_r(n - 1) + 7


print(num_in_seq_r(1))
print(num_in_seq_r(5))
print(num_in_seq_r(10))


# Non-recursive solution:
def num_in_seq_nr(n):
    if n < 1:
        return None

    first_num = 8
    difference = 7
    nth_num = first_num + (n - 1) * difference
    return nth_num


print(num_in_seq_nr(1))
print(num_in_seq_nr(2))
print(num_in_seq_nr(3))
