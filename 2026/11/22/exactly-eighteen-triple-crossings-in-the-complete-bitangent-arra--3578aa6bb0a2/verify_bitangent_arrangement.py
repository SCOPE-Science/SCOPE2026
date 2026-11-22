#!/usr/bin/env python3
"""Exact independent certificates for the order-nine quartic bitangent arrangement."""
import itertools
from collections import Counter
import sympy as S

m,b,d=S.symbols('m b d')
H=m**9-96*m**6+48*m**3+64
D=m**6+20*m**3-8
R=8*m*(1+m**3)**2
f_d=m**3-9*d**3*m**2+4
h_d=27*d**9-4

assert S.gcd(H,S.diff(H,m))==1
assert S.gcd(H,D)==1
assert S.gcd(H,1+m**3)==1
assert S.gcd(H,m)==1
assert S.gcd(S.Poly(h_d,d),S.Poly(S.diff(h_d,d),d))==1
r=S.symbols('r')
assert S.gcd(27*r**3-4,(3*r-1)*(9*r*r+3*r+1))==1
# Square-of-quadratic coefficient identities eliminate to D*b^3=R and H(m)=0.
u=3*m**2*b/(2*(1+m**3))
v=3*m*(4+m**3)*b**2/(8*(1+m**3)**2)
assert S.cancel((1+m**3)*(u**2+2*v)-3*m*b**2)==0
lin=S.factor((1+m**3)*2*u*v-(b**3+m))
con=S.factor((1+m**3)*v**2-b)
assert S.cancel(lin-((D*b**3-R)/(8*(1+m**3)**2)))==0, 'Incorrect x coefficient normalization'
# Below constraints verified by elimination rather than relying on a particular scaling.
I=S.groebner([D*b**3-R,H],b,m,order='lex')
# With D*b^3=R, constant square equation vanishes iff H=0.
num=S.together(con).as_numer_denom()[0]
assert I.reduce(S.expand(num))[1]==0
# Certify the nine finite triple points. If h_d=0, the cubic f_d has
# three distinct slopes and their resulting lines all pass through P_d.
G=S.groebner([f_d,h_d],m,d,order='lex')
assert G.reduce(H)[1]==0
B=(3*d**3+m)**3*D-216*d**6*m*(1+m**3)**2
assert G.reduce(B)[1]==0
assert S.gcd(27*r**3-4,S.discriminant(f_d,m).subs(d**3,r))==1

# A complete good-prime reduction: every characteristic-zero bitangent
# has a unique distinct reduction at p=433; all triple determinants remain zero.
p=433
mm=[a for a in range(p) if int(H.subs(m,a))%p==0]
assert len(mm)==9
bb=[(a,c) for a in mm for c in range(p)
    if (c**3*(a**6+20*a**3-8)-8*a*(1+a**3)**2)%p==0]
assert len(bb)==27 and len(set(bb))==27
assert all((a**6+20*a**3-8)%p!=0 and (1+a**3)%p!=0 for a in mm)
lines=[(0,1,0)]+[((-a)%p,1,(-c)%p) for a,c in bb]
assert len(lines)==len(set(lines))==28

def det(a,b,c):
    return (a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0]) +a[2]*(b[0]*c[1]-b[1]*c[0]))%p

def cross(a,b):
    return ((a[1]*b[2]-a[2]*b[1])%p,(a[2]*b[0]-a[0]*b[2])%p,(a[0]*b[1]-a[1]*b[0])%p)

def norm(v):
    pivot=next(x for x in v if x!=0)
    return tuple(x*pow(pivot,-1,p)%p for x in v)

points={}
for i,j in itertools.combinations(range(28),2):
    P=norm(cross(lines[i],lines[j]))
    points.setdefault(P,set()).update([i,j])
for P,ls in points.items():
    assert {i for i,L in enumerate(lines) if sum(x*y for x,y in zip(L,P))%p==0}==ls
multiplicity=Counter(map(len,points.values()))
assert multiplicity==Counter({2:324,3:18})
assert sum(1 for P,ls in points.items() if len(ls)==3 and P[2]==0)==9
assert sum(1 for P,ls in points.items() if len(ls)==3 and P[2]!=0)==9
roots_d=[e for e in range(p) if (27*e**9-4)%p==0]
assert len(roots_d)==9
for e in roots_d:
    P=norm(((-pow(3*e**2,-1,p))%p,e,1))
    assert P in points and len(points[P])==3
    assert len([a for a in mm if (a**3-9*e**3*a*a+4)%p==0])==3
triples=sum(det(lines[i],lines[j],lines[k])==0 for i,j,k in itertools.combinations(range(28),3))
assert triples==18
assert 324+18*S.binomial(3,2)==S.binomial(28,2)
assert 324+18*3-28+1==351
print('BITANGENT_28_LINE_18_TRIPLE_324_DOUBLE_CERTIFIED',len(lines),len(points),dict(multiplicity),triples)
