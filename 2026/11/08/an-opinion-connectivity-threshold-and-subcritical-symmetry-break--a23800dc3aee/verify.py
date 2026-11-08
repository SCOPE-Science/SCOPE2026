#!/usr/bin/env python3
"""Exact calculations for a two-community SIS/opinion bifurcation."""
import sympy as sp

x1, x2, y1, y2, w = sp.symbols('x1 x2 y1 y2 w', real=True)
u, v, z, h, t = sp.symbols('u v z h t', real=True)
Q = sp.Rational
s = Q(1, 3)

# y_i is shifted opinion o_i+1/2. Both o_i<0 near the studied state.
def epidemic(x, neighbor, opinion):
    return -(Q(2, 5) + 3*opinion)*x + (1-x)*(Q(1, 10)*neighbor + 6*x*x)

F = sp.Matrix([
    epidemic(x1, x2, y1), epidemic(x2, x1, y2),
    x1-y1 + w*(y2-y1), x2-y2 + w*(y1-y2)
])
J = F.jacobian([x1, x2, y1, y2])
e = {x1:s,x2:s,y1:s,y2:s}
assert F.subs(e) == sp.zeros(4, 1)

# Exact endemic roots on the synchronous subspace.
G = sp.factor(-(Q(2, 5)+3*t)+(1-t)*(Q(1, 10)+6*t))
assert sp.expand(G+6*(t-Q(3,20))*(t-Q(1,3))) == 0
assert G.subs(t,0) < 0 and G.subs(t,1) < 0

# Decomposition into synchronous and antisynchronous two-dimensional modes.
J0 = J.subs(e)
P = sp.Matrix([[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]])
# The 2x2 blocks follow from equal-diagonal/off-diagonal structure directly.
Jplus = sp.Matrix([[J0[0,0]+J0[0,1],J0[0,2]+J0[0,3]],
                  [J0[2,0]+J0[2,1],J0[2,2]+J0[2,3]]])
Jminus= sp.Matrix([[J0[0,0]-J0[0,1],J0[0,2]-J0[0,3]],
                  [J0[2,0]-J0[2,1],J0[2,2]-J0[2,3]]])
assert Jplus == sp.Matrix([[Q(19,30),-1],[1,-1]])
assert Jminus == sp.Matrix([[Q(1,2),-1],[1,-1-2*w]])
assert sp.factor(Jplus.det()) == Q(11,30)
assert sp.simplify(Jminus.det() - (Q(1,2)-w)) == 0
assert sp.factor(Jplus.trace()) == -Q(11,30)
assert sp.simplify(Jminus.trace() + Q(1,2)+2*w) == 0

# Healthy equilibrium eigenvalues: infection -3/10,-1/2 and opinion -1,-1-2w.
Jhealthy = J.subs({x1:0,x2:0,y1:0,y2:0})
assert Jhealthy[:2,:2].eigenvals() == {-Q(3,10):1,-Q(1,2):1}
assert sp.factor(Jhealthy[2:,2:].det()) == 1+2*w

# Exact equilibrium reduction to mean infection u and disagreement v.
# At equilibrium mean opinion equals mean infection and opinion difference is
# smaller than infection difference by 1+2w.
X1,X2 = s+u+v,s+u-v
Y1,Y2 = s+u+v/(1+2*w),s+u-v/(1+2*w)
F1 = epidemic(X1,X2,Y1)
F2 = epidemic(X2,X1,Y2)
S = sp.factor((F1+F2)/2)
D = sp.factor((F1-F2)/(2*v))
Sformula = -Q(11,30)*u-Q(31,10)*u*u-6*u**3-18*u*v*v+(Q(1,10)-3/(1+2*w))*v*v
Dformula = (2*w-1)/(2*(1+2*w))-3*u*(1+1/(1+2*w))-18*u*u-6*v*v
assert sp.cancel(S-Sformula) == 0
assert sp.cancel(D-Dformula) == 0
Su,Sw,St=(sp.diff(Sformula,k).subs({u:0,v:0,w:Q(1,2)}) for k in (u,w,v))
Du,Dw = (sp.diff(Dformula,k).subs({u:0,v:0,w:Q(1,2)}) for k in (u,w))
# Differentiate with respect to t=v**2 at t=0.
St = Q(1,10)-3/Q(2)
Dt = -6
alpha,kappa=sp.symbols('alpha kappa')
ans=sp.solve([Su*alpha+Sw*kappa+St,
              Du*alpha+Dw*kappa+Dt], [alpha,kappa],dict=True)
assert ans == [{alpha:-Q(42,11),kappa:-Q(246,11)}]

# Independent center-manifold cubic calculation at the critical coupling.
# Put x1=s+u+v,x2=s+u-v,y1=s+z+h,y2=s+z-h.
Uf = sp.expand((epidemic(s+u+v,s+u-v,s+z+h)+
                epidemic(s+u-v,s+u+v,s+z-h))/2)
Vf = sp.expand((epidemic(s+u+v,s+u-v,s+z+h)-
                epidemic(s+u-v,s+u+v,s+z-h))/2)
expected_U = Q(19,30)*u-z-Q(1,10)*u*u-3*u*z-6*u**3-18*u*v*v+Q(1,10)*v*v-3*h*v
expected_V = Q(1,2)*v-h-3*h*u-18*u*u*v-6*v**3-3*z*v
assert sp.expand(Uf-expected_U) == sp.expand(Vf-expected_V) == 0
A,B,H=sp.symbols('A B H')
center={u:A*v**2,z:A*v**2,h:v/2+H*v**3}
neq_U=sp.expand(Uf.subs(center)).coeff(v,2)
neq_V=sp.expand(Vf.subs(center)).coeff(v,3)
# From h'=v-2h and invariance (dh/dv)*v'=B*v^3/2+...,
# H=-B/4. The mean opinion z' =u-z forces the same quadratic A.
center_solutions=sp.solve([neq_U,neq_V-B,H+B/4],[A,B,H],dict=True)
assert center_solutions == [{A:-Q(42,11),B:Q(164,11),H:-Q(41,11)}]
assert (sp.diff(Jminus.det(),w).subs(w,Q(1,2))) == -1
assert (sp.diff(Jminus.trace(),w).subs(w,Q(1,2))) == -2

print('PASS: equilibrium, exact roots, four-dimensional stability threshold,')
print('      equilibrium-branch derivatives, critical center cubic, healthy stability')
print('center cubic',center_solutions[0][B],
      'branch w(v^2) slope',ans[0][kappa])
