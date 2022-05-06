r=[]
n=0
while n<31:  #تعداد روز های ماهی که قرار است  مشاوره بدهد
    print('r=',r)
    date=int(input('enter a date :[1,30]'))

    if date<1 or date>30:
        print('error')
        continue
    elif date in r:
        print('error')
        continue
    else:
        print('enter your information')
        fname=input('first name:')
        lname=input('last name:')
        print(fname,lname,'was booked for you on',date)
        r.append(date)
        n=n+1
