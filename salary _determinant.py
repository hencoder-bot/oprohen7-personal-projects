name = input('What is your name: ' )
possition = ('What is your possision at PROJUICE COCKTAIL: ')
print(str(name) + str(' You are welcome') + '\n' + str(possition))
print('PROJUCE COCKTAIL\nYou are most welcome our blessed employee of PROJUICE COCKTAIL\nPlease consider us paying you awage /hour\nThe wage may not appear as prommised coz of several terms like , taxes, NSSF,\nWe will fire and burn lazy workers and we will be willing to prompte the hardworking employees\nFrom The Directors Office')
hourlypay1 = 5000
totol_hours= 8
hourlypay2 = hourlypay1 * totol_hours
print('Projucie Cocktail will pay you '+ str(hourlypay1  ) + ' per hour' +' which is equivalent ' + str(hourlypay2  ) + ' per day')
daypay1 = int(input('Enter number of days you worked:  '))
daypay2 = hourlypay2 * daypay1
print(daypay2)
print('Your Total earnings is ' + str(daypay2)+'\n' + 'Dont give up we are abaut to reach your Actual Salary.\nWe regret for any inconviniences')
Gov_tax=((10/100)* daypay2)
NSSF = ((5/100)*daypay2)
Deductions = (Gov_tax + NSSF)
print('We shall deduct 10% from your salary  to catter for Government Tax giving you a Total of = ' + str(Gov_tax))
print('We shall as well deduct 5% from your salary to catter for the NSSF savings  giving you a Total of = ' + str(NSSF))
Monthly_salary = (daypay2 - Deductions)
print('Your Monthly Salary is ' + str(Monthly_salary) +'\n' + 'THANKS FOR BEING PATIENT')
print( 'Dear '+str(name) + ' your salary is ' + str(Monthly_salary) + ' Check the comment of our Management below')
if daypay1 >=25 and  daypay1 <=30:
    print('You are hardworking employee')
elif daypay1 >=6 and daypay1 <= 15:
 print('You are a lazy employee')
elif daypay1 >=2 and daypay1 <= 5:
  print('You are fired')
else:
  print('You are an intruder')