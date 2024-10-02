class IOstring():
    def __init__ (self): 
        self.str1= ""
    def gets_string(self):
        self.str1 = input("Enter string: ")
    def print_string(self):
        print("result is", self.str1.upper())
obj = IOstring()
obj.gets_string()
obj.print_string()
