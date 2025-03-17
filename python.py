 print("hello world")
string = input("enter a string :")
print(len(string))
string=input("enter any srting").replace(" ","")
print(len(string))
words=[]
for i in range(5):
    word = input(f"Enter word {i+1}: ")
    words.append(word)
    print("\nWord Lengths:")
for word in words:
    print(f"'{word}' is {len(word)} characters")
arr1 = ['a', 'i', 'o', 'e', 'u']
arr2 = ['k', 'j', 'p', 't', 'f']

# Function to replace characters based on arr1 and arr2
def kajipo(text):
    result = []
    for char in text:
        if char in arr1:
            index = arr1.index(char)
            result.append(arr2[index])
        elif char in arr2:
            index = arr2.index(char)
            result.append(arr1[index])
        else:
            result.append(char)
    return ''.join(result)

# Get user input
user_input = input("Enter text: ")

# Replace characters in the user input
result = kajipo(user_input)

print("Updated text:", result)
