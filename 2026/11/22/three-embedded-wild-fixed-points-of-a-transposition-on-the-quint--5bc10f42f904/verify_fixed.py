#!/usr/bin/env python3
"""Exact chart identities and finite-field checks for a factor-swap fixed scheme.
Requires Python 3 and SymPy >=1.10. No external data or network access.
"""
from sympy import symbols, together, simplify, factor, groebner, Matrix

x, r, t = symbols('x r t')
# In the blowup chart v-a = r (u-a), the exchange maps (x,r) to (rx,1/r).
sigma_x, sigma_r = r*x, 1/r
assert simplify(sigma_x.subs({x:sigma_x, r:sigma_r}, simultaneous=True)-x) == 0
assert simplify(sigma_r.subs({r:sigma_r}, simultaneous=True)-r) == 0
# A point is fixed iff x(r-1)=0 and r^2-1=0 (r is a unit near fixed directions).
assert factor((sigma_x-x)) == x*(r-1)
assert simplify(r*(sigma_r-r) + (r-1)*(r+1)) == 0
# Local parameter t=r-1 and fixed ideal (x*t,t*(t+2)).
assert simplify(sigma_x.subs(r,1+t)-x) == x*t
assert simplify((r*r-1).subs(r,1+t)) == t*(t+2)
assert groebner([x*t,t*(t+2)], t,x).reduce(x*t)[1] == 0
assert groebner([x*t,t*(t+2)], t,x,modulus=2).reduce(t*t)[1] == 0
G = groebner([x*t,t*t],t,x,modulus=2)
assert G.reduce(t)[1] != 0 and G.reduce(x*t)[1] == 0
assert G.reduce(t*t)[1] == 0
# Tangent action is diag(1,-1) at t=0, becoming the identity mod 2.
sigma_t = -t/(1+t)
J = Matrix([sigma_x.subs(r,1+t),sigma_t]).jacobian([x,t]).subs({x:0,t:0})
assert J == Matrix([[1,0],[0,-1]])
# The action is not the identity as a formal automorphism in characteristic 2:
# sigma(x)-x=x*t and sigma(t)-t=t^2/(1+t) in characteristic 2.
assert simplify(sigma_x.subs(r,1+t)-x) == x*t
assert simplify((sigma_t-t) + t*(t+2)/(1+t)) == 0

INF = 'infinity'
def inverse_on_p1(z,p):
    if z==INF: return 0
    if z==0: return INF
    return pow(z,-1,p)

def count_fixed(p):
    P=list(range(p))+[INF]
    centers=[0,1,INF]
    # Ordinary base chart: all pairs other than the three blow-up centers.
    base=[('base',u,v) for u in P for v in P if not(u==v and u in centers)]
    # The exceptional projective direction r=(v-a)/(u-a) at each center.
    exceptional=[('exc',a,r) for a in centers for r in P]
    def action(pt):
        kind,u,v=pt
        return (kind,v,u) if kind=='base' else (kind,u,inverse_on_p1(v,p))
    assert all(action(action(pt))==pt for pt in base+exceptional)
    fixed=[pt for pt in base+exceptional if action(pt)==pt]
    expect = p+1 if p==2 else p+4
    assert len(fixed)==expect,(p,len(fixed),expect)
    assert len(base)+len(exceptional)==(p+1)**2+3*p
    return (p,len(fixed),len(base)+len(exceptional))

counts=[count_fixed(p) for p in (2,3,5,7,11,13)]
print('M05_TRANSPOSITION_WILD_EMBEDDED_FIXED_SCHEME_VERIFIED', counts)
