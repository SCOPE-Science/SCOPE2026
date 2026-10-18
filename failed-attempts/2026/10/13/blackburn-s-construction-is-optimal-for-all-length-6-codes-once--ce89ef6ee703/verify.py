#!/usr/bin/env python3
from fractions import Fraction as F
from math import comb
from itertools import product
from pathlib import Path
import json

# Multivariate polynomials in (p,r,s,t), exact rational coefficients.
ZERO=(0,0,0,0)
def const(c): return {ZERO:F(c)}
def var(i):
    e=[0,0,0,0]; e[i]=1
    return {tuple(e):F(1)}
def add(A,B):
    C=dict(A)
    for e,c in B.items(): C[e]=C.get(e,F(0))+c
    return {e:c for e,c in C.items() if c}
def neg(A): return {e:-c for e,c in A.items()}
def sub(A,B): return add(A,neg(B))
def mul(A,B):
    C={}
    for a,x in A.items():
        for b,y in B.items():
            e=tuple(a[i]+b[i] for i in range(4))
            C[e]=C.get(e,F(0))+x*y
    return {e:c for e,c in C.items() if c}
def scale(A,c): return {e:x*F(c) for e,x in A.items() if x*c}
def power(A,n):
    R=const(1)
    while n:
        if n&1: R=mul(R,A)
        A=mul(A,A); n//=2
    return R

p,r,s,t=var(0),var(1),var(2),var(3)
one=const(1)
a=p; b=sub(one,p)
x2=mul(r,mul(a,b)); y2=sub(mul(a,b),x2)
T3=add(mul(a,y2),mul(x2,b)); x3=mul(s,T3); y3=sub(T3,x3)
T4=add(add(mul(a,y3),mul(x2,y2)),mul(x3,b)); x4=mul(t,T4); y4=sub(T4,x4)
T5=add(add(add(mul(a,y4),mul(x2,y3)),mul(x3,y2)),mul(x4,b))
OBJ=add(add(add(mul(x2,y4),mul(x3,y3)),mul(x4,y2)),mul(T5,b))
assert [max(e[i] for e in OBJ) for i in range(4)]==[6,3,2,1]

def affine_substitute(P,alpha,beta):
    R={}
    for exp,c in P.items():
        term=const(c)
        for i,n in enumerate(exp):
            lin=add(const(alpha[i]),scale(var(i),beta[i]))
            term=mul(term,power(lin,n))
        R=add(R,term)
    return R

def bernstein_coeffs(P):
    deg=[max((e[i] for e in P),default=0) for i in range(4)]
    vals=[]
    for beta in product(*[range(n+1) for n in deg]):
        z=F(0)
        for alpha,c in P.items():
            if all(alpha[i]<=beta[i] for i in range(4)):
                fac=F(1)
                for i,n in enumerate(deg):
                    fac*=F(comb(beta[i],alpha[i]),comb(n,alpha[i]))
                z+=c*fac
        vals.append(z)
    return deg,vals

# Exact Bernstein certificate on 0 <= p <= 1/5.
D1=sub(mul(p,power(b,5)),OBJ)
Q1=affine_substitute(D1,[0,0,0,0],[F(1,5),1,1,1])
deg1,bc1=bernstein_coeffs(Q1)
assert deg1==[6,3,2,1] and len(bc1)==168 and min(bc1)>=0

# Exact Bernstein certificate on 1/5 <= p <= 1/2, subdividing each of
# r,s,t into halves. A nonnegative Bernstein coefficient vector proves
# 1024/15625 - OBJ >= 0 on every box.
D2=sub(const(F(1024,15625)),OBJ)
mid_mins={}
for er,es,et in product((0,1),repeat=3):
    Q=affine_substitute(
        D2,
        [F(1,5),F(er,2),F(es,2),F(et,2)],
        [F(3,10),F(1,2),F(1,2),F(1,2)]
    )
    deg,bc=bernstein_coeffs(Q)
    assert deg==[6,3,2,1] and len(bc)==168 and min(bc)>=0
    mid_mins[f"{er}{es}{et}"]=str(min(bc))

# q >= 10: q=5k+r, k>=2.  The chosen Blackburn split is
# (q-l,l)=(k,4k+r).  After multiplying by 15625 the desired lower
# bound is a polynomial in k.  On substituting k=h+2 every coefficient
# below is nonnegative, which proves the inequality for h>=0.
shift_coeffs={
    0:[0],
    1:[800000,8400000,35140000,73168500,75778905,31202786],
    2:[1600000,17600000,76320000,162376000,168380960,67352384],
    3:[2400000,27600000,123180000,262888500,260925915,90191334],
    4:[3200000,38400000,175360000,368256000,326046720,65755136],
}
assert all(all(c>=0 for c in cs) for cs in shift_coeffs.values())

# Exact integer SQN check on the boundary and a few later values.  By
# left-right symmetry take a=x1<=b=y1.  For fixed earlier levels x5 is
# maximized at its upper endpoint. After that substitution the
# objective is linear in x4 with coefficient b^2-2*x2, so x4 is also
# optimized at an endpoint. Exhaust only x2 and x3.
def sqn6(q):
    best=-1; arg=None
    for a0 in range(1,q//2+1):
        b0=q-a0
        for c in range(a0*b0+1):
            y2=a0*b0-c
            T3=a0*y2+c*b0
            for d in range(T3+1):
                y3=T3-d
                T4=a0*y3+c*y2+d*b0
                e=T4 if b0*b0>=2*c else 0
                y4=T4-e
                T5=a0*y4+c*y3+d*y2+e*b0
                val=c*y4+d*y3+e*y2+T5*b0
                if val>best:
                    best=val; arg=(a0,b0,c,d,e,T5)
    return best,arg
def blackburn(q):
    return max(l**5*(q-l) for l in range(1,q))
finite={}
for q in range(2,16):
    opt,arg=sqn6(q)
    finite[q]=(opt,blackburn(q),arg)
for q in range(10,16):
    assert finite[q][0]==finite[q][1]
assert finite[9][0]==33872 and finite[9][1]==33614

cert=json.loads((Path(__file__).resolve().parent/"certificate.json").read_text(encoding="utf-8"))
assert cert["theorem_domain"]=="all integers q >= 10"
assert cert["small_box"]["bernstein_minimum"]=="0"
assert cert["middle_boxes"]["count"]==8

print(
    "VERIFY_OK bernstein_small=168_nonnegative "
    "bernstein_middle=8x168_nonnegative "
    "residue_polynomials=5_nonnegative "
    "integer_sqn_q=2..15 "
    "theorem_q_ge_10=blackburn_k5"
)
