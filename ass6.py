def perfect_number(n):
    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum += x
    return sum == n
k=int(input("Write a number : "))
print(perfect_number(k))

def palindrome(s):
 f_s = s.split()
 s_s = s[::-1].split()
 if ''.join(f_s) == ''.join(s_s):
    return 'YES, its palindrome'
 else:
   return 'NO, its not palindrome'

print(palindrome(input()))
def pascal_triangle(n):
   trow = [1]
   y = [0]
   for x in range(max(n,0)):
      print(trow)
      trow=[l+r for l,r in zip(trow+y, y+trow)]
   return n>=1
pascal_triangle(6)

from http.client import FOUND
import string
def ispangram(sentence, alphabet=string.ascii_lowercase):
    return set(alphabet) <= set(sentence.lower())
print(ispangram(input('Sentence: ')))
items=[n for n in input().split('-')]
items.sort()
print('-'.join(items))
def student_data(student_id, **kwargs):
    print(f'\nStudent ID: {student_id}')
    if 'student_name' in kwargs:
        print(f"Student Name: $ {kwargs['student_name']}")

    if 'student_name' and 'student_class' in kwargs:
        print(f"\nStudent Name: $ {kwargs['student_name']}")
        print(f"Student Class: $ {kwargs['student_class']}")


student_data(student_id='PEC12', student_name='Ian Bell')

student_data(student_id='PEC12', student_name='Ian Bell', student_class ='V')
class Student:
    pass
class Marks:
    pass
student1 = Student()
marks1 = Marks()
print(isinstance(student1, Student))
print(isinstance(marks1, Student))
print(isinstance(marks1, Marks))
print(isinstance(student1, Marks))
print("\nCheck whether the said classes are subclasses of the built-in object class or not")
print(issubclass(Student, object))
print(issubclass(Marks, object))



def findTriplets(arr, n):
    
    found = True
    for i in range(0, n-2):

        for j in range(i+1, n-1):

            for k in range(j+1, n):
                
                if (arr[i] + arr[j] + arr[k] == 0):
                    print(arr[i], arr[j], arr[k])
                    found = True


    # If no triplet with 0 sum
    # found in array

    if (found == False):
        print(" not exist ")

arr = [-25, -10, -7, -3, 2, 4, 8, 10]
n = len(arr)
findTriplets(arr, n)
class validity:
    
    def f(str):

        a= ['()', '{}', '[]']
        
        while any(i in str for i in a):

            for j in a:

                str = str.replace(j, '')

        return not str

s = input("enter : ")

print(s, "-", "is balanced"

      if validity.f(s) else "is Unbalanced")
