def myFunc():
    print("Hello from module.py")

if __name__ == "__main__":
    # If this code is executed by running the file its present in
    print("We are directly running this code")
    myFunc()
    print(__name__)
