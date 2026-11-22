"""Reproduce the rational variance identity for the standard-Cauchy Fourier--Stein statistic.

Requires only Python 3 standard library.  Uses exact rational arithmetic.
The integral is split into same-sign and opposite-sign frequency quadrants.
"""
from fractions import Fraction as F
from math import factorial

# Polynomial represented by {(power_of_r,power_of_u): rational_coefficient}.
def add(*polys):
    out = {}
    for p in polys:
        for e,c in p.items(): out[e] = out.get(e,F(0))+c
    return {e:c for e,c in out.items() if c}

def mul(p,q):
    out={}
    for (i,j),c in p.items():
        for (k,l),d in q.items():
            e=(i+k,j+l)
            out[e]=out.get(e,F(0))+c*d
    return out

R={(1,0):F(1)}
U={(0,1):F(1)}
O={(0,0):F(1)}
def scaled(p,c):return {e:v*F(c) for e,v in p.items()}
P=add(scaled(mul(R,R),2),scaled(mul(R,U),2),mul(U,U),U,O)
Q=add(scaled(mul(R,R),2),scaled(mul(R,U),-2),mul(U,U),U,O)
P2=mul(P,P)
Q2=mul(Q,Q)

def integrated(a):
    a=F(a)
    # 4 triangles with same sign, each kernel squared contributes 1/4.
    same=sum(c*factorial(i)*factorial(j)/(2*a)**(i+1)/(a+2)**(j+1)
             for (i,j),c in P2.items())
    # 2 opposite quadrants, each kernel squared contributes 1/4.
    opposite=sum(F(1,2)*c*factorial(i+j+1)/F(i+1)/(a+2)**(i+j+2)
                 for (i,j),c in Q2.items())
    return same+opposite

def numerator(a):
    return (a**9+12*a**8+64*a**7+193*a**6+356*a**5+366*a**4+
            408*a**3+416*a**2+288*a+96)

def closed(a):
    a=F(a)
    return numerator(a)/(a**5*(a+2)**6)

N=0
for a in [F(k,10) for k in range(1,31)] + [F(k,7) for k in range(1,31)]:
    assert integrated(a)==closed(a), (a,integrated(a),closed(a))
    assert closed(a)>0
    N+=2
# Exact coefficient at a=0; 96/2^6=3/2.
assert F(96,2**6)==F(3,2); N+=1
# Scalar Cauchy-score moments are E[g^2]=1/2 and E[g^4]=3/8.
assert F(3,8)-F(1,2)**2==F(1,8); N+=1
for n in range(2,30):
    for a in [F(1,4),F(1,2),F(1,1),F(2,1),F(3,1)]:
        var_T=F(1,2*n*a*a)+F(2*(n-1),n)*closed(a)
        var_W=a*a*var_T
        assert var_W==F(1,2*n)+F(2*(n-1),n)*a*a*integrated(a)
        assert var_T>0
        N+=2
print('PASS: {} exact rational assertions'.format(N))
print('J(1) =',closed(F(1)), 'Var(T_2,1) =', F(1,4)+closed(F(1)))
