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

  # total = 0
  

  def add(num1, num2):
    # global total 
    value = num1 + num2
    return value

  def subtract(num1, num2):
    # global total 
    value = num1 - num2
    return value

  def multiply(num1, num2):
    # global total 
    value = num1 * num2
    return value

  def divide(num1, num2):
    # global total
    value = num1 / num2
    return value

  # last_total = 0
  
  while continue_calc == 'y':
    # print(total)
    # print(last_total)
    operation = input("Pick an operation: ")
    second_num = float(input("What's the next number? "))
    result = evaluate(total, second_num)
    if result == None:
      print("Invalid operation entered")
    # global last_total  
    # last_total = result
    print(f"{total} {operation} {second_num} = {result}")
    # global total
    total = result
    # if last_total != 0:
    #   result = evaluate(total, second_num)
    #   if result == None:
    #     print("Invalid operation entered")
    #   last_total = result
    #   print(f"{last_total} {operation} {second_num} = {result}")
    # else:
    #   result = evaluate(first_num, second_num)
    #   if result == None:
    #     print("Invalid operation entered")
    #   last_total = result
    #   print(f"{first_num} {operation} {second_num} = {result}")
  
    continue_calc = input(f"Type 'y' to continue calculating with {total}, or type 'n' to start a new calculation: ")

  calculator()

calculator()