"""Numerical checks of the exact Szego Gram reduction and the collision limit.

Usage: python CHECK.py   (requires mpmath)
Finite checks do not replace the analytic proof.
"""
from mpmath import mp

mp.dps = 85
checks = 0


def check(statement, label):
    global checks
    assert statement, label
    checks += 1


def smallest_gram(points):
    n = len(points)
    gram = mp.matrix([[mp.sqrt((1-abs(points[i])**2)*(1-abs(points[j])**2)) /
                       (1-mp.conj(points[i])*points[j]) for j in range(n)]
                      for i in range(n)])
    eigenvals, eigenvecs = mp.eighe(gram)
    return eigenvals[0], eigenvecs


def bary_weights(nodes):
    return [1/mp.fprod(nodes[j]-nodes[k] for k in range(len(nodes)) if k != j)
            for j in range(len(nodes))]


for n in range(2, 7):
    roots = [mp.e**(2*mp.pi*mp.j*k/n) for k in range(n)]
    for ee in ['.08', '.2', '.37', '.65']:
        eps = mp.mpf(ee)
        val, vec = smallest_gram([eps*z for z in roots])
        exact = n*(1-eps**2)*eps**(2*n-2)/(1-eps**(2*n))
        check(abs(val/exact-1) < mp.mpf('1e-60'), ('roots', n, ee))
        weights = bary_weights(roots)
        limit_constant = 1/sum(abs(w)**2 for w in weights)
        check(abs(limit_constant-n) < mp.mpf('1e-60'), ('roots_constant', n))

for n in [2, 3, 4, 5]:
    zetas = [mp.mpc(j, ((j*7) % 5)/4) for j in range(n)]
    a = mp.mpc('.17', '.24')
    weights = bary_weights(zetas)
    limit_constant = 1/((1-abs(a)**2)**(2*n-2)*sum(abs(w)**2 for w in weights))
    last_error = mp.inf
    for ee in ['.04', '.02', '.01', '.005']:
        eps = mp.mpf(ee)
        points = [a+eps*z for z in zetas]
        val, v = smallest_gram(points)
        ratio = val/(eps**(2*n-2)*limit_constant)
        error = abs(ratio-1)
        check(error < last_error, ('trend', n, ee, mp.nstr(ratio, 9)))
        last_error = error
        check(val > 0, ('positive', n, ee))
        norm_w = mp.sqrt(sum(abs(w)**2 for w in weights))
        correlation = abs(sum(mp.conj(weights[j])*v[j, 0] for j in range(n)))/norm_w
        check(correlation > mp.mpf('.95'), ('weak_direction', n, ee))

print('FOCK_DILATION_SZego_COLLISION_CHECK_OK', checks)
