#Available on Github


#To find the even numbers

def find_Even(x):
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
    if (x==1):
        return x;
    
    for i in range(1,x+1):
        if x % i == 0:
            Prime_factors.append(i);
    return Prime_factors        
    
#over !----------------------------!

#Lets test it
print(find_Even(4));
print (find_Prime(4));



    