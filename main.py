from sympy import *
x = symbols('x',positve=True)




def taylor(ebarat,noghte,deghat):
    if noghte==0:
        print('بدلیل آنکه نقطه داده شده صفر است بسط مکلورن است')
    else:
        print('بدلیل آنکه نقطه داده شده صفر نیست بسط تیلور است')
    result = ebarat.subs(x, noghte)
    for i in range(1,deghat):
        result += diff(ebarat, x, i).subs(x, noghte) * ((x - noghte) ** i) / factorial(i)
    print(':عبارت حاصل شده از سری')
    pretty_print(result)
    print(':عدد حاصل شده از سری(جاگذاری x در عبارت بالا با نقطه)')
    print(float(result.subs(x,noghte)))
    print(':عدد حاصل شده از عبارت')
    print(float(ebarat.subs(x,noghte)))

    plot(result,ebarat)

expression=input('عبارت را وارد کنید')
loc=int(input('نقطه مورد نظر را وارد کنید'))
accuracy=int(input('دقت را وارد کنید'))
taylor(eval(expression),loc,accuracy)



# سری فوریه


# def fourier(ebarat,start,end):
#     l=(end-start)/2
#     sum=0
#     a0=(1/l)*(integrate(ebarat,(x,-l,l)))
#     sum+=a0/2
#
#     for n in range(1,50):
#         an=(1/l)*( (integrate(ebarat*cos(n*pi*x/l)).subs(x,l)) - (integrate(ebarat*cos(n*pi*x/l)).subs(x,-l)))
#         bn = (1 / l) * ((integrate(ebarat * sin(n * pi * x / l)).subs(x, l)) - (integrate(ebarat * sin(n * pi * x / l)).subs(x, -l)))
#         sum+=((an*cos(n*pi*x/l))+(bn*sin(n*pi*x/l)))
#     pretty_print(sum)
#     plot(sum,ebarat)
# expression=input('عبارت را وارد کنید')
# start=input('نقطه شروع را وارد کنید')
# high=input('نقطه انتهایی را وارد کنید')
# fourier(eval(expression),eval(start),eval(high))













