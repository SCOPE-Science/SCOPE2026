from cypari2 import Pari
pari = Pari()
pari.default("parisize", "4096M")
Q='x^6 - 3*x^5 + 771*x^4 - 1535*x^3 + 200463*x^2 - 201249*x + 17575221'
# Unit rank of K1,1 (sextic CM?): signature
print("signature:", pari(f'nfsign({Q})'))
print("Q1 signature:", pari('nfsign(x^3-3*x+1)'))
print("K1 signature:", pari('nfsign(x^2+1031)'))
# class number of K1,1 already 2625; regulator-free check of A1^G via bnfinit units? get fu
K1 = pari(f'K1=bnfinit({Q},1); K1.fu')
print("fund units:", K1)
print("torsion:", pari(f'(bnfinit({Q},1)).tu'))
