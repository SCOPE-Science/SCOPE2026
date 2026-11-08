#!/usr/bin/env python3
"""Exact-arithmetic checks for a Richardson-extrapolated directed-cycle step.

Uses only the Python standard library. Finite checks supplement, but do not
replace, the all-dimension and all-stepsize arguments in RESULT.md.
"""
from fractions import Fraction as F
from math import comb

checks=0

def check(x, reason):
    global checks
    assert x, reason
    checks += 1

def add(a,b):
    c=[0]*max(len(a),len(b))
    for j,x in enumerate(a): c[j]+=x
    for j,x in enumerate(b): c[j]+=x
    return trim(c)

def trim(a):
    a=a[:]
    while len(a)>1 and a[-1]==0:a.pop()
    return a

def sub(a,b):return add(a,[-v for v in b])
def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return trim(c)
def power(a,k):
    o=[1]
    for _ in range(k):o=mul(o,a)
    return o
def scale(a,k):return [k*x for x in a]
def shift(a,k):return [0]*k+a

def numerator_no_hj(n,j):
    # This is N_{n,j}(h)/h^j, over the common strictly positive
    # denominator ((h+2)^n-h^n)^2*((h+1)^n-h^n).
    A=[2,1];B=[1,1];Hn=[0]*n+[1]
    U=sub(power(A,n),Hn);V=sub(power(B,n),Hn)
    term=scale(mul(power(A,2*n-j-2),V),8*(j+1))
    if j<n-1:
        term=add(term,scale(shift(mul(power(A,n-j-2),V),n),8*(n-j-1)))
    return sub(term,mul(power(B,n-j-1),power(U,2)))

p=[-96,-160,560,2240,3450,2850,1300,300,25]
for n in range(2,6):
    for j in range(n):
        num=numerator_no_hj(n,j)
        if n<=4 or j<4:
            check(all(v>=0 for v in num),f'negative coefficient n={n},j={j}: {num}')
            check(any(v>0 for v in num),f'zero coefficient polynomial n={n},j={j}')
        else:
            check(num==scale(p,4),f'five-cycle exceptional polynomial differs: {num}')
            signs=[1 if x>0 else -1 for x in num if x]
            check(sum(s!=t for s,t in zip(signs,signs[1:]))==1,
                  'exceptional numerator should have one sign change')

# Rational endpoint bracket, uniqueness analytically follows from Descartes.
def evaluate(poly,h):return sum(F(c)*h**j for j,c in enumerate(poly))
left=F(297835687,10**9)
right=F(297835689,10**9)
check(evaluate(p,left)<0,'lower root bracket')
check(evaluate(p,right)>0,'upper root bracket')

def coeff(n,j,h):
    a=h/(h+2); b=h/(h+1)
    return (F(8,(1)) / (h+2)**2 * a**j *
            (F(j+1)+F(n-j-1)*a**n)/(1-a**n)**2
            -h**j/(h+1)**(j+1)/(1-b**n))

# An independent finite-dimensional matrix computation, never used for the
# continuum/all-n proof: exact inverse by row reduction.
def mm(A,B):
    n=len(A);return [[sum(A[i][k]*B[k][j] for k in range(n))
                    for j in range(n)] for i in range(n)]
def inv(A):
    n=len(A)
    rows=[list(A[i])+[F(int(i==j)) for j in range(n)] for i in range(n)]
    for c in range(n):
        pivot=next(k for k in range(c,n) if rows[k][c])
        rows[c],rows[pivot]=rows[pivot],rows[c]
        z=rows[c][c];rows[c]=[v/z for v in rows[c]]
        for r in range(n):
            if r==c:continue
            z=rows[r][c]
            rows[r]=[v-z*w for v,w in zip(rows[r],rows[c])]
    return [row[n:] for row in rows]

def matrix_R(n,h):
    Q=[[F(int(j==(i+1)%n)-int(i==j)) for j in range(n)] for i in range(n)]
    I=[[F(int(i==j)) for j in range(n)] for i in range(n)]
    half=inv([[I[i][j]-h*Q[i][j]/2 for j in range(n)] for i in range(n)])
    whole=inv([[I[i][j]-h*Q[i][j] for j in range(n)] for i in range(n)])
    half2=mm(half,half)
    return [[2*half2[i][j]-whole[i][j] for j in range(n)] for i in range(n)]

for n in range(2,9):
    for h in (F(1,20),F(1,4),F(1,2),F(1),F(3),F(9)):
        M=matrix_R(n,h)
        for i in range(n):
            check(sum(M[i])==1,f'nonconservation {n},{h}')
            for j in range(n):
                check(M[i][j]==coeff(n,(j-i)%n,h),f'coefficient mismatch {n},{i},{j},{h}')

# Explicit low-h sign witness and large-h recovery examples.
for n in range(5,13):
    check(coeff(n,4,F(1,10000))<0,f'missing small-h negative {n}')
    check(all(coeff(n,j,F(10**7))>0 for j in range(n)),f'missing large-h positive {n}')
for h,expected in ((F(1,4),-1),(F(1,2),1)):
    check(coeff(5,4,h)*expected>0,'five-cycle witness side')
print(f'VERIFY_OK {checks} exact-arithmetic assertions')
print('critical five-cycle factor: 4*h^4*(-96-160*h+560*h^2+2240*h^3+3450*h^4+2850*h^5+1300*h^6+300*h^7+25*h^8)')
print('five-cycle threshold enclosed in (0.297835687, 0.297835689)')
