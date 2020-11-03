age = int(input('Please enter your age: ')) 
resident_years = int(input('How long have you been a US resident for: ')) 
naturalBorn = bool(input('are you a natural us citizen: ')) 
if age>=25 and resident_years>=14 and naturalBorn:
    print('You are preisdent')
    
