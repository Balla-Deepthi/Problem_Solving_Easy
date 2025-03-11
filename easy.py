'''Create a function that takes two numbers as arguments and returns their sum.'''
def sum(a,b):
    return a+b
print(sum(20,30))
'''Write a function that takes an integer minutes and converts it to seconds.'''
def min_to_sec(a):
    return a*60
print(min_to_sec(5))
'''Create a function that takes a number as an argument, increments the number by +1 and returns the result.'''
def value_increment(a):
    return a+1
print(value_increment(6))
'''Create a function that takes the age in years and returns the age in days.'''
def years_to_days(age):
    return age*365
print(years_to_days(3))
'''sbi Create a function that takes voltage and current and returns the calculated power.'''
def power(voltage,current):
    return voltage*current
print(power(2,5))
'''Write a function that returns the string "something" joined with a space " " and the given argument a.'''
def joining(a):
    return "something"+" "+a
print(joining("is Fishy"))
'''Create a function that takes two arguments. Both arguments are integers, a and b. Return true if one of them is 10 or if their sum is 10.'''
def ten(a,b):
    if a==10 or b==10 or a+b==10:
     return True
    else:
       return False
print(ten(2,8))
'''Create a function that takes two strings as arguments and returns either true or false depending on whether the total number
 of characters in the first string is equal to the total number of characters in the second string.'''
def check_equal_string(string1,string2):
    if len(string1)==len(string2):
        return True
    else:
        return False
print(check_equal_string("Deepu","Pinky"))
'''Create a function that takes a name and returns a greeting in the form of a string.'''
def greeting(name):  
    return "Hello! Good Morning "+name
print(greeting("Deepthi"))
'''Create a function that takes an array of 10 numbers (between 0 and 9) and 
returns a string of those numbers formatted as a phone number (e.g. (555) 555-5555).'''
def phone_numbers(a):
     return "({}{}{}) {}{}{}-{}{}{}{}".format(*a)
    # return f"({a[8]}{a[1]}{a[3]}) {a[2]}{a[6]}{a[8]}-{a[5]}{a[7]}{a[5]}{a[7]}"
print(phone_numbers([0,1,2,3,4,5,6,7,8,9]))
'''Create a function that returns an array of strings sorted by length in ascending order.
Example:
sortByLength(["a", "ccc", "dddd", "bb"]) ➞ ["a", "bb", "ccc", "dddd"]
'''
def sortBylength(string):
    return sorted(string,key=len)
print(sortBylength(["acgdf","ab","abcd"]))
'''Create a function that takes an array of arrays with numbers. Return a new (single) array with the largest numbers of each.
Example:
findLargestNums([[4, 2, 7, 1], [20, 70, 40, 90], [1, 2, 0]]) ➞ [7, 90, 2]
'''
def Largest_num(array):
    for i in array:
        print(max(i))
Largest_num([[4, 2, 7, 1], [20, 70, 40, 90], [1, 2, 0]])
'''Create a function that takes an array of numbers and returns the second largest number.
Example:
secondLargest([10, 40, 30, 20, 50]) ➞ 40
'''
def Second_largest_number(array):
     array.remove(max(array))
     second_largest=max(array)
     return second_largest

print(Second_largest_number([10, 40, 30, 20, 50]))
'''Create a function that takes an array of items, removes all duplicate items and returns a new array in the same sequential order as the old array (minus duplicates).
Example:

removeDups([1, 0, 1, 0]) ➞ [1, 0]

removeDups(["The", "big", "cat"]) ➞ ["The", "big", "cat"]
'''
def removeDups(array):
    return list(dict.fromkeys(array))
print(removeDups([1,0,1,0]))
print(removeDups(["The", "big", "cat"]))
'''Create a function that takes an array of integers as an argument and returns a unique number 
from that array. All numbers except unique ones have the same number of occurrences in the array.

Example:

findSingleNumber([2, 2, 2, 3, 4, 4, 4]) ➞ 3
'''
def unique_number(array):
   
    for i in array:
        count=0
        for j in array:
            if i==j:
                count+=1
        if count==1:
          return i
print(unique_number([2,2,2,3,4,4,4]))
'''Create a function that takes two strings as arguments and returns the number of times the first string (the single character) is found in the second string.
Example:

charCount("c", "Chamber of secrets") ➞ 1'''
def charCount(string1,string2):
    count=0
    for i in range(0,len(string2)):
        if string1[0]==string2[i]:
            count+=1
    return count
print(charCount("c", "Chamber of secrets"))
'''Create a function that takes a string and returns the number (count) of vowels contained within it.
Example:

countVowels("Celebration") ➞ 5
'''
def countVowels(string):
    vowels="aeiouAEIOU"
    count=0
    for i in string:
        if i in vowels:
            count+=1
    return count
print(countVowels("Celebration"))
'''Given a string, create a function to reverse the case. All lower-cased letters should be upper-cased, and vice versa.
Example:
reverseCase("Happy Birthday") ➞ "hAPPY bIRTHDAY"
'''
def reverseCase(String):
    list=[]
    for i in String:
        if i==i.upper():
           list.append(i.lower())
        else:
           list.append(i.upper())
    return ''.join(list)
print(reverseCase("Happy Birthday"))
''' Take one integer n, loop till n and pass each value to a function, 
create a function that takes one integer parameter, and multiply with 2 in every integer.
			
			Input:      n=5
			Output:   2 4 6 8 10

			Explanation:  Loop start with 1 go till 5 bcoz n=5
					1 x 2 =2, 2 x 2=4, 3 x 2=6 …..etc '''
def multiply(n):
    for i in range(1,n+1):
        print( i*2)
multiply(6)
''' Create Function that will take one parameter and return type of the data.
			
			Input:       500
			Output:     Integer

			Input:       Coding
			Output:    String'''
def type_data(data):
      if type(data).__name__=="int":
           return "Integer"
      else:
            return "String'''"
print(type_data(500))
print(type_data("Coding"))
'''Program to find greatest of three numbers(using ternary operator).

			Input:  4 8 2
			Output: 8 is greatest'''
def graterNumber(a,b,c):
      return a if a>b and a>c else ( b if b>c else  c)
print(graterNumber(4,8,2))
'''C Program to find factorial of number.
		
			Input: n=5
			Output: 120

			Explanation: 5 x 4 x 3 x 2 x 1 = 120'''

def factorial(n):
    i=1
    fact=1
    while(i<=n):
        fact*=i
        i+=1
    return fact
print(factorial(5))
'''3. C Program to arrange numbers in ascending order
			Input: [2,3,1,5,4]
			Output: [1,2,3,4,5]

		        Sort the Array using loop only(you can not use predefined function).
                '''


def asscending_order(a):
    for i in range(0,len(a)):
        for j in range(i+1,len(a)):
            if a[i]>a[j]:
                a[i],a[j]=a[j],a[i]
    return a
    
print(asscending_order([2,3,1,5,4]))
'''Print Patter using loop.

			1
			1 2
			1 2 3
			1 2 3 4
  			1 2 3 4 5'''

def pattern(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end=" ")
        print()
pattern(5)
'''C Program to Calculate the Power of a Number(using loop only).

			Input: n=5, p=3
			Output: 5 ^ 3 = 125
			Explanation: 5 x 5 x 5 = 125'''
def Power(n,p):
    result=1
    while(p>0):
        result*=n
        p-=1
    return result
print(Power(5,3))
''' Program to Check Whether a Number is Prime or Not

			Input: 9
			Output: 9 is not a prime no

			Input: 7
			Output : 7 is a prime no
'''
def check_Prime(n):
    if n<2:
        return f"{n} is not a prime no"
    for i in range(2,n):
        if n%i==0:
            return f"{n} is not a prime no"
    return f"{n} is a prime no"
print(check_Prime(9))
print(check_Prime(7))
''' Program to find LCM of two numbers using while loop

			Input: 15 50
			Output: Lcm of 15 and 50 is 150.'''
def find_LCM(a,b):
    lcm=max(a,b)
    while True:
        if lcm%a==0 and lcm%b==0:
            return lcm
        lcm+=1
print(find_LCM(15,50))
'''Program to Display Characters from A to Z Using Loop with count.

			Output: A1 B2 C3 D4 E5 F6 ……. Z26 '''
def char_count(str):
    count=0
    list=[]
    for i in str:
        count+=1
        list.append(f"{i}{count}")
    return " ".join(list)
    
print(char_count("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
'''Program to find a missing number

			Input:  n=5(length of array), arr= [5,3,1,4]
			Output: 2 is missing

		Using loop only(you can not use predefined function)'''
def missing_Number(n,arr):
    for i in range(1,n+1):
        for j in arr:
            if i==j:
                break
        else:
            return f"{i} is missing"
print(missing_Number(5,[5,3,1,4]))
'''Program to count vowels and consonants in a given String.

			Input: i am ram
			Output: 3 vowels 3 consonants.'''
def count_alphabets(string):
    vowels="aeiou"
    consonants="bcdfghjklmnpqrstvwxyz"
    count1=0
    count2=0
    for i in string:
        if i in vowels:
            count1+=1
            
        elif i in consonants:
            count2+=1
            
    return f"{count1} vowels {count2} consonants"
print(count_alphabets("i am ram"))
''' program to insert  the elements of an array for specific index.

			Input: [1,2,3,4,5,7,8,9,10] , index=5
			Output: [1,2,3,4,5,6,78,9,10]'''
def element_index(arr,index):
    element=arr[index-1]+1
    arr.insert(index,element)
    return arr
print(element_index([1,2,3,4,5,7,8,9,10],5))
'''Reverse a number using while Loop

			Input: 123
			Output: 321'''
def reverse_num(n):
    rev_num=0
    while(n!=0):
        rem=n%10
        rev_num=rev_num*10+rem
        n=n//10
    return rev_num
print(reverse_num(123))
'''Count occurrence of number:

			Input: [1,6,3,1,5,9,7,2,1,9,3,7,8,9,10] , no find=7
			Output: 7 present 2 times.'''
def count_occurance(arr,n):
    count=0
    for i in arr:
        if i==n:
            count+=1
    return f"{n} present {count} times"
print(count_occurance([1,6,3,1,5,9,7,2,1,9,3,7,8,9,10],7))
      



            
        



        
    




        
    
    

    

    
