#Available on Github


#To find the even numbers


def find_Even(x):
    x=raw_input("Type the Number");
    total=0;
    if (x==1):
        return x;
    
    for i in range(x+1):
        
        if (i%x==0):
            total+=1;
    return total;        

# over !--------------------------!

#To find the factors


def find_Prime(x):
    Prime_factors=[];
    x=raw_input("Type the Number");
    if (x==1):
        return x;
    
    for i in range(1,x+1):
        if x % i == 0:
            Prime_factors.append(i);
    return Prime_factors        
    
#over !----------------------------!




    
