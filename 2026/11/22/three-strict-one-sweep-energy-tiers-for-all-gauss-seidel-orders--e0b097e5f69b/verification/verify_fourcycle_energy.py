"""Exact symbolic checker for four-node periodic screened-Poisson Gauss--Seidel orders.
Run: python verify_fourcycle_energy.py. Requires sympy.
"""
import itertools
import sympy as s
import numpy as np

t,L,u=s.symbols('t L u')
A=s.eye(4)
edges=[(0,1),(1,2),(2,3),(3,0)]
for i,j in edges:
    A[i,j]=A[j,i]=-t

def sweep(p):
    G=s.eye(4)
    for i in p:
        E=s.eye(4)
        E[i,:]-=A[i,:]
        G=E*G
    return G

# All 24 orders, grouped by dihedral symmetries of the square.
perms=set(itertools.permutations(range(4)))
orbits=[]
for rep in ((0,2,1,3),(0,1,3,2),(0,1,2,3)):
    orbit=set()
    for k in range(4):
        for sigma in (1,-1):
            orbit.add(tuple((k+sigma*i)%4 for i in rep))
    assert len(orbit)==8
    orbits.append(orbit)
assert orbits[0].isdisjoint(orbits[1]) and orbits[1].isdisjoint(orbits[2])
assert orbits[0].isdisjoint(orbits[2]) and set.union(*orbits)==perms

# Exact generalized squared-energy singular-value polynomials.
expected=[
  (1-4*t*t)*L**3*(L-4*t*t),
  (1-4*t*t)*L**2*(L**2-4*t*t*(1+t*t)*L+4*t**4),
  (1-4*t*t)*L*(L**3-(t**6+4*t**4+4*t*t)*L**2+(2*t**6+4*t**4)*L-t**6),
]
G=[]
for j,orbit in enumerate(orbits):
    for p in orbit:
        M=sweep(p)
        poly=s.factor((M.T*A*M-L*A).det())
        assert s.simplify(poly-expected[j])==0,('energy',j,p)
    G.append(sweep(((0,2,1,3),(0,1,3,2),(0,1,2,3))[j]))

# Red-black and interlaced orders have exactly equal minimal spectral radius.
for j in (0,1):
    assert s.simplify(G[j].charpoly(L).as_expr()-L**3*(L-4*t*t))==0
# On the cyclic orbit, its characteristic has a strictly positive signed
# spectral-cubic value at 4 t^2: t^4(1-4t^2)^2>0 for 0<t<1/2.
cyclic_cubic=-L**3+(t**4+4*t*t)*L**2-2*t**4*L+t**4
assert s.expand(cyclic_cubic.subs(L,4*t*t)-t**4*(1-4*t*t)**2)==0

# Strict cyclic < red-black squared-energy norm: Sylvester minors.
K=4*t*t*A-G[2].T*A*G[2]
expected_minors=[4*t*t,
    4*t**4*(t**6+3*t**4-2*t*t+3),
    4*t**6*(8*t**6+26*t**4-19*t*t+9),
    4*t**8*(1-4*t*t)**2*(4*t*t+15)]
for k in range(1,5):
    assert s.simplify(K[:k,:k].det()-expected_minors[k-1])==0
# On u=t^2 in (0,1/4), the two nontrivial polynomials exceed
# 3-2/4>0 and 9-19/4>0, respectively.

# Strict mixed < cyclic squared-energy factor: evaluate the cyclic
# energy eigen-polynomial at the larger mixed root.
cyclic_energy=-L**3+(t**6+4*t**4+4*t*t)*L**2-(2*t**6+4*t**4)*L+t**6
mixed_quadratic=L**2-4*t*t*(1+t*t)*L+4*t**4
remainder=s.rem(cyclic_energy,mixed_quadratic,L)
assert s.factor(remainder-t**6*(4*L*t**4+4*L*t*t-2*L-4*t**4+1))==0
P=1-4*u+16*u**3+8*u**4
Q=4*u*(2*u**2+2*u-1)
assert s.expand(P*P-u*(u+2)*Q*Q-(4*u-1)**2)==0
# P>0,Q<0 for 0<u<1/4, so P+Q*sqrt(u*(u+2))>0.

# Supplementary rational instances (not a substitute for all-parameter proof).
for val in (s.Rational(1,100),s.Rational(1,10),s.Rational(1,4),s.Rational(3,10),s.Rational(2,5),s.Rational(49,100)):
    Av=A.subs(t,val)
    assert all(e>0 for e in Av.eigenvals())
    values=[]
    for order in ((0,2,1,3),(0,1,3,2),(0,1,2,3)):
        M=sweep(order).subs(t,val)
        # Symmetric real spectrum of the generalized energy eigenproblem.
        ev=np.linalg.eigvals(np.array((Av.inv()*(M.T*Av*M)).tolist(),dtype=float))
        values.append(max(e.real for e in ev))
    assert values[1]<values[2]<values[0],(val,values)
print('PASS: all 24 orders; three exact generalized polynomials; spectral ties; strict energy inequalities; six rational supplementary tests')
