"""S4a: 2-descent formalism for E_D: y^2=x^3-Dx, D=n^2, n=799657 prime.
E'(=E/D isogenous): y^2=x^3+4Dx with phi:E'->E, phi':E->E'.
phi'-Selmer torsors: d | D i.e. {1,-1,n,-n}, upsigned with 4D: N^2 = d*M^4 + (4D/d)*e^4.
phi-Selmer torsors: d | 4D i.e. {+-1,+-2,+-n,+-2n} with N^2 = d*M^4 - (4D/d)*e^4.
Here we test phi' over image (P1 known non-torsion => one of image torsors nontrivial).
Squares mod n check: legendre(d/n) must be 1 for solubility.
"""
n=799657; D=n*n
def legendre(a,p):
    return pow(a% n, (p-1)//2, p)
for d in [1,-1,n,-n]:
    print(d, 'legendre mod n =', legendre(d,n))
print('-> phi-side survivors mod n: {1,-n} i.e. two classes; -1 fails (Legendre=-1)')
# Q2: D=1 mod 8 (odd square): every odd d is square in Q2; signed: phi' eq mod 8: d odd ok.
print('D mod 8 =', D%8, '(=1). For d odd, M odd,e even => N^2=d mod 8, d=1,-1,n,-n =1 or 7 mod 8...')
print('  d=1: 1 is QR mod 8 -> solvable at 2; d=-1=7 mod 8 -> NOT QR mod 8 -> fails Q2.')
print('=> phi\'-Selmer = {1,-n} if -n (=(799657)(-1)... -n mod 8 = 7?) ', (-n)%8)
