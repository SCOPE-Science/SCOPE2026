"""Symbolic checks and numerical illustrations of a shifted BDF2 phase threshold.
No finite run is presented as proof of the all-time statements.
"""
import sympy as S
from scipy.optimize import brentq
from math import exp, sqrt
u,v,w,beta,t=S.symbols('u v w beta t',real=True)
chi=lambda a,b:(a*a+b*b)*(a+b)/4
A=(3*w-v)/2; B=(3*v-u)/2
g=(3+2*beta*t)*w-(4+4*t)*v+(1+2*t)*u+2*t*chi(A,B)
assert S.simplify(g.subs({u:0,v:0,w:0}))==0
assert S.simplify(S.diff(g,w).subs({u:0,v:0,w:0})-(3+2*beta*t))==0
assert S.simplify(S.diff(g,v).subs({u:0,v:0,w:0})+(4+4*t))==0
assert S.simplify(S.diff(g,u).subs({u:0,v:0,w:0})-(1+2*t))==0
assert S.simplify((4+4*t)**2-4*(3+2*beta*t)*(1+2*t)+4*(4*beta*t*t+2*beta*t-4*t*t-2*t-1)) == 0
assert S.factor(S.diff(chi(A,B),w) - (S.Rational(3,8))*(3*A*A+2*A*B+B*B))==0
assert S.factor(g.subs({u:-u,v:-v,w:-w})+g)==0

def iterate(aa, beta, t, steps):
    k=beta-1
    x=aa
    y=aa*exp(-k*t)/sqrt(1+aa*aa/k*(1-exp(-2*k*t)))
    out=[x,y]
    for n in range(2,steps):
        def G(z):
            a=(3*z-y)/2; b=(3*y-x)/2
            return (3+2*beta*t)*z-(4+4*t)*y+(1+2*t)*x+2*t*((a*a+b*b)*(a+b)/4)
        z=brentq(G,-2,2,xtol=1e-300)
        out.append(z); x,y=y,z
    return out

for beta in [1.1,1.5,2,5,20]:
    k=beta-1
    tc=(sqrt(1+4/k)-1)/4
    for ratio in [0.5,0.95,1.05,2]:
        t0=ratio*tc
        aa=1e-3
        seq=iterate(aa,beta,t0,65)
        signs=[1 if z>1e-150 else (-1 if z < -1e-150 else 0) for z in seq]
        flips=sum(signs[j]*signs[j-1]<0 for j in range(1,len(signs)))
        print(f'beta={beta:.2f} t/tc={ratio:.2f} tc={tc:.8g} flip_count_first65={flips} minimum={min(seq):.3g} maximum={max(seq):.3g}')
print('symbolic checks PASS')
