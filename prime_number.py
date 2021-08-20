# prime number
def input_data():
    while True:
        try:
            num = int(input("Enter a positive integer: "))
            if 0 < num < 2:
                print("Number {} is not prime".format(num))
                exit()
            elif num >= 2:
                return num
                break
            else:
                print("Input positive number please")
                print()
        except Exception:
            print("Input value shall be an integer, not a float or string")
            print()

def check_prime(number):
    count = 0
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            count += 1
    if count == 0:
        print("Number {} is prime".format(number))
    else:
        print("Number {} is not prime".format(number))

if __name__ == '__main__':
    number = input_data()
    check_prime(number)
            