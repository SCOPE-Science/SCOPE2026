"""Exact characteristic-five identities for a reciprocal genus-three family.

Requires SymPy. Run: python verify_howe_rank.py
All infinite-field assertions reduce to polynomial identities and factorization over GF(5).
"""
import sympy as S

a,b,x,z,t = S.symbols('a b x z t')
f = x**8 + a*x**6 + b*x**4 + a*x**2 + 1

def modpoly(g, *vars):
    return S.Poly(S.expand(g), *vars, modulus=5)

def eq5(u,v, *vars):
    return modpoly(u-v,*vars).is_zero

F2=S.Poly(S.expand(f*f),x)
M=S.Matrix(3,3,lambda i,j:F2.nth(5*(i+1)-(j+1)))
A=a*a+2*b; B=2*a; C=2*a*a+b*b+2
assert M == S.Matrix([[A,0,B],[0,C,0],[B,0,A]])
P=S.Matrix([[1,1,0],[0,0,1],[1,-1,0]])
assert P.det()!=0
assert eq5((P.inv()*M*P)[0,0],A+B,a,b)
assert eq5((P.inv()*M*P)[1,1],A-B,a,b)
assert eq5((P.inv()*M*P)[2,2],C,a,b)
assert all(eq5((P.inv()*M*P)[i,j],0,a,b) for i in range(3) for j in range(3) if i!=j)

Delta=S.discriminant(f,x)
Delta_exp = 256*(2*a-b-2)**2*(2*a+b+2)**2*(a*a-4*b+8)**4
assert S.expand(Delta-Delta_exp)==0

# Three genus-one quotient equations; these are identities of function fields.
h0=t**4 + a*t**3 + b*t**2 + a*t +1
hp=t**4+(a-4)*t*t+(b-2*a+2)
hm=t**4+(a+4)*t*t+(b+2*a+2)
assert S.expand(h0.subs(t,x*x)-f)==0
assert S.cancel(x**4*hp.subs(t,x+1/x)-f)==0
assert S.cancel(x**4*hm.subs(t,x-1/x)-f)==0
assert eq5(S.Poly(S.expand(h0*h0),t).nth(4),C,a,b)
assert eq5(S.Poly(S.expand(hp*hp),t).nth(4),A-B,a,b)
assert eq5(S.Poly(S.expand(hm*hm),t).nth(4),A+B,a,b)

# Solve pairwise vanishing loci on the smooth parameter space.
Bp=2*a*a+4*a # A+B=0
Bm=2*a*a+a   # A-B=0
assert eq5((A+B).subs(b,Bp),0,a)
assert eq5((A-B).subs(b,Bm),0,a)
assert eq5(C.subs(b,Bp),-(a+2)*(a-1)**3,a)
assert eq5(C.subs(b,Bm),-(a-2)*(a+1)**3,a)
assert eq5((A+B)-(A-B),4*a,a)
assert eq5((A+B).subs({a:0,b:0}),0,a)
assert eq5(C.subs({a:0,b:0}),2,a)
for aa,bb in [(0,0),(2,0),(3,0)]:
    assert Delta_exp.subs({a:aa,b:bb}) % 5 != 0
    assert sum((v.subs({a:aa,b:bb}) % 5)!=0 for v in [A+B,A-B,C])==1
for aa,bb in [(1,1),(4,1)]:
    assert Delta_exp.subs({a:aa,b:bb}) % 5 == 0
# Reducedness of each of the three rank-one points.
assert S.det(S.Matrix([[S.diff(A+B,a),S.diff(A+B,b)],
                           [S.diff(A-B,a),S.diff(A-B,b)]])).subs({a:0,b:0}) % 5 != 0
assert modpoly(S.diff(C.subs(b,Bp),a),a).eval(3) % 5 != 0
assert modpoly(S.diff(C.subs(b,Bm),a),a).eval(2) % 5 != 0

# Geometric isomorphism of three exceptional models, via Mobius and scaling.
f3=z**8+3*z**6+3*z**2+1
f2=z**8+2*z**6+2*z**2+1
assert eq5((z-1)**8+(z+1)**8,2*f3,z)
assert eq5(f3.subs(z,2*z),f2,z)

# Independent finite-field check using quadratic-character point counts
# for all 13 smooth F5 parameter choices.
def chi(v):
    v=int(v)%5
    return (0 if v==0 else (1 if v in (1,4) else -1))
def elliptic_N(aa,bb,kind):
    if kind==0: return 7+sum(chi(u**4+aa*u**3+bb*u*u+aa*u+1) for u in range(5))
    if kind==1: return 7+sum(chi(u**4+(aa-4)*u*u+bb-2*aa+2) for u in range(5))
    return 7+sum(chi(u**4+(aa+4)*u*u+bb+2*aa+2) for u in range(5))
def genus3_N(aa,bb):
    return 7+sum(chi(u**8+aa*u**6+bb*u**4+aa*u*u+1) for u in range(5))
counts={1:0,2:0,3:0}
for aa in range(5):
    for bb in range(5):
        if int(Delta_exp.subs({a:aa,b:bb}))%5==0:continue
        vals=[int(v.subs({a:aa,b:bb}))%5 for v in (A+B,A-B,C)]
        rank=sum(bool(v) for v in vals)
        counts[rank]+=1
        nums=[elliptic_N(aa,bb,kind) for kind in range(3)]
        assert sum(nums)-12 == genus3_N(aa,bb)
        assert sum(((6-num)%5)!=0 for num in nums)==rank
assert counts=={1:3,2:6,3:4},counts
print('HOWE5_RANK_STRATIFICATION_PASS eigenvalues=3 rank1=3 reduced=3 classes=1 GF5=',counts)
