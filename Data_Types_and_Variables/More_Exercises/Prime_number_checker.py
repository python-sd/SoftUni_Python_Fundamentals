number = int(input())
is_prime = True
for num in range(2, number):
    if number % num == 0:
        print("False")
        is_prime = False
        break
if is_prime:
    print("True")