"""Independent finite checks of the stated exact congruence theorem.
Run with Python 3; the proof of the infinite statement is in RESULT.md.
"""
from collections import Counter
from fractions import Fraction

M = ((0,1,0),(0,0,1),(1,1,0))
I = tuple(tuple(int(i==j) for j in range(3)) for i in range(3))
def product(a,b):
    return tuple(tuple(sum(a[i][h]*b[h][j] for h in range(3)) for j in range(3)) for i in range(3))
def power(n):
    a=I
    for _ in range(n): a=product(a,M)
    return a
A=power(7)
assert A==((1,2,2),(2,3,2),(2,4,3))
B=tuple(tuple((A[i][j]-I[i][j])//2 for j in range(3)) for i in range(3))
assert B==((0,1,1),(1,1,1),(1,2,1))
C=tuple(tuple(B[i][j]+product(B,B)[i][j] for j in range(3)) for i in range(3))
W=(-2,1,-1)
for r in range(7):
    U=power(r)
    def slope(Q):
        T=product(U,Q)
        return sum(T[0][j]*W[j] for j in range(3))%2
    if r==4: assert slope(B)==slope(C)==1
    if r==0: assert slope(B)==0
# D_n = P_n - R_n; check exactly two even branches at precision >=4.
N=7*2**13
p=[1,1,1];r=[3,0,2]
for _ in range(3,N):
    p.append(p[-2]+p[-3]);r.append(r[-2]+r[-3])
d=[x-y for x,y in zip(p,r)]
assert [x%2 for x in d[:7]]==[0,1,1,1,0,0,1]
assert all(d[7*t]%4==2 for t in range(0,100))
assert all(d[7*t+j]%2==1 for t in range(0,100) for j in (1,2,3,6))
def v2(n):
    if n==0:return 10**9
    return (abs(n)&-abs(n)).bit_length()-1
for t in range(1,700): assert v2(d[7*t+4])==1+v2(t)
for k in range(1,13):
    period=7*2**(k-1)
    assert all(d[n+period]%(2**k)==d[n]%(2**k) for n in range(period))
    matching=[n for n in range(period) if d[n]%(2**k)==0]
    expected=3 if k==1 else 1+(2**((k-1)//2) if k<=11 else 64)
    assert len(matching)==expected,(k,expected,len(matching))
    if k>=2: assert [n for n in matching if n%7==4]==[4]
    print('k=',k,'period=',period,'modular coincidences=',len(matching))
# Test the 2-adic-isometric auxiliary H on rational points u>=1.
h=[Fraction(d[7*(u-1)+5],2*u) for u in range(1,100)]
for u in range(1,85):
    for v in range(u+1,85):
        x=h[u-1]-h[v-1]
        assert v2(x.numerator)-v2(x.denominator)==v2(u-v)
# Exact H(0) modulo 64 via eight Mahler coefficients and a controlled tail.
w=(0,1,-2)
T=I
h0=Fraction(0)
for j in range(1,9):
    T=product(T,B)
    cj=sum(T[0][s]*w[s] for s in range(3))
    h0+=Fraction(2**(j-1)*(-1)**(j-1)*cj,j)
assert (h0.numerator*pow(h0.denominator,-1,64))%64==32
print('Exact initial matrix data and complete low-power counts verified; H(0) = 32 (mod 64).')
