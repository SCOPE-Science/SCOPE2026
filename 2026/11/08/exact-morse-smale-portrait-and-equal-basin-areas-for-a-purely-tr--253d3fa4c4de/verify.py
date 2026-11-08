#!/usr/bin/env python3
"""Symbolic consistency checks and illustrative finite-orbit tests.

The universal convergence and Morse-Smale claims require the analytic proof.
"""
import sympy as sp
import numpy as np
from scipy.integrate import solve_ivp

x, y, k = sp.symbols('x y k', real=True)
pi = sp.pi
phi = [-x-y, 2*x-y, 2*y-x]
U = 3-sum(sp.cos(t) for t in phi)
F = sp.Matrix([-k*(sp.sin(x+y)+sp.sin(2*x-y)),
               -k*(sp.sin(x+y)+sp.sin(2*y-x))])
M = sp.Matrix([[2,-1],[-1,2]])
assert M.det() == 3
D = sp.Matrix([[sp.diff(phi[i],v) for v in (x,y)] for i in range(3)])
assert sp.simplify(sum(sp.sin(phi[i])*(D.row(i)*F)[0] for i in range(3))
                   + k*sum((sp.sin(phi[i])-sum(sp.sin(t) for t in phi)/3)**2 for i in range(3))*3) == 0
# Six exact critical points of the three-phase torus; each has three lifts.
reduced=[(0,0,'sink',(-3,-3)),
         (2*pi/3,2*pi/3,'source',(sp.Rational(3,2),sp.Rational(3,2))),
         (4*pi/3,4*pi/3,'source',(sp.Rational(3,2),sp.Rational(3,2))),
         (0,pi,'saddle',(-1,3)),(pi,0,'saddle',(-1,3)),
         (pi,pi,'saddle',(-1,3))]
counts={'sink':0,'saddle':0,'source':0}
seen=set()
for r1,r2,kind,eigs in reduced:
    for m in range(3):
        X = sp.Mod((2*r1+r2)/3+4*pi*m/3,2*pi)
        Y = sp.Mod((r1+2*r2)/3+2*pi*m/3,2*pi)
        # Sympy's trig periodicity works with unmodded representatives.
        X = (2*r1+r2)/3+4*pi*m/3
        Y = (r1+2*r2)/3+2*pi*m/3
        fx,fy=[sp.trigsimp(z.subs({x:X,y:Y}).subs(k,1)) for z in F]
        assert fx==0 and fy==0,(r1,r2,m,fx,fy)
        J=F.jacobian([x,y]).subs({x:X,y:Y,k:1}).applyfunc(sp.trigsimp)
        vals=sorted([value for value,mult in J.eigenvals().items() for _ in range(mult)],key=float)
        assert vals==list(eigs),(kind,vals,eigs)
        canonical=(float(X%(2*pi)),float(Y%(2*pi)))
        assert all(np.linalg.norm(np.array(canonical)-np.array(q))>1e-8 for q in seen)
        seen.add(canonical)
        counts[kind]+=1
assert counts=={'sink':3,'saddle':9,'source':6}
assert len(seen)==18
# Exact V levels: sink 0, saddle 4, source 9/2.
for r1,r2,kind,_ in reduced:
    X=(2*r1+r2)/3; Y=(r1+2*r2)/3
    level=sp.simplify(U.subs({x:X,y:Y}))
    expected={'sink':0,'saddle':4,'source':sp.Rational(9,2)}[kind]
    assert level==expected,(kind,level)
# The order-three deck translation fixes each phi modulo 2pi.
shift={x:x+4*pi/3,y:y+2*pi/3}
for a in phi:
    assert sp.simplify((a.subs(shift)-a)/(2*pi)).is_integer
assert sp.trigsimp(U.subs(shift)-U)==0
assert all(sp.trigsimp(z.subs(shift)-z)==0 for z in F)
# Illustrative non-proof numerical integrations; K=1.
rng=np.random.default_rng(4512)
sinks=np.array([[0.,0.],[4*np.pi/3,2*np.pi/3],[2*np.pi/3,4*np.pi/3]])
for initial in rng.uniform(0,2*np.pi,(24,2)):
    def vf(t,v):return np.array([float(z) for z in np.array([
        -np.sin(v[0]+v[1])-np.sin(2*v[0]-v[1]),
        -np.sin(v[0]+v[1])-np.sin(2*v[1]-v[0])])])
    sol=solve_ivp(vf,[0,45],initial,rtol=2e-9,atol=2e-11)
    z=sol.y[:,-1]
    dist=np.min([np.linalg.norm(((z-s+np.pi)%(2*np.pi))-np.pi) for s in sinks])
    assert dist<5e-5,dist
print('VERIFY_OK covering_degree=3 critical_points=18 sink=3 saddle=9 source=6 energy_levels=3 numerical_orbits=24')
