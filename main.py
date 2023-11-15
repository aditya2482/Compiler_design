import basic


while (True):
    text = input("aditya_compiler>")
    final,error = basic.run(text)
    if error:print(error.as_string())
    else:
        print(final)

