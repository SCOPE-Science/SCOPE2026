"""Independent rational-integral checks for quaternionic-projective cap spectrum.

Run with Python 3; standard library only. Finite tests corroborate the proof,
not constitute a proof for all projective dimensions and cap sizes.
"""
from fractions import Fraction as F
from math import comb, exp

def integral(k, m, t):
    """Exact integral from t to 1 of s**k (1-s)**m ds."""
    return sum(((-1)**j)*comb(m,j)*(1-t**(k+j+1))/F(k+j+1)
               for j in range(m+1))

def raw_eigen(d,t):
    m=2*d-3
    varint=lambda z: integral(3,m,z)-F(2,d)*integral(2,m,z)+F(1,d*d)*integral(1,m,z)
    return (varint(t)/varint(F(0)),
            integral(2,m+1,t)/integral(2,m+1,F(0)),
            integral(1,m+2,t)/integral(1,m+2,F(0)))

def closed_eigen(d,t):
    z=1-t
    A=z**(2*d-2)*(1+2*(d-1)*t-(2*d-1)*(d+2)*t*t+2*d*d*(2*d-1)*t**3)
    C=z**(2*d-1)*(1+(2*d-1)*t+d*(2*d-1)*t*t)
    T=z**(2*d)*(1+2*d*t)
    return A,C,T

def volume(d,t):
    return (1-t)**(2*d-2)*(1+(2*d-2)*t)

checks=0
for d in range(3,13):
    mult=(1,4*(d-1),2*d*d-5*d+2)
    D=2*d*d-d-1
    assert sum(mult)==D and mult[2]>0
    for t in (F(1,7*d),F(1,2*d),F(3,4*d),F(1,d),F(2,d),F(d-1,d)):
        A,C,T=closed_eigen(d,t)
        assert raw_eigen(d,t)==(A,C,T), (d,t,'integral mismatch')
        assert A-C==(4*d*d-1)*t*t*(1-t)**(2*d-2)*(d*t-1)
        assert C-T==d*(2*d+1)*t*t*(1-t)**(2*d-1)
        assert A-T==(d-1)*(2*d+1)*t*t*(1-t)**(2*d-2)*(2*d*t-1)
        assert mult[0]*A+mult[1]*C+mult[2]*T == D*volume(d,t)
        assert all(0<q<1 for q in (A,C,T))
        if t < F(1,2*d): assert A<T<C
        elif t == F(1,2*d): assert A==T<C
        elif t < F(1,d): assert T<A<C
        elif t == F(1,d): assert T<A==C
        else: assert T<C<A
        checks+=1

for u in (0.5,1.,1.5,2.,3.,5.):
    # Cap heights t=u/(2d) and the universal u fixed-volume limit.
    limA=exp(-u)*(1+u-u*u/2+u**3/2)
    limC=exp(-u)*(1+u+u*u/2)
    limT=exp(-u)*(1+u)
    A,C,T=map(float,closed_eigen(3000,F.from_float(u/6000)))
    assert abs(A-limA)<0.002 and abs(C-limC)<0.002 and abs(T-limT)<0.002

print(f'HP_CAP_EXACT_RATIONAL_PASS dimensions=3..12 cases={checks}')
print('HP_CAP_ALL_BRANCH_ORDER_TRACE_PASS')
print('HP_CAP_FIXED_VOLUME_SCALING_NUMERIC_PASS')
