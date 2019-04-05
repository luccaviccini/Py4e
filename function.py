def computepay(h,r):
    if h <= 40:
        pay = h*r
        return pay
    else:
        extra_hrs = h-40
        regular_pay = 40*r
        extra_pay = (extra_hrs)*1.5*r
        pay = regular_pay + extra_pay
        return pay

hrs = input('Enter number of hours: ')
h = float(hrs)
rate = input('Enter rate: ')
r = float(rate)

pay = computepay(h,r)
print(pay)

