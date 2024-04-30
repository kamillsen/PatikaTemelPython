def reverse_list(lst):
    reversed_list = []
    for item in reversed(lst):
        if isinstance(item, list):
            reversed_list.append(reverse_list(item))
        else:
            reversed_list.append(item)
    return reversed_list

# Örnek giriş
input_list = [[1, 2], [3, 4], [5, 6, 7]]
output_list = reverse_list(input_list)
print(output_list)
