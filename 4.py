def is_palindrome(s):
    rev = ''.join(reversed(s))
    if (s == rev):
        return True
    return False

input_teks = input("masukan teks: ").lower()
print(is_palindrome(input_teks))