# print(__name__)
def fun1():
    print("this is fun1")

if __name__ == "__main__":
    print("this is Internal call")
    def fun2():
        print("this is fun2")
else:
    print("this is External call")
    def fun3():
        print("this is fun3")
