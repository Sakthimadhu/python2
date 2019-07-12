x1=input()
if((x1>='a' and x1<='z') or (x1>='A' and x1<='Z')):
  x1=x1.lower()
  if(x1=='a' or x1=='e' or x1=='i' or x1=='o' or x1=='u'):
     print("Vowel")
  else:
     print("Consonant")
else:
    print("Special Characters")
    
