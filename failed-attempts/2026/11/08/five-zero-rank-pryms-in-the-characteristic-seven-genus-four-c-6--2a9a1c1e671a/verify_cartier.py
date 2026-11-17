"""Reconstruct the characteristic-seven Cartier coefficients symbolically.
Run: python verify_cartier.py   (Python standard library only).
"""
from collections import defaultdict
P = 7
# Monomial key: (power of x, power of a, power of b).
def mul(F,G):
    out = defaultdict(int)
    for (i,j,k),c in F.items():
        for (l,m,n),d in G.items():
            key=(i+l,j+m,k+n)
            out[key]=(out[key]+c*d)%P
    return {k:v for k,v in out.items() if v%P}
def powpoly(F,n):
    out={(0,0,0):1}
    for _ in range(n):out=mul(out,F)
    return out
F={(10,0,0):1,(7,0,0):1,(4,1,0):1,(1,0,1):1}
C=powpoly(F,3)
M={}
for i in range(1,5):
    for j in range(1,5):
        M[i,j]={(a,b):coef for (x,a,b),coef in C.items() if x==7*i-j}
expected={
 (1,1):{(1,2):3},(1,4):{(0,3):1},(2,2):{(3,0):1,(1,1):6,(0,2):3},
 (3,3):{(2,0):3,(1,0):3,(0,1):6},(4,1):{(0,0):3},
 (4,4):{(1,0):3,(0,0):3}
}
for i in range(1,5):
    for j in range(1,5):
        assert M[i,j]==expected.get((i,j),{}),(i,j,M[i,j])
print('C7_CARTIER_SYMBOLIC_COEFFICIENTS_PASS')
# Independently compute the elliptic quotient Hasse coefficient.
E={(4,0,0):1,(3,0,0):1,(2,1,0):1,(1,0,1):1}
CE=powpoly(E,3)
u={(a,b):coeff for (x,a,b),coeff in CE.items() if x==6}
assert u==expected[2,2]
print('C7_ELLIPTIC_QUOTIENT_HASSE_PASS')
