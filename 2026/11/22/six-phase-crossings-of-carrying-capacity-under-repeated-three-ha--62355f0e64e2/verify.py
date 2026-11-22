"""Standalone exact-algebra checks and finite numerical examples for the three-habitat theorem.
Requires only the Python 3 standard library. This does not substitute for an asymptotic proof.
"""
from fractions import Fraction as F
from decimal import Decimal, getcontext

getcontext().prec = 75
q = F(1, 3)
D = [[F(1,2), F(0), F(1,2)],
     [F(1,2), F(1,2), F(0)],
     [F(0), F(1,2), F(1,2)]]
P = [[q]*3 for _ in range(3)]
I = [[F(i == j) for j in range(3)] for i in range(3)]
xstar = [F(2,3),F(1),F(4,3)]
b = [z-F(1) for z in xstar]
a = [F(2,9), F(1,2), F(4,9)]
h = [4,-1,-5,-4,1,5]

def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(3)) for j in range(3)] for i in range(3)]

def power(A,n):
    ans=I
    for _ in range(n): ans=mm(ans,A)
    return ans

def mv(A,v):
    return [sum(A[i][j]*v[j] for j in range(3)) for i in range(3)]

def dot(u,v): return sum(x*y for x,y in zip(u,v))

assert sum(xstar)==3
assert sum(b)==0
assert sum(a)/3==F(7,18)
assert mm(D,P)==P and mm(P,D)==P
assert mm(P,P)==P
assert power(D,6)==[[P[i][j]+F(1,64)*(I[i][j]-P[i][j]) for j in range(3)] for i in range(3)]
for k in range(1,73):
    observed=dot(a,mv(power(D,k),b))/F(11,18)
    predicted=F(h[k%6],33*2**k)
    assert observed==predicted,(k,observed,predicted)

K = [F(1,2),F(1),F(3,2)]
r = [1,1,3]
def g(z,idx):
    return F(1+r[idx])*K[idx]*z/(K[idx]+r[idx]*z)
assert [g(F(1),i) for i in range(3)]==xstar
assert [F(1+r[i])*K[i]*K[i]/(K[i]+r[i])**2 for i in range(3)]==a

def dec(x): return Decimal(x.numerator)/Decimal(x.denominator)
def dec_mat(A): return [[dec(x) for x in row] for row in A]
def fp(k):
    mat = dec_mat(power(D,k))
    z=[dec(x) for x in xstar]
    vals=[dec(t) for t in K]
    for _ in range(1200):
        y=[sum(mat[i][j]*z[j] for j in range(3)) for i in range(3)]
        nxt=[Decimal(1+r[i])*vals[i]*y[i]/(vals[i]+Decimal(r[i])*y[i]) for i in range(3)]
        if max(abs(nxt[i]-z[i]) for i in range(3))<Decimal('1e-65'):
            return nxt
        z=nxt
    raise RuntimeError('numerical iteration did not converge')

for k in range(4,31):
    z=fp(k)
    diff=sum(z)-Decimal(3)
    pred=dec(F(h[k%6],33*2**k))
    assert diff*pred>0,(k,diff,pred)
    if k>=8:
        assert abs(diff/pred-1)<Decimal('.02'), (k,diff/pred)
print('PASS: exact six-step spectral identity and 72 rational coefficient checks')
print('PASS: verified local recruitment/fixed-point derivatives')
print('PASS: 27 high-precision positive-equilibrium checks (k=4,...,30)')
print('LIMITATION: finite checks cannot prove eventual signs; that follows from analytic perturbation.')
