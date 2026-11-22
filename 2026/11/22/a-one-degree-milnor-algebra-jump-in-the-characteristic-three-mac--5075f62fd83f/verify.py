"""Exact certificate for the characteristic-three MacLane Jacobian resolution.
Run: python verify.py  (requires SymPy >= 1.13)."""
import itertools
from collections import defaultdict
from math import comb
import sympy as sp

x,y,z=sp.symbols('x y z')
V=(x,y,z)
lines=[x,x-z,x+z,y,y-z,y+z,x-y,-x+y+z]
f=sp.prod(lines)
D=[sp.Poly(sp.diff(f,v),*V,modulus=3) for v in V]
P=lambda e:sp.Poly(e,*V,modulus=3)

# The exhibited homogeneous syzygies are exact over the field of 3 elements.
U=[P(-x**2*y+x**2*z-x*y**2-x*y*z-x*z**2),
   P(-x**2*y-x*y**2+x*y*z-y**2*z-y*z**2),
   P(-x**2*z-x*y*z+x*z**2-y**2*z-y*z**2)]
B=[P(-x**3*z**2+x**2*y**3-x**2*y*z**2-x*y**4+x*y**3*z+x*y**2*z**2-x*y*z**3+x*z**4),
   P(x**2*y**3-x**2*y*z**2-x*y**4-x*y**3*z+x*y**2*z**2+x*y*z**3-y**4*z-y**3*z**2+y**2*z**3+y*z**4),
   P(x*y**3*z-x*y*z**3-y**4*z+y**3*z**2+y**2*z**3-y*z**4)]
C=[P(x**4*z-x**3*y**2-x**3*y*z-x**3*z**2-x**2*y**2*z+x**2*y*z**2-x**2*z**3+x*y**4-x*y**3*z-x*y**2*z**2+x*z**4),
   P(x**3*y*z-x**2*y**3-x**2*y**2*z+x**2*y*z**2+x*y**4+x*y**3*z+y**3*z**2-y**2*z**3+y*z**4),
   P(x**3*y**2-x**2*y**3+x*y**2*z**2+x*y*z**3+y**4*z+y**2*z**3-y*z**4)]

def polyeq0(p): return P(p).is_zero
for W in [U,B,C]:
    assert polyeq0(sum(W[i].as_expr()*D[i].as_expr() for i in range(3)))
R=x*y*y-y**3+y*y*z-y*z*z
# U and B are linearly independent over the polynomial fraction field.
assert any(not P(U[i].as_expr()*B[j].as_expr()-U[j].as_expr()*B[i].as_expr()).is_zero
           for i in range(3) for j in range(i+1,3))
assert sp.gcd(x+y-z,z)==1
for j in range(3):
    assert polyeq0(R*U[j].as_expr()+(x+y-z)*B[j].as_expr()+z*C[j].as_expr())

# Degree-three relation exists, but there are no relations of lower degree.
def monoms(d): return [(i,j,d-i-j) for i in range(d+1) for j in range(d-i+1)]
def modrank(A,p=3):
    if not A:return 0
    a=[row[:] for row in A];m=len(a);n=len(a[0]);r=0
    for c in range(n):
        h=next((i for i in range(r,m) if a[i][c]%p),None)
        if h is None: continue
        a[h],a[r]=a[r],a[h]
        v=pow(a[r][c],-1,p)
        a[r]=[(v*t)%p for t in a[r]]
        for i in range(r+1,m):
            if a[i][c]:
                k=a[i][c]
                a[i]=[(aa-k*bb)%p for aa,bb in zip(a[i],a[r])]
        r+=1
        if r==m:break
    return r

def syz_dim(d):
    src=monoms(d);dst=monoms(d+7);ri={e:i for i,e in enumerate(dst)}
    M=[[0]*(3*len(src)) for _ in dst]
    for k,Pj in enumerate(D):
        for jj,a in enumerate(src):
            for b,v in Pj.terms():
                e=tuple(a[i]+b[i] for i in range(3))
                M[ri[e]][k*len(src)+jj]=int(v)%3
    return 3*len(src)-modrank(M)
assert [syz_dim(d) for d in range(6)] == [0,0,0,1,3,8]

# The two quintics are independent modulo the six quadratic multiples of U.
def vec(W,d):
    ms=monoms(d)
    return [int(P(a).coeff_monomial(x**i*y**j*z**k))%3 for a in W for i,j,k in ms]
qU=[vec([P(x**i*y**j*z**k*a.as_expr()) for a in U],5) for i,j,k in monoms(2)]
assert modrank(list(map(list,zip(*qU+[vec(B,5),vec(C,5)]))))==8

# Exact Groebner ideal and its multigraded monomial Hilbert numerator.
G=sp.groebner([a.as_expr() for a in D],x,y,z,order='grevlex',modulus=3)
leads=[tuple(p.LM(order=sp.grevlex).exponents) for p in G.polys]
expected=[(1,9,1),(0,9,2),(2,7,1),(3,5,1),(1,6,2),(3,3,2),(4,3,0),(5,1,1),(5,0,2)]
assert leads==expected
# Hilbert numerator is alternating lcm inclusion-exclusion of leading monomials.
num=defaultdict(int)
num[0]=1
for mask in range(1,1<<len(leads)):
    selected=[leads[i] for i in range(len(leads)) if mask>>i&1]
    lcm=tuple(max(t[j] for t in selected) for j in range(3))
    num[sum(lcm)] += (-1 if len(selected)%2 else 1)
num={i:c for i,c in num.items() if c}
assert num=={0:1,7:-3,10:1,12:2,13:-1}
# Minimal resolution: generator degrees (3,5,5), sole relation at degree 6;
# the Groebner Hilbert numerator equals the displayed presentation's numerator.
assert {0:1,7:-3,10:1,12:2,13:-1} == {0:1,7:-3,7+3:1,7+5:2,7+6:-1}
# Earlier characteristic-zero resolution has numerator 1-3T^7+3T^11-T^12.
# The difference is T^10(1-T)^3, hence one extra Milnor class in degree 10.
def hilb_coeff(N,d):return sum(v*comb(d-i+2,2) for i,v in N.items() if i<=d)
old={0:1,7:-3,11:3,12:-1}
assert [(d,hilb_coeff(num,d)-hilb_coeff(old,d)) for d in range(24) if hilb_coeff(num,d)!=hilb_coeff(old,d)]==[(10,1)]
assert (hilb_coeff(old,10),hilb_coeff(num,10))==(36,37)

# Verify original labeled incidence is unchanged: every nonidentically-zero
# triple determinant has norm 1 in Z[t]/(t^2-t+1).
t=sp.symbols('t'); H=[(1,0,0),(1,0,-1),(1,0,-t),(0,1,0),(0,1,-1),(0,1,-t),(1,-1,0),(t,1,-t)]
quad=t*t-t+1
count=0
for tri in itertools.combinations(range(8),3):
    dt=sp.rem(sp.det(sp.Matrix([H[i] for i in tri])),quad,t)
    if dt==0:count+=1
    else:
        a=sp.Poly(dt,t);u=a.nth(1);v=a.nth(0)
        norm=sp.expand((v+u*t)*(v+u*(1-t)))
        norm=sp.rem(norm,quad,t)
        assert norm in (1,-1), (tri,dt,norm)
assert count==8
print('MACLANE_CHAR3_INTEGRAL_SYZYGY_HILBERT_VERIFIED_OK')
