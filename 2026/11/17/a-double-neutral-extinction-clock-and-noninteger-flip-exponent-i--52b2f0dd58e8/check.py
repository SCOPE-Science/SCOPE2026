"""Symbolic Taylor checks and finite-time diagnostics for the Ricker–Kolmogorov map.

Run with Python 3 and SymPy: python check.py
Numerical checks are finite and do not certify infinite-time convergence.
"""
import math
import sympy as sp

w, v, c, s, g = sp.symbols('w v c s g', real=True)
L = 1-s
D = L/(2*(1+2*g))
kappa = c*(L+D)
a = c*(1+D)
b0 = L*(1+2*g)/(2*c)
x = 2+w-c*v
X = x*sp.exp(2-x)/(1+c*v)
Y = v*(s + c*b0*x/((1+g*x)*(1+c*v)))
W = X-2+c*Y

# A Taylor coefficient for w^i v^j, evaluated exactly at (0,0).
def coeff(F, i, j):
    return sp.factor(sp.diff(F, w, i, v, j).subs({w:0,v:0})/(sp.factorial(i)*sp.factorial(j)))
expected_w={(1,0):-1,(0,1):0,(2,0):0,(1,1):a,(0,2):c*c*(s-D)}
expected_v={(1,0):0,(0,1):1,(2,0):0,(1,1):D,(0,2):-kappa}
for F,expected in [(W,expected_w),(Y,expected_v)]:
    assert all(sp.simplify(coeff(F,*ij)-val)==0 for ij,val in expected.items())
# Compose the quadratic Taylor polynomials; retain all degree <=2 terms.
ww=-w+a*w*v+c*c*(s-D)*v*v
vv=v+D*w*v-kappa*v*v
pol2=lambda e:sum(sp.expand(e).coeff(w,i).coeff(v,j)*w**i*v**j for i in range(3) for j in range(3-i))
w2=pol2(ww.subs({w:ww,v:vv},simultaneous=True))
v2=pol2(vv.subs({w:ww,v:vv},simultaneous=True))
assert sp.simplify(w2-(w-2*a*w*v))==0
assert sp.simplify(v2-(v-2*kappa*v*v))==0
print('Exact first- and second-return Taylor coefficients: PASS')

for gamma, sur, cc in [(1.0,0.1,0.4),(1.0,0.3,0.4),(2.0,0.3,0.6)]:
    ell=1-sur; d=ell/(2*(1+2*gamma)); kap=cc*(ell+d)
    aa=cc*(1+d); power=aa/kap
    assert 1<power<2
    birth=ell*(1+2*gamma)/(2*cc)
    x_now=2-cc*.02+.004
    y_now=.02
    outputs={}
    for n in range(1,400001):
        x_next=x_now*math.exp(2-x_now)/(1+cc*y_now)
        y_next=y_now*(sur+cc*birth*x_now/((1+gamma*x_now)*(1+cc*y_now)))
        x_now,y_now=x_next,y_next
        if n in (100000,400000):
            corrected=x_now-2+cc*y_now
            outputs[n]=(n*y_now,(-1)**n * (n**power) * corrected)
    v100,c100=outputs[100000];v400,c400=outputs[400000]
    assert x_now>0 and y_now>0 and c100>0 and c400>0
    assert abs(v400-1/kap)/(1/kap)<.008
    assert abs(c400-c100)/c400 <.04
    print('Finite diagnostic:', {'gamma':gamma,'s':sur,'c':cc,'p':round(power,6),
          'n_y_at_400000':round(v400,7),'target':round(1/kap,7),
          'amplitude_at_400000':round(c400,7)})
print('All finite diagnostics: PASS (not an infinite-time proof)')
