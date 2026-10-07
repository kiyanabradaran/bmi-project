
user_name = input('enter your name')
user_weight =float(input('enter your weight'))
user_height =float(input('enter your height in meter'))
bmi = user_weight/(user_height**2)
# چون میخوایم فقط تا دو رقم اعشار نشون بده پس از تابغ اف استفاده میکنیم 
print('BMI:',f'{bmi:.2f}')
if bmi <= 18.5 :
    print ('kamboode vazn')
elif 18.5< bmi <= 25 :
    print('normal')
elif 25< bmi <= 30 :
    print ('ezafe vazn')
elif 30< bmi <= 35:
    print('chagi darje 1')
else :
    print ('chagi darje 2')