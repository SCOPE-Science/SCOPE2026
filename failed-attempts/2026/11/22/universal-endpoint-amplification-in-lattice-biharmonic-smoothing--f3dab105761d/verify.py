"""Independent finite checks for the lattice biharmonic smoothing resolvent.

Run: python3 verify.py
Only the Python standard library is required. Finite tests do not prove limits.
"""
import cmath
import math

COUNT = 0


def check(ok, msg):
    global COUNT
    COUNT += 1
    if not ok:
        raise AssertionError(msg)


def inner_root(lam):
    t = 2 + 1j / math.sqrt(lam)
    d = cmath.sqrt(t * t - 4)
    roots = ((t + d) / 2, (t - d) / 2)
    r = min(roots, key=abs)
    check(abs(r) < 1, "selected root lies inside the disk")
    return r


def kernel_coefficients(lam, truncation):
    r = inner_root(lam)
    pd = 2*r + 4*lam*(r-1)**3
    g = [2*(r**(k+1)/pd).real for k in range(truncation+1)]
    tail = 4*abs(r)**(truncation+2)/(abs(pd)*(1-abs(r)))
    return g, tail


def cyclic_fourier(n, lam):
    weights = [1/(1+lam*(2-2*math.cos(2*math.pi*j/n))**2) for j in range(n)]
    return [sum(weights[j]*math.cos(2*math.pi*j*k/n) for j in range(n))/n for k in range(n)]


def periodization(g,n):
    return [sum(g[abs(k)] for k in range(-len(g)+1,len(g)) if k%n==j) for j in range(n)]


for lam in (0.0001, 0.01, 1., 100., 10000., 1000000., 1e8):
    length = max(300, int(45*lam**0.25))
    g,tail = kernel_coefficients(lam,length)
    norm = g[0] + 2*sum(abs(x) for x in g[1:])
    mass = g[0] + 2*sum(g[1:])
    check(abs(mass-1) <= max(1e-10,tail*2), f"row mass lam={lam}")
    check(norm > 1.000000001, f"nontrivial gain lam={lam}")
    check(g[0]>0, f"positive central weight lam={lam}")
    for n in (3,4,5,7,11,17):
        cyc=cyclic_fourier(n,lam)
        period=periodization(g,n)
        for a,b in zip(cyc,period):
            check(abs(a-b)<1e-8+tail, f"Fourier/periodization at n={n}, lam={lam}: {a} {b}")
        check(abs(sum(cyc)-1)<1e-9, "cyclic mass one")
        check(sum(abs(x) for x in cyc)<=norm+1e-7, "periodization triangle bound")
    print(f"lambda={lam:g}  infinite-norm approx={norm:.12f}  tail<={tail:.3g}")

C=1+math.sqrt(2)*math.exp(-3*math.pi/4)/(1-math.exp(-math.pi))
check(1.14<C<1.141, "continuum universal constant")
for lam,tol in ((1e4,1e-3),(1e6,5e-5),(1e8,5e-6)):
    g,tail = kernel_coefficients(lam,max(300,int(45*lam**0.25)))
    gain=g[0]+2*sum(abs(x) for x in g[1:])
    check(abs(gain-C)<tol, f"continuum scaling: {lam}")
for n in (3,4,7,11):
    last=cyclic_fourier(n,1e6)
    check(abs(sum(abs(x) for x in last)-1)<1e-4, "fixed finite cycle large-lambda limit")

print(f"CHECK_OK {COUNT} assertions; limiting constant={C:.15f}")
