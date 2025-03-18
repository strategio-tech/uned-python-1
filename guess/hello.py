
def main():
    requested_hellos=int(input(
        "How many hellos would you like? "
    ))
    say_hello(requested_hellos)

def say_hello(times):
    number = 0
    [0, 1, 2]
    # at least 1 time
    if times <= 0:
        print("Howdy")
    elif times > 5:
        print("Hello\n" * 5)
    else:
        while number < times:
            print("Hello")
            number += 1

main()


