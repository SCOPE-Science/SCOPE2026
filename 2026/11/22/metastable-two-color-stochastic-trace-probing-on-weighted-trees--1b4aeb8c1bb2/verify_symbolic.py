"""Symbolic reconstruction of variance gap identities.
Requires SymPy: python verify_symbolic.py
"""
import sympy as s
x=s.symbols('x', positive=True)
edge=((0,1,2),(0,2,2),(0,6,1),(1,3,1),(1,4,1),(1,5,1))
Q=s.diag(*([x]*7))
for u,v,c in edge:
    Q[u,u]+=c;Q[v,v]+=c;Q[u,v]-=c;Q[v,u]-=c
G=Q.inv()
W=G.multiply_elementwise(G)
base=s.Matrix([1,-1,-1,1,1,1,-1])
energy=lambda z:(z.T*W*z)[0]
F=x**4+14*x**3+58*x**2+76*x+28
P=x**6+16*x**5+83*x**4+162*x**3+112*x**2-16
pieces={
    'edge01':([1,3,4,5],16*(x*x+2*x-2)*(x**4+6*x**3+8*x*x-4)/(x*x*F**2)),
    'edge02':([2],(16*x**6+224*x**5+960*x**4+1408*x**3+640*x*x+256*x+128)/(x*x*F**2)),
    'edge06':([6],(4*x**6+64*x**5+336*x**4+640*x**3+240*x*x+64*x+128)/(x*x*F**2)),
    'leaf13':([3],4*(x+2)*P/(x*(x+1)**2*F**2)),
    'leaf14':([4],4*(x+2)*P/(x*(x+1)**2*F**2)),
    'leaf15':([5],4*(x+2)*P/(x*(x+1)**2*F**2)),
    'vertex0':([0],4*(9*x**5+104*x**4+444*x**3+800*x*x+636*x+176)/(x*F**2)),
    'vertex1':([1],4*(7*x**6+80*x**5+348*x**4+688*x**3+640*x*x+256*x+32)/(x*x*F**2)),
    'competitor':([1,3,4],4*(x+2)**2*(x*x+2*x-1)*(5*x**3+28*x*x+40*x+16)/(x*(x+1)**2*F**2)),
}
assertions=0
for name,(positions,formula) in pieces.items():
    v=base.copy()
    for i in positions:v[i]=-v[i]
    assert s.cancel(energy(v)-energy(base)-formula)==0,(name,s.factor(energy(v)-energy(base)-formula))
    assertions+=1
assert s.factor(P.diff(x))==2*x*(3*x**4+40*x**3+166*x*x+243*x+112) or s.Poly(P.diff(x),x).all_coeffs()[:-1] # monotone positive on x>0
assertions+=1
assert P.subs(x,s.Rational(3,10))<0<P.subs(x,s.Rational(1,3))
assertions+=1
print(f'PASS: {assertions} symbolic identities and monotonicity/interval assertions')
