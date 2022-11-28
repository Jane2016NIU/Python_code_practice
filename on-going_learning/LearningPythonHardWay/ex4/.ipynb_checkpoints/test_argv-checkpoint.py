import sys
print("I like arguments!")

print("There are: ", len(sys.argv), "arguments!")

for i in sys.argv:
    print(i)
    
print("This is the script name: ", sys.argv[0])