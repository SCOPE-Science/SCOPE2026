"""Standalone numerical spot checks of the symmetric two-zero kernel equation.
Analytic proof is in RESULT.md; these tests are not an exhaustive certificate.
Usage: python CHECK.py (requires mpmath).
"""
import mpmath as mp
mp.mp.dps = 85
checks = 0
for beta in range(1, 25):
    for eps in (mp.mpf('0.01'), mp.mpf('0.002')):
        q = 1 - eps
        r = mp.sqrt(q)
        root_indices = []
        for j in range(beta):
            omega = mp.e**(2 * mp.pi * mp.j * j / beta)
            v = omega
            for _ in range(40):
                f = v**(-beta) + eps**beta * (2-eps*v)**(-beta) - 1 - eps**beta * (2-eps)**(-beta)
                fp = -beta*v**(-beta-1) + beta*eps**(beta+1)*(2-eps*v)**(-beta-1)
                if abs(f) < mp.mpf('1e-73'):
                    break
                v -= f/fp
            t = 1-eps*v
            c = mp.cos(2*mp.pi*j/beta)
            in_disk = abs(t) < r
            predicted = c > mp.mpf('0.5') + mp.mpf('1e-44')
            assert in_disk == predicted, (beta,j,eps,t)
            assert abs(v-omega) < mp.mpf('1e-5'), (beta,j,eps,v,omega)
            assert abs(v**(-beta) + eps**beta * (2-eps*v)**(-beta)-1 - eps**beta*(2-eps)**(-beta)) < mp.mpf('1e-65')
            assert abs(1 + (eps*v/(2-eps*v))**beta - v**beta*(1+(eps/(2-eps))**beta)) < mp.mpf('1e-65')
            checks += 4
            if in_disk:
                root_indices.append(j)
        expected_per_cluster = 2 * ((beta + 5)//6) - 1
        assert len(root_indices) == expected_per_cluster, (beta,eps,root_indices)
        checks += 1
print('ANTIPODAL_KERNEL_CHECKS_PASS', checks)
