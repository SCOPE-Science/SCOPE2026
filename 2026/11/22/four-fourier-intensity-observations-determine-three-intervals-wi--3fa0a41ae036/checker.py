"""Supplementary exact checks for equal-gap three-interval Fourier recovery.

Requires Python 3.10+ and SymPy. The proof in RESULT.md is analytic.
"""
import math
import random
import sympy as sp

b,v,g,h,z,t=sp.symbols('b v g h z t',real=True)
P=(sp.cos((b+g)*t/2)*sp.cos(h*t)
  -sp.cos((v+g)*t/2)*sp.cos(sp.sqrt(z)*t)
  +sp.sin(g*t/2)*sp.sin((b-v)*t/2))
q2=sp.expand(sp.series(P,t,0,4).removeO()).coeff(t,2)
assert sp.simplify(q2+(b*b-v*v+4*h*h-4*z)/8)==0
z2=sp.solve(q2,z)[0]
q4=sp.expand(sp.series(P,t,0,6).removeO()).coeff(t,4)
assert sp.simplify(q4.subs(z,z2)+(b-v)*(v-2*h)*(v+2*h)*(b+v+3*g)/96)==0

# Independent integration versus complement formula for random strict-positive examples.
def direct_intensity(a,b,c,g,w):
    ends=[(0,a),(a+g,a+g+b),(a+2*g+b,a+2*g+b+c)]
    if abs(w)<1e-12: return (a+b+c)**2
    F=sum((complex(math.cos(-w*y),math.sin(-w*y))-
           complex(math.cos(-w*x),math.sin(-w*x)))/(-1j*w)
          for x,y in ends)
    return abs(F)**2

def sinc(x): return 1.0 if x==0 else math.sin(x)/x

def closed_intensity(a,b,c,g,w):
    L=a+b+c+2*g
    A=L*sinc(L*w/2)
    B=2*g*sinc(g*w/2)*math.cos((b+g)*w/2)
    h=(a-c)/2
    return A*A+B*B-2*A*B*math.cos(h*w)

rng=random.Random(17447)
for _ in range(250):
    a,b,c,g=[rng.uniform(.05,5.0) for i in range(4)]
    for w in [0,0.033,.17,.6,1.7,4.5]:
        x=direct_intensity(a,b,c,g,w)
        y=closed_intensity(a,b,c,g,w)
        assert abs(x-y)<2e-9*(1+abs(x))
print('PASS: two exact Taylor identities and 1,500 independent Fourier-integral comparisons.')
