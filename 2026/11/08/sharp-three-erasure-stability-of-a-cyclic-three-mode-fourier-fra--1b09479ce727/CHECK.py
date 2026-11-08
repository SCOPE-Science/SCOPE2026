"""Independent finite sanity checks for three-erasure low-pass cyclic Fourier frames.

Requires numpy. This executable supplements, but does not replace, the proof.
"""
import cmath
import itertools
import math
import numpy as np

checks = 0
for n in range(6, 37):
    z = cmath.exp(2j * math.pi / n)
    U = np.array([[z ** (x * k) / math.sqrt(n) for k in range(3)]
                  for x in range(n)], dtype=complex)
    assert np.allclose(U.conj().T @ U, np.eye(3), rtol=0, atol=1e-12)
    checks += 1
    u = 1 + 2 * math.cos(2 * math.pi / n)
    v = 1 + 2 * math.cos(4 * math.pi / n)
    predicted_loss = (3 + (v + math.sqrt(v*v + 8*u*u))/2)/n
    expected_worst = {tuple(sorted(((j+k) % n for k in range(3)))) for j in range(n)}
    actual_worst = set()
    max_loss = -1.0
    min_ret = float('inf')
    for E in itertools.combinations(range(n),3):
        er = U[list(E)]
        loss = float(np.linalg.eigvalsh(er.conj().T @ er)[-1])
        retained = U[[i for i in range(n) if i not in E]]
        low = float(np.linalg.eigvalsh(retained.conj().T @ retained)[0])
        assert abs((1-loss)-low) < 1e-10, (n,E,loss,low)
        checks += 1
        assert loss <= predicted_loss + 1e-10, (n,E,loss,predicted_loss)
        checks += 1
        if abs(loss - predicted_loss) < 1e-10:
            actual_worst.add(E)
        max_loss=max(max_loss,loss)
        min_ret=min(min_ret,low)
    assert actual_worst == expected_worst, (n,actual_worst,expected_worst)
    checks += 1
    assert abs(max_loss-predicted_loss)<1e-10
    assert abs(min_ret-(1-predicted_loss))<1e-10
    assert min_ret>0
    checks += 3

# Independently test the absolute-kernel domination used in the proof.
for n in range(8, 151):
    u=1+2*math.cos(2*math.pi/n)
    v=1+2*math.cos(4*math.pi/n)
    assert u>v>=1-1e-12
    for d in range(2,n//2+1):
        assert abs(1+2*math.cos(2*math.pi*d/n)) <= v+1e-12
        checks+=1
print(f'CHECK_OK assertions={checks}')
