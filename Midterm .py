def sum_of_even_numbers(numbers):
       
    even_sum = 0
    
    
    for num in numbers:
        
        if num % 2 == 0:
            even_sum += num  
            
    return even_sum  


numbers_list = [1, 2, 3, 4, 5, 6]
result = sum_of_even_numbers(numbers_list)
print("The sum of even numbers is:", result)
