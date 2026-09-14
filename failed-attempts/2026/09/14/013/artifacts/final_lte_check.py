from cypari2 import Pari
pari = Pari()
print("v3(1031^2-1) =", pari('valuation(1031^2-1,3)'))
print("v3(1031^6-1) =", pari('valuation(1031^6-1,3)'))
print("orders mod 9,27,81,243,729:", [str(pari(f'znorder(Mod(1031,{3**k}))')) for k in range(2,7)])
print("chi(3) =", pari('kronecker(-1031,3)'))
print("disc =", pari('nfdisc(x^2+1031)'))
