import math
try:
    for i in range(1, 10):
        for j in range(1, 10):
            print(i, '*', j, '=', i * j, end='\t\t')
        print()
except Exception as ex:
    print(f"error information:{ex}")
finally:
    print("exit")