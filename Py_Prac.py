#Displaying numbers on 7 segment display - line 330
#Ceasar cipher, decryption and shift - line 362
#Palindrome checker - line 425
#Anagram checker - line 446
#Digit of Life - line 463
#Finding a word in a combination of mixed characters - line 486
#BMI Calculator in kg/m and lbs/ft/inches - line 498
#Compact Factorial and Fibonacci via Recursion - line 512
#Do 3 lengths form a triangle - line 530
#Right Triangle - line 551
#Prime Number Checker - line 569
#Identify Leap Year, Days in a Month, and Days in a Year - line 590
#Distance of 2 points on a Cartesian Plane / Perimeter of a Triangle - line 689

#---Displaying numbers on 7 segment display---
def display():
    try:    
        number = int(input("input non-negative integers only: "))
        list_1 = ['  # ','  # ','  # ','  # ','  # ']
        list_2 = ['### ','  # ','### ','#   ','### ']
        list_3 = ['### ','  # ','### ','  # ','### ']
        list_4 = ['# # ','# # ','### ','  # ','  # ']
        list_5 = ['### ','#   ','### ','  # ','### ']
        list_6 = ['### ','#   ','### ','# # ','### ']
        list_7 = ['### ','  # ','  # ','  # ','  # ']
        list_8 = ['### ','# # ','### ','# # ','### ']
        list_9 = ['### ','# # ','### ','  # ','### ']
        list_0 = ['### ','# # ','# # ','# # ','### ']
        d = {'1':list_1, '2':list_2, '3':list_3, '4':list_4, '5':list_5,
             '6':list_6, '7':list_7, '8':list_8, '9':list_9, '0':list_0}
        digits = ""
        if number >= 0:
            number = str(number)
            for x in range(5):
                for n in number:
                    List = d[n]
                    digits += List[x]
                digits += "\n"
            print(digits)
        else:
            display()
    except:
        display()
    
#display()

#---Ceasar cipher, decryption and shift---
# Caesar cipher.
def ceasar_encryption():
    text = input("Enter your message: ")
    cipher = ''
    for char in text:
        if not char.isalpha():
            continue
        char = char.upper()
        code = ord(char) + 1
        if code > ord('Z'):
            code = ord('A')
        cipher += chr(code)

    print(cipher)

# Caesar cipher - decrypting a message.
def ceasar_decrption():
    cipher = input('Enter your cryptogram: ')
    text = ''
    for char in cipher:
        if not char.isalpha():
            continue
        char = char.upper()
        code = ord(char) - 1
        if code < ord('A'):
            code = ord('Z')
        text += chr(code)

    print(text)

# Ceasar cipher - entering text and shift
def cipher_shift(text,shift):
    try:
        '''text = input("Enter your message: ")
        shift = int(input("Enter your shift value (1-25): "))'''
        c = ''
        if shift > 0 or shift < 26:
            for char in text:
                if char.isalpha():
                    code = ord(char) + shift
                    if code > 122 and ord(char) >= 97 and ord(char) <= 122:
                        code -= 26
                        c += chr(code)
                    elif code > 90 and ord(char) >= 65 and ord(char) <= 90:
                        code -= 26
                        c += chr(code)
                    else:
                        c += chr(code)
                else:
                    c += char
            print(c)
        else:
            cipher()
        
    except:
        cipher()

#ceasar_encryption()
#ceasar_decrption()
#cipher_shift('abc',5)
#cipher_shift('The die is cast',25)

#---Palindrome checker---
def is_palindrome(text):
    text = text.upper()
    forward = ''
    backward = []
    for char in text:
        if char.isalpha():
            forward += char
    for char in forward:
        backward.insert(0,char)
        b = ''.join(backward)
    if b == forward:
        print("It's a palindrome")
    else:
        print("It's not a palindrome")
        
#is_palindrome('Ten animals I slam in a net')
#is_palindrome('basketBALL')
#is_palindrome('raceCAR')
#is_palindrome('KAYak')

#---Anagram checker---
def anagram(text_1, text_2):
    text_1 = list(text_1.lower().replace(' ',''))
    text_2 = list(text_2.lower().replace(' ',''))
    for char in text_1:
        for elem in text_2:
            if elem == char:
                text_2.remove(elem)
                break
    if text_2 == []:
        print("It is an anagram!")
    else:
        print("It is not an anagram!")

#anagram("Listen",'Silent')
#anagram("anagram",'nag a ram')

#---Digit of Life---
def digit_of_life():
    birthday = input("Enter Birthday YYYYMMDD in intergers only: ")
    total = 0
    if len(birthday) == 8 and birthday.isnumeric():
        for b in birthday:
            total += int(b)
            digit = total
        if len(str(digit)) > 1:
            total = str(total)
            digit = 0
            for t in total:
                digit += int(t)
            print(digit)
        else:
            print(digit)

    else:
        print("input not long enough or you entered non-numeric input")
        digit_of_life()
        
#digit_of_life()

#---Finding a word in a combination of mixed characters---
def is_word_found(word, mixed_characters):
    word = word.lower()
    mixed_characters = mixed_characters.lower()
    for w in word:
        x = mixed_characters.find(w)
        if x == -1:
            return print("No")
    return print("Yes")
            
#is_word_found('Congratz','tZawG2icONera')

#---BMI Calculator in kg/m and lbs/ft/inches---
def ft_and_inch_to_m(ft, inch = 0.0):
    return ft * 0.3048 + inch * 0.0254

def lb_to_kg(lb):
    return lb * 0.45359237

def bmi(weight, height):
    if height < 1.0 or height > 2.5 or weight < 20 or weight > 200:
        return None
    return weight / height ** 2

#print(bmi(weight = lb_to_kg(176), height = ft_and_inch_to_m(5, 7)))

#---Compact Factorial and Fibonacci via Recursion---
def fib(n):
    if n < 1:           
        return None
    if n < 3:           
        return 1
    return fib(n - 1) + fib(n - 2)

def fac(n):
    if n < 0:           
        return None
    if n < 2:           
        return 1
    return n * fac(n - 1)

#print(fib(20))
#print(fac(8))

#---Do 3 lengths form a triangle---
def triangle(a, b, c):
    if a + b <= c:
        return False
    if b + c <= a:
        return False
    if c + a <= b:
        return False
    return True
        #   VERSUS
def triangle(a, b, c):
    if a + b <= c or b + c <= a or c + a <= b:
        return False
    return True
        #   VERSUS  (most compact code)
def triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b

#print(triangle(1, 1, 1))
#print(triangle(1, 1, 3))

#---Right Triangle---
#   NOTE: error in calculation when sqrt and exponentiation
#   (   2 != (2**0.5)**2    )
def right_triangle(a, b, c):
    if not triangle(a, b, c):
        return False
    if c > a and c > b:
        return round(c ** 2,5) == a ** 2 + b ** 2
    if a > b and a > c:
        return round(a ** 2,5) == b ** 2 + c ** 2
    else:
        return round(b ** 2,5) == a ** 2 + c ** 2

#print(right_triangle(3,4,5))
#print(right_triangle(3,18**0.5,3))
#print(right_triangle(2**0.5,1,1))
#print('2 =',2,'\n2**0.5 =', 2**0.5, '\n(2**0.5)**2 =', (2**0.5)**2)

#---Prime Number Checker---
def prime(num):
    P = 0
    N = num
    if num > 0:
        while N > 0:
            if num % N == 0:
                P += 1
                N -= 1
            else:
                N -= 1
        if P == 2:
            return True
        else:
            return False
'''
for i in range(1, 20):
    if prime(i + 1):
        print(i + 1, end=" ")
'''

#---Identify Leap Year, Days in a Month, and Days in a Year---
#FINDING LEAP YEAR USING DEFINED FUNCTION, WITH TEST DATA AND RESULTS
def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True
'''
test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]

for i in range(len(test_data)):
	yr = test_data[i]
	print(yr,"--> ",end="")
	result = is_year_leap(yr)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")
'''
#FINDING DAYS IN MONTH IF LEAP OR COMMON YEAR
def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def days_in_month(year, month):
    if month in (1,3,5,7,8,10,12):
        return 31
    elif month in (4,6,9,11):
        return 30
    elif month == 2:
        if is_year_leap(year) == True:
            return 29
        else:
            return 28
'''   
test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]

for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "--> ", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")
'''
#GIVEN INPUT YEAR, MON, DAY. RETURN NUMBER OF DAYS IN THAT YEAR
def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def days_in_month(year, month):
    if month in (1,3,5,7,8,10,12):
        return 31
    elif month in (4,6,9,11):
        return 30
    elif month == 2:
        if is_year_leap(year) == True:
            return 29
        else:
            return 28

def day_of_year(year, month, day):
    D = 0
    M = 1
    if is_year_leap(year) == True:
        while M < month:
            D += days_in_month(year, M)
            M += 1
        D += day
    else:
        while M < month:
            D += days_in_month(year, M)
            M += 1
        D += day
    return D

#print(day_of_year(2000, 12, 31))

#---Distance of 2 points on a Cartesian Plane / Perimeter of a Triangle---
import math

class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_xy(self, x, y):
        x = x - self.__x
        y = y - self.__y
        return math.hypot(x,y)

    def distance_from_point(self, point):
        x = self.getx() - point.getx()
        y = self.gety() - point.gety()
        return math.hypot(x,y)

class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.__points = [vertice1, vertice2, vertice3]

    def perimeter(self):
        a = self.__points[0].distance_from_point(self.__points[1])
        b = self.__points[1].distance_from_point(self.__points[2])
        c = self.__points[2].distance_from_point(self.__points[0])
        return a + b + c
'''
point1 = Point(0, 0)
point2 = Point(1, 1)
print(point1.distance_from_point(point2))
print(point2.distance_from_xy(2, 0))
print(point2.distance_from_xy(2, 3))
print('------Triangle Perimeter-------')
triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())
'''




