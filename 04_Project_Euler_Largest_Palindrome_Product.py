def is_palindrome(num):
    return str(num)==str(num)[::-1]

largest_palindrome=0
for i in range(999,99,-1):
    for j in range(i,99,-1):
        product=i*j
        if product<largest_palindrome:
            break
        if is_palindrome(product):
          largest_palindrome=product
print(largest_palindrome)