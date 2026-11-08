#!/usr/bin/env python3
"""Exact checks for a characteristic-two quartic secant-scroll model.
Requires Python 3 and SymPy. All polynomial identities are reduced modulo two.
These checks corroborate the accompanying geometric proof and do not replace it.
"""
import sympy as S
x0,x1,x2,x3,s,t,u,v=S.symbols('x0 x1 x2 x3 s t u v')
q0=x0*x2+x1**2
q1=x0*x3+x1*x2
q2=x1*x3+x2**2
F=S.expand((q0+q1+q2)**2+q0*q2)

def zero2(expr,variables):
    return all(int(c)%2==0 for c in S.Poly(S.expand(expr),*variables).coeffs())

assert zero2(x2*q0+x1*q1+x0*q2,(x0,x1,x2,x3))
assert zero2(x3*q0+x2*q1+x1*q2,(x0,x1,x2,x3))
Cpoint={x0:u**3,x1:u**2*v,x2:u*v**2,x3:v**3}
assert all(zero2(q.subs(Cpoint, simultaneous=True),(u,v)) for q in (q0,q1,q2))
assert zero2(F.subs(Cpoint,simultaneous=True),(u,v))
assert all(zero2(S.diff(F,x).subs(Cpoint,simultaneous=True),(u,v)) for x in (x0,x1,x2,x3))
print('TWISTED_CUBIC_SYZYGIES_AND_SINGULAR_CONTAINMENT_PASSED')

# On Gamma=[s^2:s^2+st+t^2:t^2], the preimage of the twisted cubic
# is the (2,2) curve f=0 in Gamma x C.
B=s*s+s*t+t*t
f=S.expand(t*t*u*u+B*u*v+s*s*v*v)
assert zero2(S.diff(f,s)-t*u*v,(s,t,u,v))
assert zero2(S.diff(f,t)-s*u*v,(s,t,u,v))
assert zero2(S.diff(f,u)-B*v,(s,t,u,v))
assert zero2(S.diff(f,v)-B*u,(s,t,u,v))
# These four derivatives imply uv=0, B=0. The equation f=0 then
# forces t=0 (if v=0), or s=0 (if u=0), contradicting B=0.
print('INCIDENCE_CURVE_SMOOTHNESS_JACOBIAN_CERTIFICATE_PASSED')

# The map to C has quadratic in (s,t):
assert zero2(f-(u*v+v*v)*s*s-u*v*s*t-(u*u+u*v)*t*t,(s,t,u,v))
# Its mixed coefficient is uv. Both geometric branch points are simple
# roots of uv on C; at each, the quadratic has exactly one root in Gamma.
print('TWO_DISTINCT_WILD_BRANCH_SUPPORTS_PASSED')

# At p=(u:v)=(1:z), q=(s:t)=(1:w), the local defining equation is:
w,z=S.symbols('w z')
local=S.expand(f.subs({s:1,t:w,u:1,v:z}, simultaneous=True))
assert zero2(local-(w*w+(1+w+w*w)*z+z*z),(w,z))
# Hensel expansion z(w) = w^2 + w^3 modulo w^4.
zapprox=w*w+w**3
assert all(int(c)%2==0 for mon,c in S.Poly(S.expand(local.subs(z,zapprox)),w).terms() if mon[0]<4)
# The first nonzero formal derivative of z(w) is w^2:
assert zero2(S.diff(zapprox,w)-w*w,(w,))
print('RAMIFICATION_INDEX_TWO_DIFFERENT_EXPONENT_TWO_PASSED')

# Restriction of the universal rank-two quotient bundle to Gamma is
# balanced: exact Serre-dual 8x8 test for H^0(Q(-3))=0.
A=t*t;C=s*s
basis=(s**3,s*s*t,s*t*t,t**3)
cols=[]
for j in range(4):
    for mon in (s,t):
        vs=[0,0,0,0];vs[j]=mon
        exprs=(S.expand(A*vs[0]+B*vs[1]+C*vs[2]),
               S.expand(A*vs[1]+B*vs[2]+C*vs[3]))
        cols.append([S.Poly(E,s,t).coeff_monomial(m) for E in exprs for m in basis])
M=S.Matrix(cols).T
assert abs(int(M.det()))==1
print('BALANCED_NORMALIZATION_8X8_DETERMINANT',int(M.det()))

# A corroborative exact finite-field point count for the conductor at q=2.
pts=[(1,0),(0,1),(1,1)]
count=0
for ss,tt in pts:
    for uu,vv in pts:
        val=(tt*tt*uu*uu+(ss*ss+ss*tt+tt*tt)*uu*vv+ss*ss*vv*vv)%2
        count+=(val==0)
assert count==4
print('CONDUCTOR_F2_RATIONAL_POINTS',count)
print('ALL_EXACT_CHECKS_PASSED')

# Exhaustive independent counts over the first four binary extensions.
# Each nonzero projective vector has one representative with leading 1.
IRREDUCIBLE = {1:0b11, 2:0b111, 3:0b1011, 4:0b10011}
def field_mul(a,b,m):
    poly=IRREDUCIBLE[m];mask=(1<<m)-1;acc=0
    while b:
        if b & 1:acc ^= a
        b >>= 1
        a <<= 1
        if a & (1<<m):a ^= poly
    return acc & mask

def projective_points(n,q):
    import itertools
    for first in range(n):
        for tail in itertools.product(range(q),repeat=n-first-1):
            yield (0,)*first+(1,)+tail

def poly_x(F,m):
    a,b,c,d=F
    mul=lambda x,y:field_mul(x,y,m)
    A=mul(a,c)^mul(b,b)
    B=mul(a,d)^mul(b,c)
    C=mul(b,d)^mul(c,c)
    return mul(A^B^C,A^B^C)^mul(A,C)

def poly_e(SUV,m):
    s,t,u,v=SUV
    mul=lambda x,y:field_mul(x,y,m)
    t2=mul(t,t);s2=mul(s,s);u2=mul(u,u);v2=mul(v,v)
    b=s2^mul(s,t)^t2
    return mul(t2,u2)^mul(b,mul(u,v))^mul(s2,v2)

T_old,T_prev=2,-1
for m in range(1,5):
    q=1<<m
    E=sum(poly_e((s,t,u,v),m)==0 for s,t in projective_points(2,q) for u,v in projective_points(2,q))
    X=sum(poly_x(p,m)==0 for p in projective_points(4,q))
    T = -1 if m==1 else -T_prev-2*T_old
    assert E==q+1-T,(q,E,T)
    assert X==(q+1)**2+T,(q,X,T)
    print('EXTENSION_FIELD_COUNT',q,'CONDUCTOR',E,'SURFACE',X,'TRACE',T)
    if m>=2:
        T_old,T_prev=T_prev,T
print('BINARY_EXTENSION_ZETA_CHECKS_PASSED')
