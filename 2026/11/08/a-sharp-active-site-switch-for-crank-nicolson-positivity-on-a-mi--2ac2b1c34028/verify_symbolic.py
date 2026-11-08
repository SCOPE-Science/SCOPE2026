"""Symbolic replay of inverse-matrix identities for a mirrored five-site heat chain.
Requires SymPy; complements the analytical proof and stdlib rational verifier.
"""
import sympy as sp
h, t, eps, z = sp.symbols('h t eps z', positive=True)
w=[1,t,t,1]
L=sp.zeros(5)
for i,a in enumerate(w):
    L[i,i]+=a;L[i+1,i+1]+=a;L[i,i+1]-=a;L[i+1,i]-=a
R=(sp.eye(5)+h*L/2).inv()
D1=h*h*t+2*h*t+4*h+4
D2=5*h*h*t+6*h*t+4*h+4
F=3*h**4*t*t+8*h**3*t*t+4*h**3*t+4*h*h*t*t-8*h*h*t-16*h*t-16*h-16
C=3*h*h*t+2*h*t-4*h-4
assert sp.factor(R[2,2]-D1/D2)==0
assert sp.factor(R[1,1]-(h+2)*((1+h*t)/D2+1/D1))==0
assert sp.factor(R[0,0]-R[1,1]-2*h*t*(3*h*h*t+4*h*t+4*h+4)/(D1*D2))==0
assert sp.factor(R[1,1]-R[2,2]-2*h*(t*(h+2)**2-4*(h+1))/(D1*D2))==0
assert sp.factor(2*R[1,1]-1+F/(D1*D2))==0
assert sp.factor(2*R[2,2]-1+C/D2)==0
assert sp.simplify(C.subs({h:2,t:sp.Rational(3,4)}))==0
assert sp.simplify(F.subs({h:2,t:sp.Rational(3,4)}))==0
G=sp.expand(eps*F.subs({t:eps**2,h:z/eps}))
assert sp.expand(G-(4*z**3-16*z+eps*(3*z**4-8*z**2-16)+eps**2*(8*z**3-16*z)+4*z*z*eps**3))==0
assert sp.diff(G,z).subs({z:2,eps:0})==32
assert sp.diff(G,eps).subs({z:2,eps:0})==0
assert sp.diff(G,eps,2).subs({z:2,eps:0})==64
print('SYMBOLIC_VERIFY_OK 12')
