try:
    a = int(input("enter num1"))
    if a == a:
        print("goodbay")

except Exception as ex:
    print(f"error information:{ex}")
finally:
    print("exit")