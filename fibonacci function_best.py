def fibonacci(n):
    f1, f2 = 1, 1
    n_condition = ['false']
    zero_condition = ['false']
    
    while zero_condition == ['false']:
        
        if n <=0:
            n = int(input('please enter an integer greater than zero \n\n'))
            
            
        else:
            zero_condition = ['true']
            
    while n_condition == ['false']:
        
        if n == 1:
            break
        
        else:
            n_condition = ['true']
    
    for i in range(n):
        print('\n',f1)
        fnext = f1 + f2
        f1 = f2
        f2 = fnext
        

n = int(input('please enter the fibonacci term you would like to print\n\n'))

fibonacci(n)