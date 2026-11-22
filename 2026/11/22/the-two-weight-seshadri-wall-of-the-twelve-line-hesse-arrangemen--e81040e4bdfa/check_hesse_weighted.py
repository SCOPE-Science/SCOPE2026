"""Exact incidence certificate for the Hesse two-stratum Seshadri formula.

All arithmetic is in Z[w]/(w*w+w+1), with w a primitive cubic root.
No floating point arithmetic or external packages are used.
"""
from fractions import Fraction


def add(a,b): return (a[0]+b[0],a[1]+b[1])
def neg(a): return (-a[0],-a[1])
def mul(a,b):
    x,y=a; u,v=b
    return (x*u-y*v,x*v+y*u-y*v)

def zero(a): return a==(0,0)

def sum3(a,b,c): return add(add(a,b),c)

ONE=(1,0); ZERO=(0,0); W=(0,1)
P=[ONE,W,mul(W,W)]

# The nine original non-coordinate Hesse lines have coefficients
# (1,w**i,w**j). The three coordinate lines are included separately.
H=[(ONE,ZERO,ZERO),(ZERO,ONE,ZERO),(ZERO,ZERO,ONE)]
H += [(ONE,P[i],P[j]) for i in range(3) for j in range(3)]

# The dual Hesse nine-line arrangement consists of the three pencils
# x=w**i y, x=w**i z, y=w**i z.
G=[]
for t in P:
    G += [(ONE,neg(t),ZERO),(ONE,ZERO,neg(t)),(ZERO,ONE,neg(t))]

# Twelve nodes, and nine quadruple points, of H.
D=[(ONE,ZERO,ZERO),(ZERO,ONE,ZERO),(ZERO,ZERO,ONE)]
D += [(ONE,a,b) for a in P for b in P]
Q=[]
for t in P:
    Q += [(ZERO,ONE,neg(t)),(ONE,ZERO,neg(t)),(ONE,neg(t),ZERO)]


def incident(line,point):
    return zero(sum3(*(mul(u,v) for u,v in zip(line,point))))

assert len(H)==12 and len(G)==9 and len(D)==12 and len(Q)==9
assert len(set(H))==12 and len(set(G))==9
assert set(H).isdisjoint(G)
assert all(sum(incident(L,p) for L in H)==4 for p in Q)
assert all(sum(incident(L,p) for L in H)==2 for p in D)
assert all(sum(incident(L,p) for L in G)==0 for p in Q)
assert all(sum(incident(L,p) for L in G)==3 for p in D)
assert all(sum(incident(L,p) for p in Q)==3 for L in H)
assert all(sum(incident(L,p) for p in D)==2 for L in H)
assert all(sum(incident(L,p) for p in D)==4 for L in G)

# The original singular-point list is complete. Pairwise H intersections
# must meet at one of its 21 distinct marked points. Distinctness of
# projective points follows by explicit coordinate normalization below.

def canonical_point(v):
    # Normalize the first nonzero entry, using w conjugation and norm.
    u=next(t for t in v if t!=ZERO)
    a,b=u
    norm=a*a-a*b+b*b
    conj=(a-b,-b)
    return tuple(tuple(Fraction(k,norm) for k in mul(t,conj)) for t in v)

all_pts=[canonical_point(p) for p in Q+D]
assert len(set(all_pts))==21
for i,L in enumerate(H):
    for K in H[i+1:]:
        assert sum(incident(L,p) and incident(K,p) for p in Q+D)==1

# A weighted ratio has maximum reciprocal weight density
# max(3*a+2*b,4*b). Two summed Bezout inequalities imply
# 4*A+2*B<=12*d and 3*B<=9*d for every curve off H union G.
# Check the piecewise linear support calculation on exact rationals.
def bound(a,b):
    assert a>0 and b>0
    return max(3*a+2*b,4*b)

for a in range(1,20):
    for b in range(1,20):
        M=bound(Fraction(a),Fraction(b))
        assert M*M >= 9*a*a+12*b*b
        # Vertices of triangle A,B>=0, 2A+B<=6, B<=3,
        # scaled by arbitrary degree d=1.
        vertices=[(Fraction(0),Fraction(0)),(Fraction(3),Fraction(0)),
                  (Fraction(0),Fraction(3)),(Fraction(3,2),Fraction(3))]
        assert all(a*A+b*B<=M for A,B in vertices)
        assert (3*a+2*b==4*b)==(2*b==3*a)

print('PASS: 21 distinct points, H=12 and G=9 line incidences,')
print('      pairwise H singular support, rational chamber and volume checks')
