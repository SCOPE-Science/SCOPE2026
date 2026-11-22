"""Exact checks for a rooted-tree conjugate-gradient sign theorem.
Run: python verify.py (requires SymPy >= 1.12)."""
from fractions import Fraction
import itertools
import sympy as S

z=S.symbols('z', real=True)
P=6*z**5-193*z**4+732*z**3-1715*z**2+1200*z-1200
Q=72*z**6-165*z**5-348*z**4+9849*z**3-8630*z**2+3600*z+5600
P1=24*z**5-115*z**4+594*z**3-345*z**2+400
P4=9*z**5+84*z**4-441*z**3+1930*z**2-1200*z+1400

def variations(seq):
    a=[int(S.sign(x)) for x in seq if x!=0]
    return sum(v!=w for v,w in zip(a,a[1:]))

def sturm_counts(poly):
    chain=S.sturm(poly,z)
    at_zero=variations([S.expand(g).subs(z,0) for g in chain])
    at_inf=variations([S.LC(S.Poly(g,z)) for g in chain])
    return at_zero,at_inf

assert sturm_counts(P)==(3,2), sturm_counts(P)
assert sturm_counts(P1)==(2,2), sturm_counts(P1)
assert sturm_counts(P4)==(2,2), sturm_counts(P4)
assert P.subs(z,28)<0<P.subs(z,29)

def mat(edges,nn,mu):
    A=S.eye(nn)*mu
    for i,j,w in edges:
        A[i,i]+=w; A[j,j]+=w; A[i,j]-=w; A[j,i]-=w
    return A

def cg_iterates(A,root):
    n=A.rows
    b=S.eye(n)[:,root];x=S.zeros(n,1);r=b;p=r
    out=[]
    for k in range(n):
        ar=A*p
        step=S.factor(r.dot(r)/p.dot(ar))
        x=S.simplify(x+step*p)
        out.append(x)
        nr=S.simplify(r-step*ar)
        if all(q==0 for q in nr):break
        beta=S.factor(nr.dot(nr)/r.dot(r))
        p=S.simplify(nr+beta*p)
        r=nr
    return out

for val in [S.Rational(1,2),1,2,5,10,28,29,30,50]:
    edges=[(0,1,S.Integer(5)),(0,2,S.Integer(1)),(0,4,S.Rational(val)),(2,3,2*S.Rational(val))]
    A=mat(edges,5,S.Integer(1))
    xs=cg_iterates(A,0)
    assert len(xs)>=3
    third=xs[2]
    assert S.factor(third[2]+P.subs(z,val)/Q.subs(z,val))==0
    assert S.factor(third[1]-5*P1.subs(z,val)/Q.subs(z,val))==0
    assert S.factor(third[4]-val*P4.subs(z,val)/Q.subs(z,val))==0
    assert third[0]>0 and third[3]>0 and third[1]>0 and third[4]>0
    assert (third[2]<0)==(val>=29)
    assert all(c>=0 for c in xs[0]) and all(c>=0 for c in xs[1])
    assert all(c>0 for c in A.inv()[:,0])

# Local identity checked on representative weighted paths, stars, broom, and a branched tree.
cases=[
 (3,[(0,1,2),(1,2,3)],0,1),
 (4,[(0,1,1),(0,2,5),(0,3,3)],0,2),
 (4,[(0,1,3),(1,2,2),(2,3,6)],1,5),
 (5,[(0,1,5),(0,2,1),(0,4,30),(2,3,60)],0,1),
 (7,[(0,1,2),(0,2,4),(1,3,3),(1,4,2),(2,5,5),(5,6,7)],0,3),
]
for n,edges,root,mu in cases:
    A=mat(edges,n,mu)
    b=S.eye(n)[:,root]
    w={i:-A[root,i] for i in range(n) if i!=root and A[root,i]!=0}
    sigma=sum(t*t for t in w.values())
    a1=S.factor(sum(t*t*A[i,i] for i,t in w.items())/sigma)
    v=S.zeros(n,1)
    for i,t in w.items():v[i]=-t*(A[i,i]-a1)
    for j in range(n):
        if j==root or j in w:continue
        parents=[i for i in w if A[j,i]!=0]
        if parents:
            assert len(parents)==1
            i=parents[0]
            v[j]=w[i]*(-A[j,i])
    if v.dot(v)==0:continue
    a2=S.factor(v.dot(A*v)/v.dot(v))
    b1sq=sigma;b2sq=S.factor(v.dot(v)/sigma)
    a0=A[root,root]
    det=S.factor(a0*(a1*a2-b2sq)-b1sq*a2)
    assert det>0
    xs=cg_iterates(A,root)
    assert len(xs)>=3
    x3=xs[2]
    for i,t in w.items():
        assert S.factor(x3[i]-t*(a1+a2-A[i,i])/det)==0
    for j in range(n):
        if j==root or j in w:continue
        assert S.factor(x3[j]-v[j]/det)==0
print('PASS: 3 Sturm certificates, 9 exact-rational broom CG runs, 5 rooted-tree local identities')
