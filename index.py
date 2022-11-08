from art import logo

print(logo)

def calculator():

  first_num = float(input("What's the first number?: "))

  operations = ["+", "-", "*", "/"]

  for operation in operations:
    print(operation)

  continue_calc = 'y'

  def evaluate(first_num, second_num):
    if operation == "+":
      return add(first_num, second_num)
    elif operation == "-":  
      return subtract(first_num, second_num)
    elif operation == "*":  
      return multiply(first_num, second_num)
    elif operation == "/":  
      return divide(first_num, second_num)
    else:
      return None

  total = 0

  def add(num1, num2):
    global total 
    total = num1 + num2
    return total

  def subtract(num1, num2):
    global total 
    total = num1 - num2
    return total

  def multiply(num1, num2):
    global total 
    total = num1 * num2
    return total

  def divide(num1, num2):
    global total
    total = num1 / num2
    return total

  last_total = 0

  while continue_calc == 'y':
    last_total = total
    operation = input("Pick an operation: ")
    second_num = float(input("What's the next number? "))
    if total != 0:
      result = evaluate(total, second_num)
      if result == None:
        print("Invalid operation entered")
      print(f"{last_total} {operation} {second_num} = {result}")
    else:
      result = evaluate(first_num, second_num)
      if result == None:
        print("Invalid operation entered")
      print(f"{first_num} {operation} {second_num} = {result}")
  
    continue_calc = input(f"Type 'y' to continue calculating with {last_total}, or type 'n' to start a new calculation: ")

  calculator()

calculator()