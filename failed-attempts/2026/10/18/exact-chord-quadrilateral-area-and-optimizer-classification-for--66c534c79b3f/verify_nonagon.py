#!/usr/bin/env python3
"""Exact exhaustive certificate for minimal chord quadrilaterals of a regular nonagon.

Only the Python standard library is required. Algebra takes place in
Q[c]/(8*c**3-6*c-1), c=cos(pi/9). Rational root isolation and exact
field operations decide every strict and non-strict comparison.
"""
from fractions import Fraction as F
from itertools import combinations, product
from math import comb, cos, pi, sin

ZERO = (F(0), F(0), F(0))
ONE = (F(1), F(0), F(0))
C = (F(0), F(1), F(0))

def add(a, b):
    return tuple(x+y for x, y in zip(a, b))

def neg(a):
    return tuple(-v for v in a)

def sub(a, b):
    return add(a, neg(b))

def mul(a, b):
    z = [F(0) for _ in range(5)]
    for i in range(3):
        for j in range(3):
            z[i+j] += a[i]*b[j]
    # c**3 = (6*c+1)/8 and c**4=(6*c**2+c)/8.
    return (z[0]+z[3]/8, z[1]+3*z[3]/4+z[4]/8,
            z[2]+3*z[4]/4)

def integer(n):
    return (F(n), F(0), F(0))

def scale(a, z):
    return tuple(v*z for v in a)

def inverse(a):
    """Solve a*b=1 over Q by 3-by-3 rational elimination."""
    basis=[ONE,C,(F(0), F(0), F(1))]
    columns=[mul(a, e) for e in basis]
    m=[[columns[j][i] for j in range(3)]+[ONE[i]] for i in range(3)]
    for i in range(3):
        pivot=next((j for j in range(i, 3) if m[j][i]), None)
        assert pivot is not None, ('not invertible', a)
        m[i],m[pivot]=m[pivot],m[i]
        d=m[i][i]
        m[i]=[u/d for u in m[i]]
        for j in range(3):
            if j!=i:
                d=m[j][i]
                m[j]=[u-d*v for u,v in zip(m[j],m[i])]
    ans=tuple(m[i][3] for i in range(3))
    assert mul(a,ans)==ONE
    return ans

# Rational isolating interval for c=cos(pi/9).
LOW=F(93969262078590838405,10**20)
HIGH=LOW+F(1,10**20)
def cubic(t):
    return 8*t**3-6*t-1
assert cubic(LOW)<0<cubic(HIGH)
assert LOW>F(1,2)  # The cubic is strictly increasing on this interval.

def sign(p):
    if p==ZERO:
        return 0
    a=b=F(0)
    for power,v in enumerate(p):
        if v>=0:
            a+=v*LOW**power
            b+=v*HIGH**power
        else:
            a+=v*HIGH**power
            b+=v*LOW**power
    if a>0:
        return 1
    if b<0:
        return -1
    raise ArithmeticError(('insufficient isolating precision',p,a,b))

# Chebyshev recurrences in the cubic field.
T=[ONE,C]
U=[ONE,scale(C,2)]
for j in range(2,19):
    T.append(sub(scale(mul(C,T[-1]),2),T[-2]))
    U.append(sub(scale(mul(C,U[-1]),2),U[-2]))
assert T[9]==neg(ONE) and T[18]==ONE
assert U[8]==ZERO and U[17]==ZERO
S={0:ZERO}
for i in range(1,19):
    S[i]=U[i-1]
    S[-i]=neg(U[i-1])
# sin(d*pi/9)/sin(pi/9) = S[d].

# E = 2*sin(pi/9)*area = sum over successive pairs:
# [2*h_i*h_j-(h_i**2+h_j**2)*cos(gap*pi/9)] / U_(gap-1)(c).
EDGE={}
for parity_a,parity_b,d in product((0,1),(0,1),range(1,9)):
    ha=C if parity_a else ONE
    hb=C if parity_b else ONE
    numerator=sub(scale(mul(ha,hb),2),
                  mul(add(mul(ha,ha),mul(hb,hb)),T[d]))
    EDGE[parity_a,parity_b,d]=mul(numerator,inverse(U[d-1]))


def quad_value(indices):
    gaps=[indices[i+1]-indices[i] for i in range(3)]
    gaps.append(indices[0]+18-indices[3])
    if max(gaps)>=9:  # The support normals lie in a closed semicircle.
        return None
    for i in range(4):
        a=indices[i]
        b=indices[i+1] if i<3 else indices[0]+18
        ha=C if a%2 else ONE
        hb=C if b%2 else ONE
        for k in indices:
            hk=C if k%2 else ONE
            # Adjacent support-line intersection v must obey u_k.v <= h_k.
            # Divide by positive sin((b-a)*pi/9), then clear sin(pi/9).
            violation=sub(add(mul(ha,S[b-k]),mul(hb,S[k-a])),
                          mul(hk,S[b-a]))
            if sign(violation)>0:
                return None
    E=ZERO
    for i in range(4):
        a=indices[i]
        b=indices[(i+1)%4]
        E=add(E,EDGE[a%2,b%2,gaps[i]])
    return E

best=None
minimizers=[]
feasible=0
bounded=0
for t in combinations(range(18),4):
    gaps=[t[1]-t[0],t[2]-t[1],t[3]-t[2],t[0]+18-t[3]]
    bounded+=max(gaps)<9
    val=quad_value(t)
    if val is None:
        continue
    feasible+=1
    if best is None or sign(sub(val,best))<0:
        best=val
        minimizers=[t]
    elif sign(sub(val,best))==0:
        minimizers.append(t)

EXPECTED=(F(5,4),F(-1,2),F(2))
assert best==EXPECTED, best
assert feasible==1548, feasible
assert len(minimizers)==9, minimizers
assert (0,5,9,13) in minimizers
assert sign(sub(quad_value((1,5,9,15)),best))>0
assert comb(18,4)==3060
print('EXACT_NONAGON_CHORD_QUADRILATERAL_CERTIFICATE_OK')
print('candidate_4tuples',comb(18,4),'bounded',bounded,'feasible',feasible)
print('minimum E=2*sin(pi/9)*area',best)
print('all minimizing normal index tuples',minimizers)
c=cos(pi/9)
area=(float(best[0])+float(best[1])*c+float(best[2])*c*c)/(2*sin(pi/9))
print('area for circumradius 1',format(area,'.15g'))
print('area ratio to regular nonagon',format(area/(9/2*sin(2*pi/9)),'.15g'))
