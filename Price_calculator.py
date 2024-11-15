
import math

def round_up(output):
    decimal = int((output*100) % 10)
    if decimal != 0:
        output += 0.05
        output = round(output, 1)
        return(output)

def calculate_output(a, b=None, c=None):
    if b is not None:
        a /= b
    if a < 3:
        output = a * 1.5
    else:
        output = a * 1.4
    if c == '+':
        output *= 1.1
    return round_up(output)

while True:
    inputs = input("Enter price, quantity, and GST as + separated by spaces (or 'quit' to exit). Only price is necessary: ").split()

    if inputs[0].lower() == 'quit':
        print("Exiting...")
        break

    if len(inputs) < 1 or len(inputs) > 3:
        print("Invalid number of inputs. Please enter a, b, and c separated by spaces.")
    else:
        try:
            a = float(inputs[0])
            b = float(inputs[1]) if len(inputs) > 1 else None
            c = inputs[2] if len(inputs) > 2 else None

            if c not in ['+', None]:
                print("Invalid input for 'c'. It should be '+' or left blank.")
            else:
                result = calculate_output(a, b, c)
                print("Price:", result)
        except ValueError:
            print("Invalid input. Please enter numeric values for 'a' and 'b'.")

print("Exited.")
