def triangular(i):
    if i < 2:
        return 1
    else:
        return i + triangular(i-1)
        
input_triangular = int(input("Masukkan bilangan : "))
print(triangular(input_triangular))