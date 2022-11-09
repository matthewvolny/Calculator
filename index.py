from art import logo

print(logo)

def calculator():
  
  total = float(input("What's the first number?: "))

  operations = ["+", "-", "*", "/"]

  for operation in operations:
    print(operation)

  continue_calc = 'y'

  def evaluate(total, second_num):
    if operation == "+":
      return add(total, second_num)
    elif operation == "-":  
      return subtract(total, second_num)
    elif operation == "*":  
      return multiply(total, second_num)
    elif operation == "/":  
      return divide(total, second_num)
    else:
      return None

  def add(num1, num2):
    value = num1 + num2
    return value

  def subtract(num1, num2):
    value = num1 - num2
    return value

  def multiply(num1, num2):
    value = num1 * num2
    return value

  def divide(num1, num2):
    # global total
    value = num1 / num2
    return value
  
  while continue_calc == 'y':
    operation = input("Pick an operation: ")
    second_num = float(input("What's the next number? "))
    result = evaluate(total, second_num)
    if result == None:
      print("Invalid operation entered")
    print(f"{total} {operation} {second_num} = {result}")
    total = result
  
    continue_calc = input(f"Type 'y' to continue calculating with {total}, or type 'n' to start a new calculation: ")

  calculator()

calculator()