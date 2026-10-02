"""Closed-form cross-check: tau=(-1+i sqrt3)/2, q=-exp(-pi sqrt3);
z_U=i exp(-5 pi sqrt3/6), z_V=-i exp(-pi sqrt3/2); Euler partial sums for L(E,2)."""
import mpmath
mpmath.mp.dps = 60
import cypari
pari = cypari.pari
pari.set_real_precision(120)
E = pari.ellinit([0,0,0,0,1])
om = pari.ellperiods(E); w1, w2 = om[0], om[1]
def p2m(z):
    r = str(pari.real(z)).replace(' ','').replace('E','e')
    i = str(pari.imag(z)).replace(' ','').replace('E','e')
    return mpmath.mpc(mpmath.mpf(r), mpmath.mpf(i))
print("tau-(-1+isqrt3)/2 =", p2m(w1/w2) - mpmath.mpc(mpmath.mpf('-0.5'), mpmath.sqrt(3)/2))
print("q+exp(-pi sqrt3) =", p2m(pari.exp(2*pari.Pi()*pari.I()*w1/w2)) + mpmath.e**(-mpmath.pi*mpmath.sqrt(3)))
zU = p2m(pari.exp(2*pari.Pi()*pari.I()*pari.ellpointtoz(E,pari([2,3]))/w2))
zV = p2m(pari.exp(2*pari.Pi()*pari.I()*pari.ellpointtoz(E,pari([-1,0]))/w2))
print("zU - i exp(-5pi sqrt3/6) =", zU - mpmath.j*mpmath.e**(-5*mpmath.pi*mpmath.sqrt(3)/6))
print("zV + i exp(-pi sqrt3/2) =", zV + mpmath.j*mpmath.e**(-mpmath.pi*mpmath.sqrt(3)/2))
for N in [500, 2000, 8000]:
    s = mpmath.nsum if False else None
    tot = mpmath.mpf('0')
    for n in range(1, N+1):
        tot += mpmath.mpf(int(pari.ellak(E,n)))/mpmath.mpf(n)**2
    print("euler partial N=", N, tot)
print("pari lfun L2 =", pari.lfun(pari.lfuncreate(E), 2))
