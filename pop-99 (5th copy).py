#!/usr/bin/python

row_0 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
row_m1 = [24, 26, 31, 32, 38, 42]
row_m2 = [2, 6, 8, 16, 36, 48]
row_m3 = [6, 7, 9, 18, 27, 46]
row_m4 = [7, 9, 11, 18, 29, 46]

w_los4 = [1, 16, 20, 21, 45, 46]
w_los4p = [13, 19, 24, 31, 37, 46]
w_los3 = [9, 15, 26, 31, 47, 49]
w_los3p = [3, 10, 11, 22, 30, 39]
w_los2 = [13, 16, 22, 25, 29, 32]
w_los2p = [2, 8, 18, 20, 25, 37]
w_los1 = [4, 8, 11, 20, 41, 44]
w_los1p = [2, 16, 17, 29, 31, 47]

row_1 = row_m1[:]
row_2 = row_m2[:]
row_3 = row_m3[:]
row_4 = row_m4[:]


for x in [5, 4, 3, 2, 1, 0]:
 zx1 = row_m1[x]
 zx2 = row_m2[x]
 zx3 = row_m3[x]
 zx4 = row_m4[x]
 if row_1.count(zx1+1) == 0: row_1.insert(x+1, zx1+1) #wazna kolejnosc wstawiania
 if row_1.count(zx1-1) == 0: row_1.insert(x, zx1-1)
 if row_2.count(zx2+1) == 0: row_2.insert(x+1, zx2+1)
 if row_2.count(zx2-1) == 0: row_2.insert(x, zx2-1)
 if row_3.count(zx3+1) == 0: row_3.insert(x+1, zx3+1)
 if row_3.count(zx3-1) == 0: row_3.insert(x, zx3-1)
 if row_4.count(zx4+1) == 0: row_4.insert(x+1, zx4+1)
 if row_4.count(zx4-1) == 0: row_4.insert(x, zx4-1)

print row_m1, row_1
print row_m2, row_2
print row_m3, row_3
print row_m4, row_4

row_b_s = 0
row_c_s = 0
row_d_s = 0
row_bcd = [0, 0, 0, 0, 0, 0]
row_abcd = [0, 0, 0, 0, 0, 0]

row_mm1 = [row_m1[0]%10, row_m1[1]%10, row_m1[2]%10, row_m1[3]%10, row_m1[4]%10, row_m1[5]%10]
row_mm2 = [row_m2[0]%10, row_m2[1]%10, row_m2[2]%10, row_m2[3]%10, row_m2[4]%10, row_m2[5]%10]
row_mm3 = [row_m3[0]%10, row_m3[1]%10, row_m3[2]%10, row_m3[3]%10, row_m3[4]%10, row_m3[5]%10]
row_mm4 = [row_m4[0]%10, row_m4[1]%10, row_m4[2]%10, row_m4[3]%10, row_m4[4]%10, row_m4[5]%10]

j_mm_pop = [0, 0, 0, 0, 0, 0]

j_m1_roz = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
j_m2_roz = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
j_m3_roz = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
j_m4_roz = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


def dziesiatki(z_row1):
 l_dz = [0, 0, 0, 0, 0]
 for z_r in z_row1:
  if z_r <= 9:
   l_dz[0] = l_dz[0] + 1
  elif z_r <= 19:
   l_dz[1] = l_dz[1] + 1
  elif z_r <= 29:
   l_dz[2] = l_dz[2] + 1
  elif z_r <= 39:
   l_dz[3] = l_dz[3] + 1
  elif z_r <= 49:
   l_dz[4] = l_dz[4] + 1
 return l_dz

def jednostki(z_row2):
 l_j = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
 for z_j in z_row2:
  if z_j == 0:
   l_j[0] = l_j[0] + 1
  elif z_j == 1:
   l_j[1] = l_j[1] + 1
  elif z_j == 2:
   l_j[2] = l_j[2] + 1
  elif z_j == 3:
   l_j[3] = l_j[3] + 1
  elif z_j == 4:
   l_j[4] = l_j[4] + 1
  elif z_j == 5:
   l_j[5] = l_j[5] + 1
  elif z_j == 6:
   l_j[6] = l_j[6] + 1
  elif z_j == 7:
   l_j[7] = l_j[7] + 1
  elif z_j == 8:
   l_j[8] = l_j[8] + 1
  elif z_j == 9:
   l_j[9] = l_j[9] + 1
 return l_j

#np dz_m1 = [0, 3, 2, 1, 0]
dz_m1 = dziesiatki(row_m1)
dz_m2 = dziesiatki(row_m2)
dz_m3 = dziesiatki(row_m3)
dz_m4 = dziesiatki(row_m4)

#np j_m1 = [3, 2, 1, 0, 0, 0, 0, 0, 0, 0]
j_m1 = jednostki(row_mm1)
j_m2 = jednostki(row_mm2)
j_m3 = jednostki(row_mm3)
j_m4 = jednostki(row_mm4)

def dziesiatki_suma(lista5, lista6):
 lista_56 = [0, 0, 0, 0, 0]
 for x56 in [0, 1, 2, 3, 4]:
  lista_56[x56] = min(lista5[x56], lista6[x56])
 return lista_56

#roznice
def jednostki_suma(lista1, lista2):
 lista_wyn = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
 for x1 in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
  lista_wyn[x1] = min(lista1[x1], lista2[x1])
 return lista_wyn

def sortuj(lista_s):
 lista_sort = [0] *len(lista_s)
 listast = lista_s[:]
 for xs in range(0,len(listast),1):
  lista_sort[xs] = min(listast)
  listast.remove(min(listast))
 return lista_sort

#ile wyazow z j_lista jest w liscie w_lista (j_lista bierze kazdy wyraz musi byc bez powtorzen)
def trafionych(j_lista, w_lista):
 wynik_j = []
 for xj in range(0, len(j_lista)):
  if w_lista.count(j_lista[xj]) > 0:
   wynik_j.insert(len(wynik_j)+1, j_lista[xj])
 return wynik_j

#petla glowna

plik = open("ppp-99.txt", "wb")
for par01 in [0]:     #[0, 1]:
 for par02 in [2]:     #[2, 3, 4]:
  for par03 in [1]:
   for par04 in [6]:   #[3, 5]:
    for par05 in [3]:    #[1, 2, 3]:
     for par06 in [6]:    #[0, 6]:
      for par07 in [8]:    #[4, 6, 8]:
       for par08 in [2]:    #[1, 2]:
        for par09 in [0, 1]:    #[0, 1]:
#         plik = open("ppp-tr" + str(par01) + str(par02) + str(par03) + str(par04) + ".txt", "wb")
         print par01, par02, par03, par04, par05, par06, par07, par08, par09
         row_all = [row_1, row_2, row_3, row_4]
         row_all_plus = [row_1, row_2, row_3, row_4, row_1, row_2, row_3]
         all00 = 0
         all01 = 0
         all02 = 0
         all03 = 0
         all04 = 0
         all05 = 0
         all06 = 0
         all07 = 0
         all08 = 0
         all09 = 0
         for row_a in row_all:
          row_b = row_all_plus[row_all_plus.index(row_a)+1]
          row_c = row_all_plus[row_all_plus.index(row_a)+2]
          row_d = row_all_plus[row_all_plus.index(row_a)+3]
#          print row_all.index(row_a), "row-a", row_a
          for a01 in row_a:
#  print a01
           for a02 in row_a:
            if a02 > a01:
             for a03 in row_a:
              if a03 > a02:
               for a04 in row_a:
                if a04 > a03:
                 for a05 in row_0:
                   if (a05 <> a04) & (a05 <> a03) & (a05 <> a02) & (a05 <> a01):
                    for a06 in row_0:
                     if (a06 > a05) & (a06 <> a04) & (a06 <> a03) & (a06 <> a02) & (a06 <> a01):
                      dz_ax6 = dziesiatki([a01, a02, a03, a04, a05, a06])
                      all00 = all00 + 1
#                                     | 3 | 2| 1 | 0 | 0|
                      if (dz_ax6.count(6) == 0) & (dz_ax6.count(5) == 0) & (dz_ax6.count(4) <= 1) & (dz_ax6.count(3) == 0) & (dz_ax6.count(2) <= 1) & (dz_ax6.count(1) <= 4) & (dz_ax6.count(0) <= 3):
                       all01 = all01 + 1
                       if ((row_b.count(a01) + row_b.count(a02) + row_b.count(a03) + row_b.count(a04) + row_b.count(a05) + row_b.count(a06)) <= 3) & ((row_c.count(a01) + row_c.count(a02) + row_c.count(a03) + row_c.count(a04) + row_c.count(a05) + row_c.count(a06)) <= 3) & ((row_d.count(a01) + row_d.count(a02) + row_d.count(a03) + row_d.count(a04) + row_d.count(a05) + row_d.count(a06)) <= 3):
#^to wyzej, sprawdza dla b,c,d pozostale trzy listy
                        row_bcd[0] = row_b.count(a01) + row_c.count(a01) + row_d.count(a01)
                        row_bcd[1] = row_b.count(a02) + row_c.count(a02) + row_d.count(a02)
                        row_bcd[2] = row_b.count(a03) + row_c.count(a03) + row_d.count(a03)
                        row_bcd[3] = row_b.count(a04) + row_c.count(a04) + row_d.count(a04)
                        row_bcd[4] = row_b.count(a05) + row_c.count(a05) + row_d.count(a05)
                        row_bcd[5] = row_b.count(a06) + row_c.count(a06) + row_d.count(a06)
# dla row_bcd i row_abcd [ile_a01,a02,a03,a04,a05,a06]
                        if (min(row_bcd[0:3]) == 0) & (max(row_bcd) >= 2):
                         all02 = all02 + 1
                         row_abcd[0] = row_a.count(a01) + row_bcd[0]
                         row_abcd[1] = row_a.count(a02) + row_bcd[1]
                         row_abcd[2] = row_a.count(a03) + row_bcd[2]
                         row_abcd[3] = row_a.count(a04) + row_bcd[3]
                         row_abcd[4] = row_a.count(a05) + row_bcd[4]
                         row_abcd[5] = row_a.count(a06) + row_bcd[5]
                         if (max(row_abcd[0:3]) >= 2) & (min(row_abcd) == 0):
#                         plik.write("\n" + str([a01, a02, a03, a04, a05, a06]))
                          all03 = all03 + 1
                          dz_m1_roz = dziesiatki_suma(dz_ax6, dz_m1)
                          dz_m2_roz = dziesiatki_suma(dz_ax6, dz_m2)
                          dz_m3_roz = dziesiatki_suma(dz_ax6, dz_m3)
                          dz_m4_roz = dziesiatki_suma(dz_ax6, dz_m4)
                          dz_m1_roz_s = sum(dz_m1_roz)
                          dz_m2_roz_s = sum(dz_m2_roz)
                          dz_m3_roz_s = sum(dz_m3_roz)
                          dz_m4_roz_s = sum(dz_m4_roz)
                          dz_roz_sum = [dz_m1_roz_s, dz_m2_roz_s, dz_m3_roz_s, dz_m4_roz_s]
                          if (dz_roz_sum.count(6) <= 1) & (dz_roz_sum.count(5) <= 1) & (dz_roz_sum.count(4) <= 3) & (dz_roz_sum.count(3) <= 3) & (dz_roz_sum.count(2) <= 3) & (dz_roz_sum.count(1) <= 1) & (dz_roz_sum.count(0) <= 1) & (dz_roz_sum.count(0) <= par03) & (max(dz_roz_sum) <= par04):
                           all04 = all04 + 1
                           j_mm10 = jednostki([a01%10, a02%10, a03%10, a04%10, a05%10, a06%10])
                           j_m1_roz = jednostki_suma(j_mm10, j_m1)
                           j_m2_roz = jednostki_suma(j_mm10, j_m2)
                           j_m3_roz = jednostki_suma(j_mm10, j_m3)
                           j_m4_roz = jednostki_suma(j_mm10, j_m4)
                           j_m1_m2_roz = jednostki_suma(j_m1_roz,j_m2_roz)
                           j_m1_m3_roz = jednostki_suma(j_m1_roz,j_m3_roz)
                           j_m1_m4_roz = jednostki_suma(j_m1_roz,j_m4_roz)
                           j_m2_m3_roz = jednostki_suma(j_m2_roz,j_m3_roz)
                           j_m2_m4_roz = jednostki_suma(j_m2_roz,j_m4_roz)
                           j_m3_m4_roz = jednostki_suma(j_m3_roz,j_m4_roz)
                           j_m1234_roz = [sum(j_m1_m2_roz[:]),sum(j_m1_m3_roz[:]),sum(j_m1_m4_roz[:]),sum(j_m2_m3_roz[:]),sum(j_m2_m4_roz[:]),sum(j_m3_m4_roz[:])]
#                                 .2.1.1.1.1.0.0.0.0.0.
#                                 .roznica. roznic...
                           #if ((j_mm10.count(2) <= par05) & (j_mm10.count(1) <= par06)) | (j_mm10.count(0) <= par07):
                           if sum(j_m1234_roz) <= 7:
                            j_m1_roz_s = sum(j_m1_roz)
                            j_m2_roz_s = sum(j_m2_roz)
                            j_m3_roz_s = sum(j_m3_roz)
                            j_m4_roz_s = sum(j_m4_roz)
                            j_roz_sum = [j_m1_roz_s, j_m2_roz_s, j_m3_roz_s, j_m4_roz_s]
                            all05 = all05 + 1
                            if j_roz_sum.count(6) == 0:
                             if j_roz_sum.count(5) == par01:
                              if j_roz_sum.count(4) <= par02:
                               if j_roz_sum.count(3) <= par02:
                                if j_roz_sum.count(2) <= par02:
                                 if j_roz_sum.count(1) <= par08:
                                  if j_roz_sum.count(0) == par09:
                                   all06 = all06 + 1
                                   j_mm = sortuj([a01, a02, a03, a04, a05, a06])
                                   j_mm_roz = [j_mm[1] - j_mm[0], j_mm[2] - j_mm[1], j_mm[3] - j_mm[2], j_mm[4] - j_mm[3] , j_mm[5] - j_mm[4]]
                                   if (j_mm_roz.count(j_mm_roz[0]) <= 1) & (j_mm_roz.count(j_mm_roz[1]) <= 1) & (j_mm_roz.count(j_mm_roz[2]) <= 1) & (j_mm_roz.count(j_mm_roz[3]) <= 1):
                                    j_mm2 = [a01%2, a02%2, a03%2, a04%2, a05%2, a06%2]
                                    if (j_mm2.count(0) >= 1) & (j_mm2.count(0) <= 5):
                                     all07 = all07 + 1
                                     if (sum(j_mm10[0:4]) > 1) & (sum(j_mm10[5:9]) > 1):
                                      all08 = all08 + 1
# plik.write("\n" + wynik_jmm) # zapisuje trafione powyzej 3, sprawdza w funkcji
                                      wynik_jmm = trafionych(j_mm, w_los1)
                                      if len(wynik_jmm) >= 3:
                                       all09 = all09 + 1
#                                       if len(wynik_jmm) >= 4:
#                                        plik.write("\n" + str(j_mm) + " w " + str(w_los1) + str(wynik_jmm))
         plik.write("\n" + str(par01)+ str(par02)+ str(par03)+ str(par04)+ str(par05)+ str(par06)+ str(par07)+ str(par08)+ str(par09) + ", " + str([all00, all01, all02, all03, all04, all05, all06, all07, all08]) + " - " + str(all09) +str(j_m1_m2_roz))
plik.close()
print "all", all00, all01, all02, all03, all04, all05, all06, all07, all08, all09

#plik = open("ppp.txt", "wb")
#plik.write("\n" + str([a01, a02, a03, a04, a05, a06]))
#plik.close()

