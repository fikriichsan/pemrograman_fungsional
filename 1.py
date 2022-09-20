def sum_square(l):
    list = l.split()
    for i in range(len(list)):
        list[i] = int(list[i])
    return sum(map(lambda x:x*x, list))

input_list = input('masukan input dipisah dengan spasi : ')
print(sum_square(input_list))
