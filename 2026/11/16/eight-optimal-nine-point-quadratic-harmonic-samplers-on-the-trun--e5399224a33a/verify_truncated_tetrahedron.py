"""Exact rational certificate for quadratic harmonic sampling on a truncated tetrahedron.

Requires Python 3 and SymPy; no network, stochastic methods, or external files.
"""
from itertools import permutations, combinations
from collections import Counter
import sympy as s

V=((1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1))
labels=tuple(permutations(range(4),2))
index={v:i for i,v in enumerate(labels)}
P=[tuple(2*V[i][k]+V[j][k] for k in range(3)) for i,j in labels]
assert all(sum(t*t for t in v)==11 for v in P)

def kernel(i,j):
    t=s.Rational(sum(x*y for x,y in zip(P[i],P[j])),11)
    return (1+3*t+s.Rational(5,2)*(3*t*t-1))/12
K=s.Matrix(12,12,kernel)
M=s.Matrix([[11,x,y,z,x*y,y*z,z*x,x*x-y*y,3*z*z-11] for x,y,z in P])
assert M.rank()==9
N=s.Matrix([[-1,-1,0],[1,0,-1],[0,1,1],[1,1,0],[-1,0,0],[0,-1,0],[-1,0,1],[1,0,0],[0,0,-1],[0,-1,-1],[0,1,0],[0,0,1]])
assert N.rank()==3 and N.T*M==s.zeros(3,9)

actions=tuple(permutations(range(4)))
def act(T,p):
    return tuple(sorted(index[(p[labels[a][0]],p[labels[a][1]])] for a in T))
remaining=set(combinations(range(12),3))
assert len(remaining)==220
orbits=[]
while remaining:
    T=min(remaining)
    orbit={act(T,p) for p in actions}
    assert orbit <= remaining
    remaining-=orbit
    S=tuple(i for i in range(12) if i not in T)
    B=K.extract(S,S)
    D=M.extract(S,range(9)).det()
    det_N=N.extract(T,range(3)).det()
    assert (D!=0)==(det_N!=0)
    orbits.append((T, len(orbit), B, D, det_N))
assert len(orbits)==13
assert sum(n for _,n,_,_,_ in orbits)==220
assert Counter((int(d!=0),n) for _,n,_,d,_ in orbits)==Counter({(1,24):5,(1,8):1,(0,24):2,(0,12):3,(0,4):2})
assert sum(n for _,n,_,d,_ in orbits if d)!=0
assert sum(n for _,n,_,d,_ in orbits if d)==128
assert sum(n for _,n,_,d,_ in orbits if not d)==92
assert set(abs(d) for _,_,_,d,_ in orbits if d)=={276824064}
assert set(abs(n) for _,_,_,d,n in orbits if d)=={1}

# A basis-independent stability criterion; one rational threshold separates the
# eight optimal erasures from all 212 alternatives.
threshold=s.Rational(7,100)
minima=[]
for T,n,B,d,_ in orbits:
    if d==0:
        assert B.det()==0
        continue
    if n==8:
        assert set(labels[i] for i in T)=={(0,1),(1,2),(2,0)}
        lead=[(B-threshold*s.eye(9))[:j,:j].det() for j in range(1,10)]
        assert all(x>0 for x in lead), (T,lead)
        z=s.Symbol('z')
        chi=s.factor(B.charpoly(z).as_expr())
        target=(5324*z**3-12353*z**2+7904*z-1280)*(161051*z**3-356708*z**2+194480*z-12800)**2/s.Integer(138090848575724)
        assert s.cancel(chi-target)==0,(chi,target)
        opt_T=T
        opt_poly=chi
        opt_det=B.det()
    else:
        # Determinant negative implies a negative eigenvalue of (B - 0.07 I).
        assert (B-threshold*s.eye(9)).det()<0, T
    minima.append((T,n, int(d!=0)))

# All eight and only eight optimal deleted sets are directed triangles.
triangles={tuple(sorted(index[(i,j)] for i,j in cyc)) for tri in combinations(range(4),3) for cyc in [((tri[0],tri[1]),(tri[1],tri[2]),(tri[2],tri[0])),((tri[0],tri[2]),(tri[2],tri[1]),(tri[1],tri[0]))]}
assert len(triangles)==8
assert {act(opt_T,p) for p in actions}==triangles
assert opt_det==s.Rational(52428800000,34522712143931)

# Rational root isolation for the smallest root of the squared cubic factor.
z=s.Symbol('z')
p=161051*z**3-356708*z**2+194480*z-12800
roots=s.polys.polytools.intervals(p,eps=s.Rational(1,10000000))
assert len(roots)==3 and all(m==1 for _,m in roots)
small=min(roots,key=lambda a:a[0][0])[0]
assert small[0]>s.Rational(76,1000) and small[1]<s.Rational(77,1000)
q=5324*z**3-12353*z**2+7904*z-1280
other=s.polys.polytools.intervals(q,eps=s.Rational(1,10000000))
assert len(other)==3 and all(m==1 for _,m in other)
assert min(lo for (lo,hi),m in other)>s.Rational(24,100)
assert sorted([lo for (lo,hi),m in roots])[1]>s.Rational(75,100)

print('PASS: 13 symmetry orbits exhaust all 220 three-deletion patterns')
print('PASS: 128 invertible, 92 singular, 8 E-optimal directed triangles')
print('PASS: determinant of each viable 9-by-9 sampling matrix in the integer basis has magnitude 276824064')
print('PASS: for the 8 optima K - 7/100 I is positive definite by 9 rational leading principal minors')
print('PASS: for the other 120 invertible masks det(K - 7/100 I)<0')
print('PASS: all eight directed triangle erasures have exact characteristic polynomial:',opt_poly)
print('PASS: sharp minimum eigenvalue lies within',small, 'of polynomial',p)
print('PASS: optimizer Gram determinant',opt_det)
