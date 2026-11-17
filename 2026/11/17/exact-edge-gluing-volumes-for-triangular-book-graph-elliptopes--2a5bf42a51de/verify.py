"""Reproduce exact book-graph volume identities and finite numerical checks.

The all-n theorem follows from the proof in RESULT.md, not from these finite checks.
Dependencies: Python 3, mpmath, numpy, scipy.
"""
from itertools import product
import math
import numpy as np
import mpmath as mp
from scipy.spatial import ConvexHull

mp.mp.dps = 70
checks = 0

def require(condition, description):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(description)

def cut_volume(n):
    return mp.power(2, n) * mp.beta(n + 1, n + 1)

def ell_volume(n):
    return mp.power(mp.pi / 2, n) * mp.beta(mp.mpf(n) / 2 + 1, mp.mpf(n) / 2 + 1)

def relerr(a, b):
    return abs(a - b) / max(mp.mpf('1e-65'), abs(b))

# Numerical integration independent of beta's evaluation.
for n in range(1, 24):
    q_num = mp.quad(lambda t: (mp.pi / 2 * mp.sqrt(t * (1 - t))) ** n,
                    [0, mp.mpf('.25'), mp.mpf('.5'), mp.mpf('.75'), 1])
    c_num = mp.quad(lambda t: (2 * t * (1 - t)) ** n,
                    [0, mp.mpf('.25'), mp.mpf('.5'), mp.mpf('.75'), 1])
    require(relerr(q_num, ell_volume(n)) < mp.mpf('1e-50'), f'ell beta n={n}')
    require(relerr(c_num, cut_volume(n)) < mp.mpf('1e-50'), f'cut beta n={n}')
    require(relerr(cut_volume(n), mp.power(2, n) * mp.factorial(n)**2 / mp.factorial(2*n+1)) < mp.mpf('1e-50'), f'factorials n={n}')
    require(ell_volume(n) >= cut_volume(n), f'containment n={n}')

# Direct 0/1 convex hull volumes of the original finite cut configurations.
for n in range(1, 5):
    cuts = []
    for bits in product([0, 1], repeat=n+1):
        # Fix hub a=0; one bit for the hub b and n bits for leaves.
        b, leaves = bits[0], bits[1:]
        cuts.append([b] + [z for v in leaves for z in (v, v ^ b)])
    hull = ConvexHull(np.array(cuts, dtype=float))
    require(abs(hull.volume - float(cut_volume(n))) < 2e-10,
            f'independent convex-hull volume n={n}')
    require(hull.ndim == 2*n+1, f'dimension n={n}')

# Each page's local triangles admit positive joint distributions,
# glued by conditional independence along the common hub spins.
for n in (1, 2, 3, 5):
    for j in range(14):
        t = -0.91 + 1.82*(j + .35)/14
        xys = []
        for i in range(n):
            theta = 2*math.pi*((7*i+11*j+3) % 31)/31
            radius = .03 + .94*((i*13+j*17+1)%23)/23
            # Elliptical Gram fiber, not necessarily binary feasible.
            x = radius * math.cos(theta)
            y = t*x + math.sqrt(1-t*t)*radius*math.sin(theta)
            xys.append((x, y))
            det = 1-t*t-x*x-y*y+2*t*x*y
            require(det > -1e-12, 'ellipsoid condition')
        # Explicit Gram completion, one new orthogonal residual per leaf.
        a = np.zeros(n+2)
        b = np.zeros(n+2)
        a[0] = 1
        b[0] = t
        b[1] = math.sqrt(1-t*t)
        vs = [a, b]
        for i,(x,y) in enumerate(xys):
            z = np.zeros(n+2)
            z[0] = x
            z[1] = (y-t*x)/math.sqrt(1-t*t)
            z[2+i] = math.sqrt(max(0, 1-z[0]**2-z[1]**2))
            vs.append(z)
            require(abs(np.dot(z, z)-1) < 3e-12, 'unit Gram leaf')
            require(abs(np.dot(z,a)-x) < 3e-12, 'Gram hub a')
            require(abs(np.dot(z,b)-y) < 3e-12, 'Gram hub b')
        require(np.min(np.linalg.eigvalsh(np.array(vs)@np.array(vs).T)) > -1e-10, 'PSD Gram completion')

# Verify exact binary joint spin extension of each local cut interval.
for n in (1, 2, 3):
    for j in range(9):
        t = -0.9 + .2*j
        pairs = []
        for i in range(n):
            alpha = (j + 2*i + 1)/ (2*n + 2*j + 10)
            beta = (3*i + j + 2) / (4*n + 4*j + 13)
            xplusy = (1+t)*(2*alpha-1)
            xminusy = (1-t)*(2*beta-1)
            x = (xplusy + xminusy)/2
            y = (xplusy - xminusy)/2
            pairs.append((x,y))
            require(abs(x+y) <= 1+t + 1e-13 and abs(x-y) <= 1-t+1e-13, 'binary facet conditions')
        law = {}
        for a,b in product((-1,1),repeat=2):
            probab=(1+t*a*b)/4
            for leaves in product((-1,1),repeat=n):
                p=probab
                for c,(x,y) in zip(leaves,pairs):
                    # Solve conditional spin mean for each (a,b):
                    # E[c|a,b]=(x*a+y*b)/(1+t*a*b).
                    m=(x*a+y*b)/(1+t*a*b)
                    require(abs(m)<=1+1e-12, 'valid conditional mean')
                    p*= (1+c*m)/2
                law[(a,b,*leaves)]=p
        require(abs(sum(law.values())-1)<2e-12, 'probability normalization')
        require(abs(sum(p*o[0]*o[1] for o,p in law.items())-t)<2e-12,'hub correlation')
        for i,(x,y) in enumerate(pairs):
            require(abs(sum(p*o[0]*o[2+i] for o,p in law.items())-x)<2e-12, 'hub-leaf x correlation')
            require(abs(sum(p*o[1]*o[2+i] for o,p in law.items())-y)<2e-12, 'hub-leaf y correlation')

# Quantitative check of the derived asymptotic coefficient (not a proof of the remainder).
for n in (100, 400, 1600, 6400):
    ratio = ell_volume(n)/cut_volume(n)
    normalized = ratio/(mp.sqrt(2)*mp.power(mp.pi/2,n))
    require(abs(normalized - (1-mp.mpf(3)/(8*n))) < mp.mpf('0.50')/n**2,
            f'first correction n={n}')

print(f'PASS: {checks} deterministic checks; 23 independent quadratures per body,')
print('four convex-hull volumes, Gram completions, binary joint extensions,')
print('and quantitative large-order asymptotics.')
for n in (1,2,3,4,6):
    print(f'n={n}: cut={float(cut_volume(n)):.12g} elliptope={float(ell_volume(n)):.12g} ratio={float(ell_volume(n)/cut_volume(n)):.12g}')
