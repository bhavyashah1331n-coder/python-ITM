ch=input("Enter the alphabet:")
if ch.isalpha():
    if ch in 'aeiouAEIOU':
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Invalid choice!")
