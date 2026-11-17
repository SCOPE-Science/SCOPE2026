"""Standalone verification for the regular bipyramid microscopic-weight theorem.
Run: python verify.py (requires Python 3, SymPy, NumPy, mpmath).
Finite matrix checks corroborate, rather than prove, the universal theorem.
"""
import math
import numpy as np
import sympy as sp
import mpmath as mp

checks = 0

def check(statement, message):
    global checks
    assert bool(statement), message
    checks += 1

x, y, a = sp.symbols('x y a', positive=True)
H = 1 + x*x + x*y + y*y - a*(x+y)
p = (1 + y*y - a*(x+y))/(2*H)
q = (1 + x*x - a*(x+y))/(2*H)
nw = (x+y)**2/(2*H)
check(sp.factor(p+q+nw-1)==0,'total mass')
check(sp.factor(sp.diff(p,y)-x*(2*x*y+y*y-1)/(2*H**2))==0,'partial derivative y')
Dy = sp.factor(sp.diff(p,x)*(2*H**2))
y_opt_x = (1-y*y)/(2*y)
check(sp.factor(Dy.subs(x,y_opt_x)-(1+y*y)*(a*(1+y*y)-4*y)/(4*y*y))==0,'partial derivative on y-minimizing locus')
z, d = sp.symbols('z d', real=True)
check(sp.expand(H.subs({x:z+d,y:z-d})-(1+3*z*z+d*d-2*a*z))==0,'sum/difference representation')
check(sp.factor((p+q).subs({x:z+d,y:z-d})-(1+z*z+d*d-2*a*z)/(1+3*z*z+d*d-2*a*z))==0,'total apex mass')

# Reconstruct all distance-row equations with exact rational variable substitution.
s = (1+x*x)/(2*x); u = (1-x*x)/(2*x)
t = (1+y*y)/(2*y); v = (1-y*y)/(2*y)
L = u+v
A = sp.symbols('A')
# The equatorial per-vertex weight equals nw/n for an arbitrary n.
W = nw/sp.Symbol('n', positive=True)
P_eq = sp.factor(A*W+s*p+t*q)
P_top = sp.factor(sp.Symbol('n', positive=True)*s*W+L*q)
P_bottom = sp.factor(sp.Symbol('n', positive=True)*t*W+L*p)
check(sp.factor((P_eq-P_top).subs(A,sp.Symbol('n', positive=True)*a))==0,'equal top and ring potentials')
check(sp.factor((P_eq-P_bottom).subs(A,sp.Symbol('n', positive=True)*a))==0,'equal bottom and ring potentials')

rt2 = sp.sqrt(2)
B = (a+2-2*rt2)/(2*(2*rt2-1-a))
C = (a*a-1)/(3-a*a)
y_star = rt2-1
check(sp.simplify(-p.subs({x:1,y:y_star})-B)==0,'one-negative boundary value')
check(sp.simplify(-(p+q).subs({x:1/a,y:1/a})-C)==0,'two-negative symmetric value')
check(sp.simplify(sp.diff(B,a)-1/(2*(2*rt2-1-a)**2))==0,'boundary derivative')
check(sp.simplify(sp.diff(C,a)-4*a/(3-a*a)**2)==0,'symmetric derivative')

a4 = (1+sp.sqrt(2))/2
a5 = sp.Rational(2,5)*sp.sqrt(5+2*sp.sqrt(5))
check(sp.sign(sp.simplify((C-B).subs(a,a4)))==-1,'exact four-gon comparison')
check(sp.sign(sp.simplify((C-B).subs(a,a5)))==1,'exact five-gon comparison')
# Rational enclosures prove the derivative-ordering gap on the full relevant range.
root2_lo=sp.Rational(707,500)  # less than sqrt(2)
root3_hi=sp.Rational(1733,1000)  # greater than sqrt(3)
pi_lo=sp.Rational(157,50) # less than pi
loC=sp.Rational(72,25)/root3_hi
hiB=1/(2*(2*root2_lo-1-4/pi_lo)**2)
check(loC>hiB,'rigorous rational derivative-gap bound')
mp.mp.dps=70
for n in range(3,51):
    an=2*mp.cot(mp.pi/(2*n))/n
    check(an>1 and an<4/mp.pi and an<mp.sqrt(2),'chord average range')
    # Strict gap between the two modes: below five the sharp sup lies on boundary.
    bn=(an+2-2*mp.sqrt(2))/(2*(2*mp.sqrt(2)-1-an))
    cn=(an**2-1)/(3-an**2)
    check((bn>cn) == (n in (3,4)),'dimension dichotomy')
    check(cn>0 and bn>0,'positive sharp quantities')

for n in range(3,21):
    theta=np.arange(n)*2*np.pi/n
    ring=np.column_stack([np.cos(theta),np.sin(theta),np.zeros(n)])
    an=2/(n*math.tan(math.pi/(2*n)))
    for u,v in [(0.03,0.09),(0.15,0.8),(0.25,0.25),(0.6,0.7),(1.0,0.01),(2.0,0.5),(3.5,3.0)]:
        verts=np.vstack([ring,[0,0,u],[0,0,-v]])
        D=np.linalg.norm(verts[:,None,:]-verts[None,:,:],axis=2)
        ones=np.ones(n+2)
        raw=np.linalg.solve(D,ones)
        obs=raw/raw.sum()
        xx=math.hypot(1,u)-u; yy=math.hypot(1,v)-v
        hh=1+xx*xx+xx*yy+yy*yy-an*(xx+yy)
        predicted=np.array([(xx+yy)**2/(2*n*hh)]*n+
            [(1+yy*yy-an*(xx+yy))/(2*hh),(1+xx*xx-an*(xx+yy))/(2*hh)])
        check(np.max(np.abs(obs-predicted))<1e-9,'independent distance-matrix solution')
        check(np.max(np.abs(D@predicted-(D@predicted)[0]))<1e-9,'equal distance potentials')
        check(np.isclose(predicted.sum(),1.0,atol=1e-12),'total mass numerical')
        check(hh>0,'normalizer positive numerical')

for n in [3,4,5,6,12,24]:
    an=2/(n*math.tan(math.pi/(2*n)))
    bb=(an+2-2*math.sqrt(2))/(2*(2*math.sqrt(2)-1-an))
    cc=(an*an-1)/(3-an*an)
    for k in range(200):
        # A deterministic dense sample checks the global bound, including asymmetry.
        xx=.0001+ .9998*((k*73 % 211)+.5)/211
        yy=.0001+ .9998*((k*107 % 223)+.5)/223
        hh=1+xx*xx+xx*yy+yy*yy-an*(xx+yy)
        pp=(1+yy*yy-an*(xx+yy))/(2*hh)
        qq=(1+xx*xx-an*(xx+yy))/(2*hh)
        neg=max(0,-pp)+max(0,-qq)
        check(neg<=max(bb,cc)+1e-10,'sample negative-mass bound')

print(f'PASS: {checks} symbolic, exact-expression, full-distance-matrix and sampled-bound assertions')
