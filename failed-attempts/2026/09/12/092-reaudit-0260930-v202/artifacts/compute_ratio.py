"""Reproducible high-precision check of L(E2,2)/pi vs (1/12) D_q(xi).
E2: y^2=x^3+1 (36a1). U=(2,3) order 6, V=(-1,0) order 2, xi=3[U]-[V].
Method: PARI (cypari) for periods/torsion/L-value; mpmath for Bloch-Wigner + D_q sums.
"""
import mpmath
mpmath.mp.dps = 80
import cypari
pari = cypari.pari
pari.set_real_precision(120)

E = pari.ellinit([0,0,0,0,1])
def p2m(z):
    r = str(pari.real(z)).replace(' ','').replace('E','e')
    i = str(pari.imag(z)).replace(' ','').replace('E','e')
    return mpmath.mpc(mpmath.mpf(r), mpmath.mpf(i))

om = pari.ellperiods(E)
w1, w2 = om[0], om[1]
q = p2m(pari.exp(2*pari.Pi()*pari.I()*w1/w2))
print("q =", q, "\n|q| =", abs(q))

def D_bw(z):
    if z == 0: return mpmath.mpf('0')
    if abs(z-1) < mpmath.mpf('1e-70'): return mpmath.mpf('0')
    if abs(z) > 1: return -D_bw(1/z)
    return mpmath.im(mpmath.polylog(2, z)) + mpmath.arg(1-z)*mpmath.log(abs(z))

def Dq(z, M=60):
    return sum((D_bw((q**n)*z) for n in range(-M, M+1)), mpmath.mpf('0'))

pts = {"U(2,3)": pari([2,3]), "mU(2,-3)": pari([2,-3]),
       "V(-1,0)": pari([-1,0]), "A(0,1)": pari([0,1])}
for k,P in pts.items():
    t = pari.ellpointtoz(E, P)
    z = p2m(pari.exp(2*pari.Pi()*pari.I()*t/w2))
    print(k, "z =", z, "|z| =", abs(z), "Dq =", Dq(z))

zU = p2m(pari.exp(2*pari.Pi()*pari.I()*pari.ellpointtoz(E, pari([2,3]))/w2))
zV = p2m(pari.exp(2*pari.Pi()*pari.I()*pari.ellpointtoz(E, pari([-1,0]))/w2))
for M in [10, 30, 60, 90]:
    print("M", M, Dq(zU, M), Dq(zV, M))
Dxi = 3*Dq(zU, 90) - Dq(zV, 90)
L2 = mpmath.mpf(str(pari.lfun(pari.lfuncreate(E), 2)).replace(' ','').replace('E','e'))
r = (L2/mpmath.pi)
print("L2 =", L2, "\nL2/pi =", r, "\nDxi =", Dxi, "\nDxi/12 =", Dxi/12)
print("ratio (L2/pi)/Dxi =", r/Dxi, "\n+4/27 =", mpmath.mpf(4)/27)
print("gap L2/pi - Dxi/12 =", r - Dxi/12)
