"""Reproduce exact series coefficients and high-precision OU excursion checks.

Requires Python 3, sympy and mpmath. No external files or network needed.
"""
import sympy as sp
import mpmath as mp

mp.mp.dps = 65
N = 0

def verify(test, label):
    global N
    if not bool(test):
        raise AssertionError(label)
    N += 1

w, q = sp.symbols('w q')
# The Gaussian law of z conditional on |z| <= v has even moments
# E[z^2] = v^2/3 - (2/45)v^4 + O(v^6), E[z^4]=v^4/5+O(v^6).
u2 = w/(1-q**2)
v2 = w*q**2/(1-q**2)
center = 1 + u2*(v2/3 - 2*v2**2/45)/2 + u2**2*v2**2/120
expr = sp.series(sp.exp(-w*q**2/(2*(1-q**2)))*center, q, 0, 6).removeO().expand()
c2 = w*(w-3)/6
c4 = w*(3*w**3-38*w**2+165*w-180)/360
verify(sp.simplify(expr.coeff(q,2)-c2)==0, 'second Hermite coefficient')
verify(sp.simplify(expr.coeff(q,4)-c4)==0, 'fourth Hermite coefficient')
verify(c4.subs(w,3)==sp.Rational(9,20), 'critical coefficient')
verify(sp.simplify(sp.diff(c2,w) - (2*w-3)/6)==0, 'dimensionless derivative')

def F(W, t):
    W, t = mp.mpf(str(W)), mp.mpf(str(t))
    qq = mp.exp(-t)
    uu = mp.sqrt(W/(1-qq*qq))
    vv = qq*uu
    return (mp.erf((uu+vv)/mp.sqrt(2))-mp.erf((uu-vv)/mp.sqrt(2)))/(2*mp.erf(vv/mp.sqrt(2)))

def q_to_t(x):
    return -mp.log(mp.mpf(str(x)))

for W in ['0.25','0.8','1.5','2.75','3','4','7']:
    Wm=mp.mpf(W)
    target=mp.exp(-Wm/2)
    c2m=Wm*(Wm-3)/6
    c4m=Wm*(3*Wm**3-38*Wm**2+165*Wm-180)/360
    for Q in ['0.05','0.025']:
        Qm=mp.mpf(Q)
        ratio=F(W,q_to_t(Q))/target
        approx=1+c2m*Qm**2+c4m*Qm**4
        verify(abs(ratio-approx)<mp.mpf('5')*Qm**6, f'asymptotic series W={W} q={Q}')
    for T in ['0.000001','0.00000025']:
        Tm=mp.mpf(T)
        leading=mp.mpf('.5')-mp.sqrt(Wm)/(2*mp.sqrt(mp.pi))*mp.sqrt(Tm)
        verify(abs(F(W,Tm)-leading)<mp.mpf('4')*Tm, f'small-time expansion W={W} t={T}')

for W in ['0.2','1','2.5','2.9']:
    verify(F(W,mp.mpf('.000001'))<mp.mpf('.5'), 'initial decline W='+W)
    verify(F(W,mp.mpf('9'))<F(W,mp.mpf('12')), 'eventual increase W='+W)
    verify(F(W,mp.mpf('9'))<mp.exp(-mp.mpf(W)/2), 'below QSD W='+W)

for W in ['3','3.5','5','8']:
    verify(F(W,mp.mpf('9'))>F(W,mp.mpf('12')), 'eventual decrease W='+W)
    verify(F(W,mp.mpf('12'))>mp.exp(-mp.mpf(W)/2), 'above QSD W='+W)

for W in ['0.5','1.5','3','5']:
    tm=mp.mpf('.8'); Wm=mp.mpf(W); a=mp.sqrt(Wm)
    v=1-mp.exp(-2*tm); mu=a*mp.exp(-tm); sd=mp.sqrt(v)
    g=lambda y, mean: mp.exp(-(y-mean)**2/(2*v))/(mp.sqrt(2*mp.pi)*sd)
    num=mp.quad(lambda y:g(y,mu)-g(y,-mu), [a, mp.inf])
    den=mp.quad(lambda y:g(y,mu)-g(y,-mu), [0, mp.inf])
    verify(abs(num/den - F(W,tm))<mp.mpf('1e-50'), 'absorbing kernel quadrature W='+W)

print(f'PASS {N} independent symbolic/numerical assertions')
