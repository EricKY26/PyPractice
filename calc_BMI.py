def input_data():
    name = input('\nWhat\'s your name?\n')
    age_s = input('\nAnd how old are you?\n')
    height_s = input('\nPlease tell me your height. (In meters)\n')
    weight_s = input('\nAnd now please tell me your weight. (In Kilograms)\n')
    return name, age_s, height_s, weight_s


def calc_BMI(age_s, height_s, weight_s):
    age = int(age_s)
    height = float(height_s)
    weight = float(weight_s)
    BMI = weight/height**2
    if BMI < 18.5:
        tip_BMI = 'too thin'
    elif BMI >= 18.5 and BMI < 25:
        tip_BMI = 'normal'
    elif BMI >= 25 and BMI < 28:
        tip_BMI = 'a little over-weight'
    elif BMI >= 28 and BMI < 32:
        tip_BMI = 'fat'
    else:
        tip_BMI = 'too fat'
    return BMI, age, tip_BMI


def output_age_BMI():
    if age >= 18:
        print('\nHello %s. You are an adult. \nAnd your BMI is %.2f. You are %s. \n' % (
            name, BMI, tip_BMI))
    elif age >= 7:
        print('\nHello %s. You are a teenager. \nAnd your BMI is %.2f. You are %s. \n' % (
            name, BMI, tip_BMI))
    else:
        print('\nHello %s. You are a child. \nAnd your BMI is %.2f. You are %s. \n' % (
            name, BMI, tip_BMI))


choice = 1
while choice == 1:
    choice = int(input(r'''
Please choose what you wanna do next: 
1. Calculate your BMI. 
2. Exit

'''))
    if choice == 2:
        break
    name, age_s, height_s, weight_s = input_data()

    BMI, age, tip_BMI = calc_BMI(age_s, height_s, weight_s)

    output_age_BMI()
