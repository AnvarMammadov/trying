# def MinMax(*args):
#     mx=max(args)
#     mn=min(args)
#     print("Max : ",mx)
#     print("Min : ",mn)
# MinMax(2,-5,-2,0,239,48,888,9923,393,9999)


# class myObject():
#     def __init__(self):
#         pass


# def myFunc(num):
#     count=0
#     i=1
#     while i<=num:
#         if num%i==0:
#             count+=1
#         i+=1
#     if num<=0:
#         print("Daxil etdiyiniz eded natural eded deyil!!!")
#     if count==1:
#         print("Daxil etdiyiniz eded ne sade ne de murekkebdir : ",num)
#     elif count==2:
#         print("Daxil etdiyiniz eded sadedir : ",num)
#     elif count>2:
#         print("Daxil etdiyiniz eded murekkebdir : ",num)
# for i in range(100):
#     num=int(input("Eded daxil edin : "))
#     myFunc(num)







# # ax^2+bx+c=0   D=b^2-4*a*c
# def kvTenlik(a,b,c):
#     if a!=0:
#         print("Daxil etdiyiniz parametrlərə görə kvadrat tənliyin çıxarışı...\n")
#         print(a,"x^2","+",b,"x","+",c,"=","0\n")
#     else:
#         print("Daxil etdiyiniz parametr kvadrat tənlik yaratmır...\n")
#         return 0
#     D=b**2-4*a*c
#     if D<0:
#         print("Tənliyin həqiqi kökü yoxdur...\n")
#     elif D==0:
#         print("Tənliyin iki bərabər və yaxud yeganə kökü var...\n")
#         x=-b/2*a
#         print("Tənliyin kökü :  x =",x,"\n\n\n")
#     else :
#         print("Tənliyin iki fərqli kökü var...")
#         x1=(-b+D**0.5)/2*a
#         x2=(-b-D**0.5)/2*a
#         print("Tənliyin 1-ci kökü :  x1 =",x1,"\n")
#         print("Tənliyin 2-ci kökü :  x2 =",x2,"\n\n\n")
# for i in range(100):
#     a=int(input("a parametrini daxil edin (DİQQƏT!!! əgər a parametrini '0' daxil etsəniz kvadrat tənlik olmayacaq) : "))
#     b=int(input("b parametrini daxil edin : "))
#     c=int(input("c parametrini daxil edin : "))
#     kvTenlik(a,b,c)



# for i in range(10):
#     num=int(input("Eded daxil edin : "))
#     rNum=0
#     realNum=num
#     while num>0:
#         dg=num%10
#         rNum=rNum*10+dg
#         num//=10
#     if realNum==rNum:
#         print("Eded polindromdur.")
#     else:
#         print("Eded polindrom deyil !!!")


# ededin faktorialini tapan proqram yazin...
# def Fc(num):
#     fc=1
#     for i in range(1,num+1):
#         fc*=i
#     return fc
# def inPut(num):
#     if type(num)==int:
#         return Fc(num)
#     raise Exception("Dəyər XƏTASI !!!")
# try:
#     num=int(input("Eded daxil edin : "))
#     print(inPut(num))
# except Exception as ax:
#     print(ax)      



# def ZeroDivEr(a,b):
#     if b!=0:
#         return a/b
#     raise Exception("Zero Division Error!!! Zeroooo")
# try:
#     a=int(input("Enter first number : "))
#     b=int(input("Enter second number : "))
#     print(ZeroDivEr(a,b))
# except Exception as ex:
#     print(ex)
# def Toplama(num1,num2):
#     return num1+num2
# def Cixma(num1,num2):
#     return num1-num2
# def Bolme(num1,num2):
#     if num2!=0:
#         return num1/num2
#     raise Exception("Zero Division Error !!! Can not division zero!!!\a")
# def Vurma(num1,num2):
#     return num1*num2
# def Quvvet(num1,num2):
#     return num1**num2
# def KokAlma(num1,num2):
#     if num1<0 and num2%2!=0 or num1>=0:
#         return num1**(1/num2)
#     raise Exception("Cut dereceden kok xetasi !!! Cut dereceden kokun altinda menfe eded ola bilmez!!!")
# def Operat(num1,num2,secim):
#     if secim=="1":
#         return Toplama(num1,num2)
#     elif secim=="2":
#         return Cixma(num1,num2)
#     elif secim=="3":
#         return Bolme(num1,num2)
#     elif secim=="4":
#         return Vurma(num1,num2)
#     elif secim=="5":
#         return Quvvet(num1,num2)
#     elif secim=="6":
#         return KokAlma(num1,num2)
#     return 0 
# try:
#     print("1)Toplama\n2)Cixma\n3)Bolme\n4)Vurma\n5)Quvvet\n6)Kok Alma")
#     secim=input("Etmek istediyiniz emeliyyati secin : ")
#     num1=float(input("1-ci ededi daxil edin : "))
#     num2=float(input("2-ci ededi daxil edin : "))
#     print(Operat(num1,num2,secim))
# except Exception as ex:
#     print(ex)




# EBOB ve EKOB'un tapilmasi 
# 2 eded daxil olunur,bu 2 ededin EBOB'u ve EKOB'u tapilmalidi.
#
# Hell yolu --> daxil olunan ededleri sade vuruqlarina ayiririq , hemin vuruqlari listde saxlayiriq , sonra listler arasinda
# muqayise serti yaziriq.
# def S(num1,num2):
#     if num1>num2 and num1>0 and num2>0:
#         s=num2
#     elif num2>num1 and num1>0 and num2>0:
#         s=num1
#     elif num1==num2:
#         s=num1
#     for i in range(1,s+1):
#         if num1%i==0 and num2%i==0:
#             ebob=i
#     return ebob
# num1=int(input("Enter firs number : "))
# num2=int(input("Enter second number : "))




