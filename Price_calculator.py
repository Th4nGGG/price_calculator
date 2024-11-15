
def round_up(output):
    decimal = int((output*100) % 10)
    print(decimal)
    if decimal != 0:
        output += 0.05
        output = round(output, 1)
        return(output)
       
    
def calculate_price(a,b,c):
    if a/b < 3:
        output = a/b * 1.5
    else:
        output = a/b * 1.4
    if c == "+":
        output *= 1.1
    else:
        print("Incorrect input for GST, please try again")
    return round_up(output)

while True:
    a,b,c = input("Enter Unit price, Quantity and GST (+ for YES, leave blank for NO), separated by spaces: ").split()
    a = float(a)      
    b = float(b)       
    c = str(c) 
    print("Price: ", calculate_price(a,b,c))