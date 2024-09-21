def si(p,r,t):
    cal = (p*r*t)/100
    return cal
principal = int(input("Enter the principal: "))
Rate = float(input("Enter the rate: "))
time = int(input("Enter the time: "))
c =si(principal,Rate,time)
print(f"Your simple interest is {c}")