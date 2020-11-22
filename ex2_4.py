def fibonacci(n):
    if n<= 2:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)

    for i in range (1,n+1):
        print (fibonacci(i), end= ' ')
