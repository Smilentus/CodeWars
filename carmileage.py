# My implementation
def toArr(number):
    numArr = []
    while number > 0:
        numArr.append(number % 10)
        number = number // 10
    numArr = numArr[::-1]
    return numArr
    
def isZeros(numArr):
    if len(numArr) > 2:
        for c in numArr[1:]:
            if c != 0:
                return False
        return True
    else:
        return False
    
def isBig(numArr):
    if len(numArr) > 2:
        for c in range(1, len(numArr)):
            if numArr[c] != numArr[c - 1]:
                return False
        return True
    else:
        return False
    
def isDecr(numArr):
    if len(numArr) > 2:
        for c in range(1, len(numArr)):
            n = numArr[c] - numArr[c - 1]
            if numArr[c] == 9 and numArr[c - 1] == 0:
                return False
            if n != -1 and n != 9:
                return False
        return True
    else:
        return False
    
def isIncr(numArr):
    if len(numArr) > 2:
        for c in range(1, len(numArr)):
            n = numArr[c - 1] - numArr[c]
            if numArr[c] == 0 and numArr[c - 1] == 1:
                return False
            if n != -1 and n != 9:
                return False
        return True
    else:
        return False

def isPal(numArr):
    if len(numArr) > 2:
        for i in range(len(numArr)//2):
            if numArr[i] != numArr[-1-i]:
                return False
        return True
    else:
        return False
    
def is_interesting(number, awesome_phrases):
    if number < 98:
        return 0

    # Проверяем на интересные фразы
    for n in awesome_phrases:
        if number == n:
            return 2
            
    # Преобразуем в массив
    numArr = toArr(number)
    
    # Проверка на нули
    # Проверка на одинаковые числа
    # Повышающиеся цифры
    # Понижающиеся цифры
    # Палиндромы
    if isZeros(numArr) or isBig(numArr) or isDecr(numArr) or isIncr(numArr) or isPal(numArr):
        return 2
            
    # Близкие значения
    for c in (-2, -1, 1, 2):
        num = toArr(number + c)
        for n in awesome_phrases:
            if number + c == n:
                return 1
        if isZeros(num) or isBig(num) or isDecr(num) or isIncr(num) or isPal(num):
            return 1
    
    return 0


# Best Solution
def is_incrementing(number): return str(number) in '1234567890'
def is_decrementing(number): return str(number) in '9876543210'
def is_palindrome(number):   return str(number) == str(number)[::-1]
def is_round(number):        return set(str(number)[1:]) == set('0')

def is_interesting(number, awesome_phrases):
    tests = (is_round, is_incrementing, is_decrementing,
             is_palindrome, awesome_phrases.__contains__)
       
    for num, color in zip(range(number, number+3), (2, 1, 1)):
        if num >= 100 and any(test(num) for test in tests):
            return color
    return 0