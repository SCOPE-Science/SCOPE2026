"""Elementary numerical consistency checks for the exact four-node Fock sampling formula."""
import cmath
import math

nodes = [0j] + [math.sqrt(2) * cmath.exp(2j * math.pi * k / 3) for k in range(3)]
weights = [0.5] + [1 / 6] * 3
basis = [lambda z: 1 + 0j, lambda z: z, lambda z: z*z / math.sqrt(2)]
checks = 0
for i in range(3):
    for j in range(3):
        g = sum(w * basis[i](z) * basis[j](z).conjugate() for z, w in zip(nodes, weights))
        assert abs(g - (1 if i == j else 0)) < 1e-12
        checks += 1
for i in range(3):
    for j in range(3):
        g = sum(w * math.exp(abs(z)**2) * math.exp(-abs(z)**2) * basis[i](z) * basis[j](z).conjugate() for z, w in zip(nodes, weights))
        assert abs(g - (1 if i == j else 0)) < 1e-12
        checks += 1
for root in [-1+1j, -1-1j]:
    assert abs(1 + root + root*root / 2) < 1e-12
    checks += 1
for s1 in (-1, 1):
    for s2 in (-1, 1):
        for s3 in (-1, 1):
            assert abs(cmath.exp(3j*math.pi*(s1+s2+s3)/4)-1) > 0.25
            checks += 1
print('PASS:', checks, 'explicit finite consistency assertions')
