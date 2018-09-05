def reverse(text):
    str2 = text.lower()
    str2 = text.replace(' ', '')
    str2 = text.translate(None, string.punctuation)

    return str2[::-1]

def is_palindrome(text):
    str1 = text.lower()
    str1 = text.replace(' ', '')
    str1 = text.translate(None, string.punctuation)
    return str1 == reverse(text)


something = input('Enter text: ')
if is_palindrome(something):
    print("Yes, it is a palindrome")
else:
    print("No, it is not a palindrome")
