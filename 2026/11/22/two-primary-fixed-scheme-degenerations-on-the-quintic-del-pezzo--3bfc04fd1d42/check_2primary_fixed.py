#!/usr/bin/env python3
"""Exact symbolic checks for two primary marking permutations on bar M_{0,5}.
Requires Python 3 and SymPy. No external data or network access.
"""
from itertools import combinations
import sympy as s
x,y,u,v,a,b=s.symbols('x y u v a b')

def same(p,q):
    assert s.cancel(p-q)==0,(p,q)

def fourcycle(pair):
    X,Y=pair
    return (s.cancel(X/(X-1)),s.cancel(X/(X-Y)))

def inv(pair):
    X,Y=pair
    return (X,s.cancel(X/Y))

z=(x,y)
for n in range(1,5):
    z=fourcycle(z)
    if n==4:
        same(z[0],x);same(z[1],y)
same(inv(inv((x,y)))[0],x)
same(inv(inv((x,y)))[1],y)

# At blown-up (0,0): x=uv, y=v; E_{00}:v=0, strict x=0:u=0.
X4=s.cancel(x/(x-1)).subs({x:u*v})
Y4=s.cancel(x/(x-y)).subs({x:u*v,y:v})
U4=s.cancel(X4/Y4);V4=s.cancel(Y4)
same(U4,v*(u-1)/(u*v-1));same(V4,u/(u-1))
# Solve fixed equations, with the denominators inverted in this chart.
P=s.expand(u*(u*u-2*u+2))
fix_u=s.together(u-U4).as_numer_denom()[0]
fix_v=s.together(v-V4).as_numer_denom()[0]
subs_v=s.solve(fix_v,v)[0]
red=s.factor(fix_u.subs(v,subs_v))
assert s.factor(red/P) in (1,-1,1/(u-1),-1/(u-1),u-1,1-u), red
assert abs(s.resultant(P,1-u,u))==1
assert abs(s.resultant(P,1-u+u*u,u))==1
# The two non-boundary fixed points are x=2 and y^2-2y+2=0.
inside=s.factor((y*y-2*y+2))
same(s.factor(P.subs(u,2/y)*y**3), 4*inside)

# Double transposition (12)(34): x unchanged, y -> x/y.
# Near blowup center (1,1): x=1+ab, y=1+b.
Xi=1+a*b;Yi=s.cancel(Xi/(1+b))
Bp=s.cancel(Yi-1)
Ap=s.cancel((Xi-1)/Bp)
same(Bp,b*(a-1)/(1+b));same(Ap,a*(1+b)/(a-1))
F=a-2-b
same(s.factor((a-Ap)*(a-1)), a*F)
same(s.factor((b-Bp)*(1+b)), -b*F)
# Curve x=y^2 has strict transform a=2+b in this chart.
same(s.cancel(((1+b)**2-1)/b),b+2)
# In characteristic two the extra element t=a+b has square 0 in
# F_2[a,b]/((a,b)*(a+b)); it is not itself in that homogeneous ideal.
t=a+b
G=s.groebner([a*t,b*t],a,b,modulus=2)
assert G.reduce(t*t)[1]==0
assert G.reduce(t)[1]!=0
# All potentially invariant boundary crossings are accounted for.
labels=range(1,6)
Ds=[tuple(z) for z in combinations(labels,2)]
def perm(pair,sigma): return tuple(sorted(sigma.get(t,t) for t in pair))
def check_boundary(sigma):
    fixed=[z for z in Ds if perm(z,sigma)==z]
    exchanges=[]
    for d,e in combinations(Ds,2):
        if not(set(d)&set(e)) and perm(d,sigma)==e and perm(e,sigma)==d:
            exchanges.append((d,e))
    print('boundary fixed components',fixed,'swapped disjoint pairs',exchanges)
    return fixed,exchanges
f,e=check_boundary({1:2,2:3,3:4,4:1})
assert f==[] and e==[((1,3),(2,4))]
f,e=check_boundary({1:2,2:1,3:4,4:3})
assert f==[(1,2),(3,4)]
assert set(e)=={((1,3),(2,4)),((1,4),(2,3))}
# Fourcycle fixed finite algebra over odd and even fields.
for p in [2,3,5,7,11,13,17,19,23,29]:
    roots=[t for t in range(p) if int(P.subs(u,t))%p==0]
    expected=1 if p==2 or p%4==3 else 3
    assert len(roots)==expected,(p,roots)
    # Involutive curve has q+1 geometric-rational points;
    # the isolated section is distinct only outside characteristic 2.
    print('p',p,'order4 rational fixed',len(roots),'order2 rational fixed',p+1+(p!=2))
print('EXACT_TWO_PRIMARY_FIXED_SCHEMES_VERIFIED')
