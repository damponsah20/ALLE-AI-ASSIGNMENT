#pseudo-code
#1. Ask the name of the user - done
#2. Ask age of user - done
#3. check if age is less than 15 - done
#4. a. if age is less than 15, print eligible - done
#4. b. if age is more than 15, print not eligible
#5. always address user's name

user_name = input("What is your name? (e.g Jessica): ") #snake casing
userAge= input("How old are you? (e.g 12): ") #camel casing
userAge = int(userAge)

if(userAge < 15):
    #age is less than 15
    print(f'Hello {user_name}, you are eligible')
elif (userAge > 15):
    # age is more than 15
    print(f'Hello {user_name}, you are not eligible')
else:
    #age is not less than 15
    # age is not more than 15
    # means age is equal to 15
    print(f'Hello {user_name}, you are eligible')

print("Thank you!")

def Jackie(num1, num2, num3):
    ans = num1 + num2 + num3
    return ans

result = Jackie(1, 5, 9)
print(result)



num1 = "15" #string
num2 = 15 #int
num3 = '15' #string


