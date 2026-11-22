"""Exact verifier for a one-parameter truncated-cube projection-volume profile.
Run: python3 verify_profile.py  (requires SymPy; optional NumPy/SciPy hull check).
All assertions identifying critical points use exact algebra and Descartes' rule,
not floating point root searches. Numerical hull checks are auxiliary.
"""
from itertools import combinations, product
from collections import Counter
from fractions import Fraction
from math import comb
import sympy as S

x,u=S.symbols('x u',real=True)
axis=[(1,0,0),(0,1,0),(0,0,1)]
diag=[(1,1,1),(1,1,-1),(1,-1,1),(-1,1,1)]
basis=axis+diag
counts=Counter()
for triple in combinations(range(7),3):
    d=abs(int(S.det(S.Matrix([basis[i] for i in triple]))))
    counts[(sum(i<3 for i in triple),d)]+=1
assert counts==Counter({(3,1):1,(2,1):12,(1,2):12,(1,0):6,(0,4):4}),counts

a1=2*(x-1)**2
b1=(x**2-3*(x-1)**2)/2
v1=S.Rational(4,3)*(x**3-3*(x-1)**3)
a2=4-2*(3-x)**2
b2=(3-x)**2/2
v2=8-S.Rational(4,3)*(3-x)**3
W=lambda a,b:8*(a**3+12*a*a*b+24*a*b*b+16*b**3)
qm=4*x**5-16*x**4+16*x**3+4*x**2-10*x+3
qp=2*x**4-15*x**3+27*x**2+3*x-25
dm=2*x**3-9*x**2+9*x-3
dp=x**3-9*x**2+27*x-21
Pm=S.factor(W(a1,b1)/v1**2)
Pp=S.factor(W(a2,b2)/v2**2)
assert S.simplify(Pm-(-9*(4*x**6-24*x**5+60*x**4-88*x**3+72*x**2-30*x+5)/dm**2))==0
assert S.simplify(Pp-(9*(3*x**6-54*x**5+393*x**4-1476*x**3+2997*x**2-3078*x+1247)/dp**2))==0
assert S.simplify(S.diff(Pm,x)-54*x*(x-1)*qm/dm**3)==0
assert S.simplify(S.diff(Pp,x)-108*(x-3)**2*qp/dp**3)==0
assert S.simplify((1+u)**5*qm.subs(x,(1+2*u)/(1+u))-(-u**5-11*u**4+2*u**3+14*u**2+7*u+1))==0
assert S.simplify((1+u)**4*qp.subs(x,(2+3*u)/(1+u))-(-16*u**4-40*u**3-24*u**2-u+1))==0
assert S.sign(qm.subs(x,1))==1 and S.sign(qm.subs(x,2))==-1
assert S.sign(qp.subs(x,2))==1 and S.sign(qp.subs(x,3))==-1
assert [S.simplify(Pm.subs(x,t)) for t in [1,S.Rational(3,2),2]]==[9,S.Rational(127,16),S.Rational(207,25)]
assert [S.simplify(Pp.subs(x,t)) for t in [2,3]]==[S.Rational(207,25),8]
assert S.simplify(Pm.subs(x,2)-Pp.subs(x,2))==0
assert S.simplify(S.diff(Pm,x).subs(x,2)-S.diff(Pp,x).subs(x,2))==0
assert S.sign(qm.subs(x,S.Rational(1574,1000)))==1
assert S.sign(qm.subs(x,S.Rational(1575,1000)))==-1
assert S.sign(qp.subs(x,S.Rational(2141,1000)))==1
assert S.sign(qp.subs(x,S.Rational(2142,1000)))==-1
# Bernstein positivity of numerator of 9-Pp on the [2,3] interval.
num=S.expand((9-Pp)*dp**2)
f=S.Poly(S.cancel(num.subs(x,2+u)),u)
n=f.degree()
bern=[sum(f.nth(j)*S.Rational(comb(k,j),comb(n,j)) for j in range(k+1)) for k in range(n+1)]
assert bern==[18,18,S.Rational(108,5),S.Rational(153,5),36,36,36], bern
assert all(q>0 for q in bern)
# Two crossings of 8 are a consequence of one critical minimum and rational endpoint signs.
assert Pm.subs(x,1)>8 and Pm.subs(x,S.Rational(3,2))<8 and Pm.subs(x,2)>8
# Special-point comparison to independently known truncated-octahedron volume 8128 after scaling by 2.
assert S.simplify(W(a1,b1).subs(x,S.Rational(3,2))*64)==8128
# Basic independent determinant sum and direct 3D polyhedral hull volume checks.
try:
    import numpy as np
    from scipy.spatial import ConvexHull
    for t in [S.Rational(11,10),S.Rational(3,2),S.Rational(2,1),S.Rational(9,4),S.Rational(3,1)]:
        if t<=2: aa,bb=a1.subs(x,t),b1.subs(x,t)
        else: aa,bb=a2.subs(x,t),b2.subs(x,t)
        gg=[np.asarray(v,dtype=float)*float(aa) for v in axis]+[np.asarray(v,dtype=float)*float(bb) for v in diag]
        verts=np.array([sum((sgn*g for sgn,g in zip(signs,gg)),np.zeros(3)) for signs in product([-1,1],repeat=7)])
        hull=ConvexHull(verts)
        target=float(W(aa,bb))
        assert abs(hull.volume-target)<max(1e-8,1e-10*target),(t,hull.volume,target)
        # Independent H-representation vertex geometry, not inferred from facet normals:
        from itertools import permutations
        if t<=2: raw=(S.Integer(1),t-1,S.Integer(0))
        else: raw=(S.Integer(1),S.Integer(1),t-2)
        pts={tuple(sgn[i]*perm[i] for i in range(3)) for perm in set(permutations(raw)) for sgn in product([-1,1],repeat=3)}
        p3=np.asarray([tuple(map(float,pt)) for pt in pts])
        v_hull=ConvexHull(p3)
        target_v=float((v1 if t<=2 else v2).subs(x,t))
        assert abs(v_hull.volume-target_v)<1e-9,(t,v_hull.volume,target_v)
        # Independently form the x1=1 axial polygon and x1+x2+x3=t diagonal polygon.
        axis_pts=np.asarray([tuple(map(float,pt)) for pt in pts if pt[0]==1])
        if aa>0:
            assert abs(ConvexHull(axis_pts[:,1:3]).volume-float(aa))<1e-9
        diag_pts=np.asarray([tuple(map(float,pt)) for pt in pts if sum(pt)==t])
        basis_1=np.array([1.,-1.,0.])/np.sqrt(2.)
        basis_2=np.array([1.,1.,-2.])/np.sqrt(6.)
        diag_uv=np.column_stack((diag_pts@basis_1,diag_pts@basis_2))
        if bb>0:
            assert abs(ConvexHull(diag_uv).volume-float(bb)*np.sqrt(3.))<1e-9
    print('EXACT_ALGEBRA_AND_NUMERIC_HULL_PASS')
except ImportError:
    print('EXACT_ALGEBRA_PASS ; optional NumPy/SciPy hull check not available')
print('DESCARTES_CERTIFIED_UNIQUE_CRITICAL_POINTS', counts)
