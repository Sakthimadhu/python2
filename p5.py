x=['a','e','i','o','u','A','E','I','O','U']
a=input()
if a.isalpha():
    if a in x:
        print('Vowel')
    else:
        print('Consonant')
else:
    print('invalid')
