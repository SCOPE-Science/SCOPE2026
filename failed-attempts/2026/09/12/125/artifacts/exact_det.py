from fractions import Fraction
def B3(x):
    ax = abs(x)
    if ax < 1: return (Fraction(4)-6*x*x+3*ax**3)/6
    elif ax <= 2: return (Fraction(2)-ax)**3/6
    else: return Fraction(0)
a=Fraction(1,2); beta=Fraction(6,11); delta=Fraction(1,22); binv=Fraction(6,11)
KS=list(range(-7,8))
def Gk(k,x):
    tot=Fraction(0)
    for n in range(-10,11):
        tot+=B3(x-n*a)*B3(x-n*a-k*beta)
    return tot
y=Fraction(0); th=0
# M[s,sp] = binv * sum_{k: (s-12k)%11==sp} G_k(s*delta)  (q=0 phases at th=0)
M=[[Fraction(0)]*11 for _ in range(11)]
for s_ in range(11):
    for sp in range(11):
        tot=Fraction(0)
        for k in KS:
            if (s_-12*k)%11 != sp: continue
            tot+=Gk(k, y+s_*delta)
        M[s_][sp]=binv*tot
# scale to integers
from math import gcd
from functools import reduce
def lcm(x,y): return x//gcd(x,y)*y
D=reduce(lcm,[f.denominator for row in M for f in row])
A=[[int(f*D) for f in row] for row in M]
print("scale D digits:",len(str(D)))
# Bareiss
n=11
B=[row[:] for row in A]
prev=1
for k in range(n-1):
    # partial pivot
    if B[k][k]==0:
        piv=next((i for i in range(k+1,n) if B[i][k]!=0),None)
        if piv is None:
            print("EXACT DET = 0 (zero pivot col)"); break
        B[k],B[piv]=B[piv],B[k]
    for i in range(k+1,n):
        for j in range(k+1,n):
            B[i][j]=(B[i][j]*B[k][k]-B[i][k]*B[k][j])//prev
        B[i][k]=0
    prev=B[k][k]
else:
    det=B[n-1][n-1]
    print("det(scaled) =",det)
    print("EXACT det(M) = det/D^11 =", "0" if det==0 else f"{det}/{D**11}")
print("done")
