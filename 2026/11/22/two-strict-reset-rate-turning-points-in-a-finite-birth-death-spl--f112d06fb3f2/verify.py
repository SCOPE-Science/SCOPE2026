"""Exact rational verification of a two-turn splitting-probability example.
Run: python3 verify.py. Only Python standard-library dependencies.
"""
from fractions import Fraction as F
from math import comb

P = [None] + [F(n,100) for n in (95,10,80,30,1,40,75,45,40,10)]
N = 0

def check(test, message):
    global N
    N += 1
    if not test:
        raise AssertionError(message)

def add(a,b):
    return [(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))]

def mul(a,b):
    out=[F(0)]*(len(a)+len(b)-1)
    for i,c in enumerate(a):
        for j,d in enumerate(b):out[i+j]+=c*d
    return out

def scale(a,c):return [c*v for v in a]

def shift(a):return [F(0)]+a

def diff(a):return [i*a[i] for i in range(1,len(a))]

def ev(a,x):return sum(c*x**i for i,c in enumerate(a))

def continuant(lo,hi):
    old=[F(1)]; cur=[F(1)]
    for j in range(lo+1,hi+1):
        nxt=add(cur, scale(shift(old), -P[j-1]*(1-P[j])))
        old,cur=cur,nxt
    return cur

L=continuant(1,4)
R=continuant(6,10)
check(L==[1,F(-287,200),F(1197,2500)],'left continuant')
check(R==[1,F(-457,400),F(423,2000)],'right continuant')
C = F(1)
for j in range(1,6):C *= 1-P[j]
for j in range(5,11):C /= P[j]
check(C==F(231,2),'boundary-path odds prefactor')
H=add(scale(mul(R,L),-1),scale(shift(add(mul(diff(R),L),scale(mul(R,diff(L)),-1))),2))
check(H==[F(-1),F(253,80),F(-271919,80000),F(2675169,2000000),F(-506331,5000000)],'derivative numerator')
transform=[sum(H[j]*comb(4-j,i-j) for j in range(i+1)) for i in range(5)]
check(transform==[F(-1),F(-67,80),F(7081,80000),F(54219,2000000),F(-423,2500000)],'Descartes transform')
check([int(t>0)-int(t<0) for t in transform]==[-1,-1,1,1,-1],'two sign variations')
for x,expect in [(F(0),-1),(F(4,5),-1),(F(9,10),1),(F(99,100),1),(F(999,1000),-1),(F(1),-1)]:
    check((ev(H,x)>0)-(ev(H,x)<0)==expect,f'sign at {x}')
for A in [L,R]:
    check(ev(A,1)>0 and sum(diff(A))<0, 'positive decreasing continuant [0,1]')

def solve(A,b):
    n=len(A)
    A=[[F(v) for v in row]+[F(b[i])] for i,row in enumerate(A)]
    for j in range(n):
        pivot=next(i for i in range(j,n) if A[i][j]!=0)
        A[j],A[pivot]=A[pivot],A[j]
        factor=A[j][j];A[j]=[z/factor for z in A[j]]
        for i in range(n):
            if i==j:continue
            factor=A[i][j]
            if factor:A[i]=[A[i][k]-factor*A[j][k] for k in range(n+1)]
    return [row[-1] for row in A]

for s in [F(1,4),F(1,2),F(3,4),F(9,10),F(99,100),F(1)]:
    M=[[F(i==j) for j in range(10)] for i in range(10)]
    for i in range(1,11):
        if i>1:M[i-1][i-2]=-s*(1-P[i])
        if i<10:M[i-1][i]=-s*P[i]
    blo=[F(0)]*10;blo[0]=s*(1-P[1])
    bhi=[F(0)]*10;bhi[-1]=s*P[10]
    U=solve(M,blo)[4]
    V=solve(M,bhi)[4]
    Q=U/(U+V)
    ex=C*ev(R,s*s)/(s*ev(L,s*s))
    check(U/V==ex,f'full resolvent check, s={s}')
    check(Q==ex/(1+ex),f'probability check, s={s}')
    check(0<Q<1,f'valid probability, s={s}')
print(f'PASS {N} exact rational assertions; two strict interior extrema certified by Descartes and sign brackets')
