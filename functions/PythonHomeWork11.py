# '''
# 1.Calculator App
# toplama
# chixma
# vurma
# bolme
# quvvete yukseltme

# kök alma  --> ozum elave etdim etdim -->
#  '''
# def NumInput(num1,num2):
#     if type(num1)==str or type(num2)==str:
#         raise ValueError("Format XƏTASI : Ədəd yerinə mətn formatında dəyər daxil edilib!!!\a")
#     return True
# def Toplama(num1,num2):
#     return num1+num2
# def Cixma(num1,num2):
#     return num1-num2
# def Vurma(num1,num2):
#     return num1*num2
# def Bolme(num1,num2):
#     if num2!=0:
#         return num1/num2
#     raise Exception("0-a bölmə XƏTASI : 0 bölmə yoxdur!!!\a")
# def Quvvet(num1,num2):
#     return num1**num2
# def KokAlma(num1,num2):
#     if num1>=0 and num2%2==0 or num1>=0 and num2%2!=0 or num1<=0 and num2%2!=0:
#         return num1**(1/num2)
#     raise Exception("Kök altı XƏTASI : Cüt dərəcədən kökün altında mənfi ədəd ola bilməz!!!\a")


# def Emeliyyat(num1,num2,secim):
#     if secim=="1" or secim=="+":
#         return Toplama(num1,num2)
#     elif secim=="2" or secim=="-":
#         return Cixma(num1,num2)
#     elif secim=="3" or secim=="*":
#         return Vurma(num1,num2)
#     elif secim=="4" or secim=="/":
#         return Bolme(num1,num2)
#     elif secim =="5" or secim=="**":
#         return Quvvet(num1,num2)
#     elif secim=="6" or secim=="^":
#         return KokAlma(num1,num2)
#     else:
#         a="Daxil etdiyiniz secime gore emeliyyat tapilmadi!!!\a\n"
#         return a
# try:
#     print("1)Toplama ==> '+' və ya '1' daxil edin\n\n2)Çıxma ==> '+' və ya '2' daxil edin\n\n3)Vurma ==> '*' və ya '3' daxil edin\n")
#     print("4)Bölmə ==> '/' və ya '4' daxil edin\n\n5)Qüvvətə qaldırma ==> '**' və ya '5' daxil edin\n\n6)Kök alma ==> '^' və ya '6' daxil edin\n")
#     secim=input("Etmək istədiyiniz əməliyyatı seçin : ")
#     num1=float(input("\n1-ci ədədi daxil edin :"))
#     num2=float(input("\n2-ci ədədi daxil edin :"))
#     if NumInput(num1,num2)==True:
#         print("\nCavab : ",Emeliyyat(num1,num2,secim))
# except Exception as ex:
#     print(ex)




# '''
# 2.Valyuta Programi
# 3 mezenneni chevirme ozelliyi
# dollar i {manat,rubl,euro}
# manat i {dollar,rubl,euro}
# euro i {manat,rubl,dollar}
# rubl i {manat,euro,dollar}
# '''
# def CountDollar(mebleg):
#     dollarToManat=mebleg*1.70
#     dollarToEuro=mebleg*0.93
#     dollarToRubl=mebleg*69.91
#     return dollarToManat,dollarToEuro,dollarToRubl
# def CountManat(mebleg):
#     manatToDollar=mebleg*0.59
#     manatToEuro=mebleg*0.55
#     manatToRubl=mebleg*41.46
#     return manatToDollar,manatToRubl,manatToEuro
# def CountEuro(mebleg):
#     euroToDollar=mebleg*1.07
#     euroToManat=mebleg*1.81
#     euroToRubl=mebleg*74.97
#     return euroToDollar,euroToManat,euroToRubl
# def CountRubl(mebleg):
#     rublToDollar=mebleg*0.014
#     rublToManat=mebleg*0.024
#     rublToEuro=mebleg*0.013
#     return rublToDollar,rublToEuro,rublToManat
# def Count(mebleg,secim):
#     if secim=="1" or secim=="dollar":
#         return CountDollar(mebleg)
#     elif secim=="2" or secim=="manat":
#         return CountManat(mebleg)
#     elif secim=="3" or secim=="euro":
#         return CountEuro(mebleg)
#     elif secim=="4" or secim=="rubl":
#         return CountRubl(mebleg)
#     return 0
# def MeblegInputExcept(mebleg):
#     if type(mebleg)==float:
#         return True
#     raise Exception("Dəyər XƏTASI!!! : Daxil edilən format səhvdir!!! (herf ve yaxud simvol daxil edilib!!!)")
# def MeblegSifirdanBoyuk(mebleg,secim):
#     if mebleg>=0:
#         return Count(mebleg,secim)
#     raise Exception("Dəyər XƏTASI!!! : Daxil edilən dəyər sıfırdan kiçik ola bilməz!!! (dəyər sıfırdan kiçik daxil olunub!!!)")
# try:
#     print("\t\t\tValyuta\n1.Dollar ==> ('1' və yaxud 'dollar' daxil edin)\n2.Manat ==> ('2' və yaxud 'manat' daxil edin)")
#     print("3.Euro ==> ('3' və yaxud 'euro' daxil edin)\n4.Rubl ==> ('4' və yaxud 'rubl' daxil edin)\n")
#     secim=input("Çevirmək istədiyiniz məzənnəni daxil edin : ")
#     mebleg=float(input("Dəyəri daxil edin : "))
#     if Count(mebleg,secim)==0:
#         print("Daxil etdiyiniz seçimə uyğun məzənnə tapılmadı...")
#     elif MeblegInputExcept(mebleg)==True:
#         if secim=="1" or secim=="dollar":
#             print(" ",MeblegSifirdanBoyuk(mebleg,secim)[0],"manat\n ",MeblegSifirdanBoyuk(mebleg,secim)[1],"euro\n ",MeblegSifirdanBoyuk(mebleg,secim)[2],"rubl") 
#         elif secim=="2" or secim=="manat":
#             print(" ",MeblegSifirdanBoyuk(mebleg,secim)[0],"dollar\n ",MeblegSifirdanBoyuk(mebleg,secim)[1],"rubl\n ",MeblegSifirdanBoyuk(mebleg,secim)[2],"euro") 
#         elif secim=="3" or secim=="euro":
#             print(" ",MeblegSifirdanBoyuk(mebleg,secim)[0],"dollar\n ",MeblegSifirdanBoyuk(mebleg,secim)[1],"manat\n ",MeblegSifirdanBoyuk(mebleg,secim)[2],"rubl") 
#         elif secim=="4" or secim=="rubl":
#             print(" ",MeblegSifirdanBoyuk(mebleg,secim)[0],"dollar\n ",MeblegSifirdanBoyuk(mebleg,secim)[1],"euro\n ",MeblegSifirdanBoyuk(mebleg,secim)[2],"manat")      
# except Exception as ex:
#     print(ex)
    