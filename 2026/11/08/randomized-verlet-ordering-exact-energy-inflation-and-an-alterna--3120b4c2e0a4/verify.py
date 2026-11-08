"""Exact-rational checks for a two-order Verlet oscillator theorem.

Run with Python 3; no third-party libraries required.
These finite tests supplement the analytic polynomial proof in RESULT.md.
"""
from fractions import Fraction as F
from itertools import product

CHECKS = 0

def check(cond):
    global CHECKS
    CHECKS += 1
    if not cond:
        raise AssertionError('exact check failed at assertion {}'.format(CHECKS))

def mm(A, B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(len(B)))
                       for j in range(len(B[0]))) for i in range(len(A)))

def tr(A):
    return tuple(zip(*A))

def eye(n):
    return tuple(tuple(F(i == j) for j in range(n)) for i in range(n))

def det2(A):
    return A[0][0]*A[1][1]-A[0][1]*A[1][0]

def det3(A):
    return (A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])
            -A[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0])
            +A[0][2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0]))

def sub(A,B):
    return tuple(tuple(A[i][j]-B[i][j] for j in range(len(A[0])))
                 for i in range(len(A)))

def add(A,B):
    return tuple(tuple(A[i][j]+B[i][j] for j in range(len(A[0])))
                 for i in range(len(A)))

def scale(a,A):
    return tuple(tuple(a*v for v in row) for row in A)

def maps(h):
    d=F(1)-h*h/2
    c=F(1)-h*h/4
    A=((d,h*c),(-h,d))
    B=((d,h),(-h*c,d))
    return A,B

def transfer(M):
    a,b=M[0]
    c,d=M[1]
    return ((a*a,2*a*b,b*b),(a*c,a*d+b*c,b*d),(c*c,2*c*d,d*d))

def norm_sq(x):
    return sum(z*z for z in x)

for denom in range(2,11):
    for num in range(1,2*denom):
        h=F(num,denom)
        A,B=maps(h)
        check(det2(A)==1)
        check(det2(B)==1)
        kappa=1+h**6/F(32)
        gram=scale(F(1,2),add(mm(tr(A),A),mm(tr(B),B)))
        check(gram==scale(kappa,eye(2)))
        P=mm(A,B)
        check(det2(P)==1)
        traceP=P[0][0]+P[1][1]
        check(traceP==2-4*h*h+h**4-h**6/F(16))
        check(traceP-2==-h*h*(h*h-8)**2/F(16))
        check(traceP+2==-(h*h-4)*(h*h-2*h-4)*(h*h+2*h-4)/F(16))
        for p in [F(1,8),F(1,4),F(1,2),F(3,4),F(7,8)]:
            TA,TB=transfer(A),transfer(B)
            T=add(scale(p,TA),scale(1-p,TB))
            check(det3(sub(eye(3),T))==-h**8*p*(1-p)*(8-h*h)**2/F(128))

for h in (F(1,3),F(2,3),F(1),F(3,2)):
    A,B=maps(h)
    kappa=1+h**6/F(32)
    for x0 in ((F(1),F(0)),(F(1),F(2)),(F(-2),F(3))):
        for n in range(0,9):
            total=F(0)
            for bits in product((0,1),repeat=n):
                x=tuple(x0)
                for bit in bits:
                    M=(A,B)[bit]
                    x=(M[0][0]*x[0]+M[0][1]*x[1],M[1][0]*x[0]+M[1][1]*x[1])
                total+=norm_sq(x)
            check(total/F(2**n)==kappa**n*norm_sq(x0))

for h in (F(1,2),F(1),F(6,5),F(5,4),F(3,2),F(7,4)):
    A,B=maps(h)
    P=mm(A,B)
    t=sum(P[i][i] for i in range(2))
    check((t>-2)==(h*h+2*h-4<0))
print('PASS: {} exact-rational assertions'.format(CHECKS))
