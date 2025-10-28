if __name__ == '__main__':
     numar1 = 10
     numar2 = 610
     print(numar1 + numar2)
     if numar1 > numar2:
          print('numarul1 este mai mare ca numarul2')
     elif numar1 < numar2:
          print('numarul1 este mai mic ca numarul2')
     else:
          print('numerele sunt egale')

     if numar1 < numar2:
          print('numarul 1 este mai mic ca si numarul 2')

     print('-----------------------')
     numar=112
     if numar%2 == 0:
          print('numarul este par')
     else:
          print('numarul este impar')
     print('/////////////////////////////')
     sir='ana are mere multe'
     if len(sir) == 0:
          print('sirul este gol')
     else:
          print('sirul nu este gol')

     print('/////////////////////////////////////////////////')

     sir1="acrisdsgsft-yahoooo.dom"
     if '@' in sir1:
          print('a introdus adresa de email')
     else:
          print('nu a introdus adresa de email')
     print('-----------------------------------------------------------')

     sir2='radar'
     if sir2 == sir2[::-1]:
          print('este palindrom ')
     else:
          print('nu este palindrom ')

     print('------------------------------')

     sir3='azi este o zi frumoasa'
     caractere_a=sir3.count('a')
     caractere_A = sir3.count('A')
     caractere_a =  caractere_a +  caractere_A
     if caractere_a % 2 == 0:
          print('nr par de caractere')
     else:
          print('nu nr par de caractere')

     print('------------------------------------------')

     for i in range(0,10,1):
          print(i, end=' ')

     for i in range(0, 10, 1):
          print(i)

     print('------------------------------------------')
     sir5='bau eu sunt Ana'
     for i in range(len(sir5)):
          print(i, sir5[i])