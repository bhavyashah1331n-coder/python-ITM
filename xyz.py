start=int(input("Enter start:"))
stop=int(input("Enter stop:"))
for outer in range(start,stop+1):
    for inner in range(1,11):
        print(f"{outer}x{inner}={outer*inner}")
              
    
