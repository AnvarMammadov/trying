# # #1. Əsl rəqəmlər o rəqəmlərdir ki bölənlərinin cəmi (rəqəmin özünü bölən
# # #kimi hesablamırıq) özünə bərabər olsun. Əsl rəqəmləri tapan funksiya
# # #yazın. Ola bilər ki sizə funksiya lazım olsun.
# def PerfectNumber(num):
#     i=1
#     total=0
#     while i<num:
#         if num%i==0:
#             total+=i
#         if total==num:
#             return num
#         i+=1
# num=int(input("Eded daxil edin :"))
# if PerfectNumber(num)==num:
#     print(num,"is perfect number")
# else:
#     print(num,"is not perfect number")








# #2. 1-36 arasında rəqəm qəbul edən, və buna uyğun kartı ekrana çıxaran   
# #funskiya yazın.
# # 1-9  qara urek
# # 10-19 qirmizi urek
# # 20-29 qara yarpaq
# # 29-36 qirmizi kerpic 

# def ShowCard(num):
#     if num>0 and num<=9:
#         showCard="Qara urek"
#     elif num>9 and num<=19:
#         showCard="Qirmizi urek"
#     elif num>19 and num<=29:
#         showCard="Qara yarpaq"
#     elif num>29 and num<=36:
#         showCard="Qirmizi kerpic"
#     else:
#         showCard="Daxil etdiyiniz edede uygun kart yoxdur"
#     return showCard
# num=int(input("Eded daxil edin :"))
# print(ShowCard(num))










# #3. Verilən rəqəmi müəyyən dəqiqliyə qədər yuvarlaqlaşdıran funksiya
# #yazın. (Funksiya iki parametr qəbul edir, birinci kəsr rəqəm, ikinci
# #parametr isə vergüldən sonra neçə rəqəm qalmalıdır)
# def Yuvarlaq(num1,yv):
#     tam=int(num1)
#     kesr=num1-tam
#     result=tam+int(kesr*(10**yv))/(10**yv)
#     return result
# num=float(input("Ededi daxil edin : "))
# yv=int(input("Yuvarlaqlasirmaq ucun vergulden sonraki reqemin sirasini daxil edin : "))
# print(Yuvarlaq(num,yv))









# #4. Rəqəmin xoşbəxt olub olmadığını tapan funksiya yazın. (Xoşbəxt
# #rəqəm ilk 3 rəqəmin cəmi son 3 rəqəmin cəminə bərabər olmalıdır)
# def XosbextEded(num):
#     totalSonReqem=totalIlkReqem=countIlk=countSon=ilk3Cem=son3Cem=0
#     reverse=""
#     while num>0:
#         dgSon=num%10
#         totalSonReqem+=dgSon
#         reverse+=str(dgSon)
#         num//=10
#         countSon+=1
#         if countSon==3:
#             son3=totalSonReqem
#     numReverse=int(reverse)      
#     while numReverse>0:
#         dgIlk=numReverse%10
#         totalIlkReqem+=dgIlk
#         numReverse//=10
#         countIlk+=1
#         if countIlk==3:
#             ilk3=totalIlkReqem
#     if ilk3Cem==son3Cem:
#         return 1
# numUser=int(input("Ededi daxil edin :"))
# if XosbextEded(numUser)==1:
#     print(numUser,"xosbext ededdir ")
# else:
#     print(numUser,"xosbxt eded deyil!!!")










# #5. İki tarix qəbul edən və bu tarixlər arasındakı fərqi tapan funksiya
# #yazın. Bu funksiyanı yazarkən ilin uzun və ya qısa olduğunu tapan            
# #funksiyanı da yazmalısınız.

# def YearFerq(yearLast,monthLast,dayLast,yearFirst,monthFirst,dayFirst):  
#     dayLastTotal=(yearLast*365)+(monthLast*30+5)+dayLast
#     dayFirstTotal=(yearFirst*365)+(monthFirst*30+5)+dayFirst
#     if yearLast%4==0 or yearLast%100==0 and yearLast%400==0:
#         dayLastTotal+=1
#     if yearFirst%4==0 or yearFirst%100==0 and yearFirst%400:
#         dayFirstTotal+=1
#     dayFerq=dayLastTotal-dayFirstTotal
#     if dayFerq>=0:
#         return dayFerq
#     else:
#         return -dayFerq
    
# print("2 tarix arasindaki ferqi tapmaq ucun ardicil olaraq ilk ili , ayi , gunu sonra da sonu ardicil olaraq daxil edin")
# yearLast=int(input("ili daxil edin : "))
# monthLast=int(input("ayi daxil edin : "))
# dayLast=int(input("gunu daxil edin : "))
# yearFirst=int(input("diger ili daxil edin : "))
# monthFirst=int(input("diger ayi daxil edin : "))
# dayFirst=int(input("diger gunu daxil edin : "))
# if yearLast<=0 or yearFirst<=0 or monthFirst<=0 or monthLast<=0 or dayLast<=0 or dayFirst<=0:
#     print("Daxil etdiyiniz format duzgun deyil!!!\a")
# print("Daxil etdiyiniz tarixler arasindaki ferq :",YearFerq(yearLast,monthLast,dayLast,yearFirst,monthFirst,dayFirst),"gun")





    

   




# #6. Göndərilən massivin ədədi ortasını tapan funksiya yazın.
# def Average(*args):
#     count=avg=total=0
#     i=0
#     for i in args:
#         total+=i
#         count+=1
#     avg=total/count
#     return avg
# print(Average(1,5))










# #7. Massivdəki sıfırların, mənfilərin, müsbətlərin sayını tapan funksiya
# #(funksiyalar) yazın.
# def GetSign(*args):
#     zeroCount=negCount=posCount=0
#     for i in args:
#         if i==0:
#             zeroCount+=1
#         elif i<0:
#             negCount+=1
#         else:
#             posCount+=1
#     return zeroCount,negCount,posCount
# print(GetSign(0,-2,1,-4,0,13,123,-43,342,-2))










# #8. Massivdəki maxmimum və minimum rəqəmi tapan funksiya      
# #(funksiyalar) yazın.
# def IsMax(*args):
#     for i in args:
#         mx=max(args)      
#     return mx
# def IsMin(*args):
#     for i in args:
#         mn=min(args)
#     return mn
# print("Maksimum :",IsMax(5,2,4,66,234,234,21,44),"Minimum :",IsMin(5,2,4,66,234,234,21,44))









# #9. Göndərilən massivi əksinə çevirən funksiya yazın. 
# def Reverse(*args):       
#     for i in args:
#         result=args[::-1]
#     return result
# print(Reverse(1,2,3,4,5,6,7,8,9))










# #10. Massivdəki sadə rəqəmlərin sayını qaytaran fuksiya yazın.
# def GetSimple(*args):
#     argCount=0
#     i=1
#     for i in args:
#         a=1
#         count=0
#         while a<=i:
#             if i%a==0:
#                 count+=1
#             a+=1
#         if count==2:
#             argCount+=1
#     return argCount                  
# print(GetSimple(3,5,10,12,14,1))
       
        


