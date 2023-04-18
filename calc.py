#perform simple unpacking
def compute(expression):
    num0, operator, num1 = expression.split(' ')
num0, num = int(num), int(num0)   
    if operator == '+':
        return num0 + num1
    elif operator == '-':
        return num0 - num1
    elif operator == '*':
        return num0 * num1
    elif operator == '/':
        return num0 / num1
    else:
        print('unknown operator!')
        return None