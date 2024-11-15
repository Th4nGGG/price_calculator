import math

def round_up(output):
    output = math.ceil(output * 10) / 10.0
    return output

def calculate_output(a, b, c):
    if b is None:  # If b is not provided, use default value of 1 (or other logic you prefer)
        b = 1
    output = a/b
    if output < 3:
        output *= 1.5
    else:
        output *= 1.4
    if c == '+':
        output *= 1.1
    return round_up(output)

while True:
    inputs = input("Enter price, quantity and GST as + separated by spaces (or 'quit' to exit). Only price is necessary: ").split()

    if inputs[0].lower() == 'quit':
        print("Exiting...")
        break

    if len(inputs) < 1 or len(inputs) > 3:
        print("Invalid number of inputs. Please enter price, quantity and GST separated by spaces.")
    else:
        try:
            a = float(inputs[0])
            b = float(inputs[1]) if len(inputs) > 1 else None
            c = inputs[2] if len(inputs) > 2 else None

            if c not in ['+', None]:
                print("Invalid input for 'c'. It should be '+' or left blank.")
            else:
                output = calculate_output(a, b, c)
                print("Price:", output)
        except ValueError:
            print("Invalid input. Please enter numeric values for 'a' and 'b'.")

print("Exited.")
