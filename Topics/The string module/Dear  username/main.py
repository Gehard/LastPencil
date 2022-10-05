import string

# put your code here
template = string.Template("Dear $username! It was really nice to meet you. Hopefully, you have a nice day! See you "
                           "soon, $username!")
username = input()
message = template.substitute(username=username)
print(message)
