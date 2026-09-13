"""Half-line scaled singular-oscillator shooting for lane-1689.

Scaled 1D problem on (0,Z), Z=sqrt(n):
    -v'' + (z^2 + mu/z^2) v = e v,  v ~ z^{p} (p=1/2+nu) at 0, v(Z)=0.
Ground root e_n -> e0 = 2+2*nu.  Checks:
    lam/n -> e0,  (1/n) log A_n -> -1/2,
where A_n = |u'(1)| for u normalized on (0,1), A = n^{3/4}|v'(Z)|/||v||_Z.
"""
import mpmath as mp
import json

mp.mp.dps = 50
mu = mp.mpf('0.125')
nu = mp.sqrt(mu + mp.mpf('0.25'))
p = mp.mpf('0.5') + nu
e0 = 2 + 2*nu
den = (p+2)*(p+1) - mu  # series denominator

def shoot(e, Z, z0=mp.mpf('0.1')):
    e = mp.mpf(e)
    a = -e/den
    v0 = z0**p * (1 + a*z0**2)
    w0 = p*z0**(p-1)*(1 + a*z0**2) + z0**p*(2*a*z0)
    f = mp.odefun(lambda z, v, w: (z**2 + mu/z**2 - e)*v, z0, v0, w0)
    # odefun returns y(z); derivative via second component? Use mp.odefun with 2nd order:
    return f

def F(e, Z):
    # value v(Z;e) using first-order system form Y=[v,w]:
    # Y' = [w, (z^2+mu/z^2-e) v]
    e = mp.mpf(e)
    z0 = mp.mpf('0.1')
    a = -e/den
    v0 = z0**p * (1 + a*z0**2)
    w0 = p*z0**(p-1)*(1 + a*z0**2) + z0**p*(2*a*z0)
    g = mp.odefun(lambda z, Y: (Y[1], (z**2 + mu/z**2 - e)*Y[0]), z0, (v0, w0))
    return g(Z)[0]

def solve_ground(n):
    Z = mp.sqrt(mp.mpf(n))
    lo, hi = e0, e0 + 1
    Flo, Fhi = F(lo, Z), F(hi, Z)
    assert Flo > 0, f"n={n}: F(e0)={Flo} not positive"
    # expand hi until sign change
    while Fhi > 0:
        hi = e0 + (hi-e0)*2 + 1
        Fhi = F(hi, Z)
        if hi > e0 + 50:
            raise RuntimeError("no sign change")
    for _ in range(80):
        mid = (lo+hi)/2
        if F(mid, Z) > 0:
            lo = mid
        else:
            hi = mid
    e = (lo+hi)/2
    # recompute profile for derivative & norm
    z0 = mp.mpf('0.1')
    a = -e/den
    v0 = z0**p * (1 + a*z0**2)
    w0 = p*z0**(p-1)*(1 + a*z0**2) + z0**p*(2*a*z0)
    g = mp.odefun(lambda z, Y: (Y[1], (z**2 + mu/z**2 - e)*Y[0]), z0, (v0, w0))
    # derivative at Z via finite difference of the ODE solution (high precision)
    h = mp.mpf('1e-6')
    vp = (g(Z+h)[0] - g(Z-h)[0])/(2*h)
    # norm on (0,Z): series part + quad
    tail = mp.quad(lambda z: (g(z)[0])**2, [z0, Z])
    head = mp.quad(lambda z: (z**p*(1+a*z**2))**2, [mp.mpf('0'), z0])
    norm = mp.sqrt(head + tail)
    A = (mp.mpf(n)**mp.mpf('0.75'))*abs(vp)/norm
    lam = mp.mpf(n)*e
    return {'n': n, 'Z': float(Z), 'e': float(e), 'lam_over_n': float(e),
            'e_minus_e0': float(e-e0), 'A': float(A),
            'logA_over_n': float(mp.log(A)/n), 'lam': float(lam)}

if __name__ == '__main__':
    print("e0 =", e0, float(e0))
    print("Tstar candidate =", 1/(2*e0), float(1/(2*e0)))
    out = []
    for n in [2, 4, 6, 9, 12, 16]:
        r = solve_ground(n)
        out.append(r)
        print(r)
    with open('rates.json', 'w') as f:
        json.dump({'e0': float(e0), 'Tstar': float(1/(2*e0)), 'rows': out}, f, indent=2)
