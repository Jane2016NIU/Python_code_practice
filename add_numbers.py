def sum_numbers(numbers=None):
    result = 0
    if(numbers == None):
        
        for i in range(1,101):
            result += i
        return result
        
    for i in numbers:
        result += i
    return result

if __name__ == "__main__":

	num = [1, 2, 3, 4]

	print(num)

	print (sum_numbers(num))


	print (sum_numbers())
