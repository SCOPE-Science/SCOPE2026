"""Fast scaled singular-oscillator ground-state solver (numpy only).

Scaled half-line problem on (0,Z), Z=sqrt(n):
    -v'' + (z^2 + mu/z^2) v = e v,  v(0)=0 (Friedrichs), v(Z)=0.
Inverse iteration + Thomas solver (O(M) per step). Checks:
    e(Z) -> e0 = 2+2*nu,   (1/n) log A_n -> -1/2,
with A_n = |u_n'(1)|, u_n(x)=n^{1/4} v(sqrt(n)x)/||v||.
"""
import numpy as np
import json

mu = 0.125
nu = np.sqrt(mu + 0.25)
p = 0.5 + nu
e0 = 2.0 + 2.0 * nu
Tstar = 1.0 / (2.0 * e0)

def ground(Z, M=12000, iters=60):
    h = Z / M
    z = np.linspace(0, Z, M + 1)
    zi = z[1:M]  # interior points
    pot = zi**2 + mu / zi**2
    d = 2.0 / h**2 + pot          # main diag of A
    off = -np.ones(M - 2) / h**2  # off diag
    # inverse iteration with fixed shift sigma slightly below e0
    sigma = e0 - 0.5
    dm = d - sigma
    # Thomas factorization of tridiag(dm, off, off), reused
    cp = np.zeros(M - 2)
    cp[0] = off[0] / dm[0]
    for i in range(1, M - 2):
        cp[i] = off[i] / (dm[i] - off[i-1] * cp[i-1])
    v = zi**p * np.exp(-zi**2 / 2.0)  # exact half-line ground as start
    v = v / np.linalg.norm(v)
    for _ in range(iters):
        # solve (A-sI) y = v via Thomas
        dp = np.zeros(M - 1)
        dp[0] = v[0] / dm[0]
        for i in range(1, M - 1):
            dp[i] = (v[i] - off[i-1] * dp[i-1]) / (dm[i] - off[i-1] * cp[i-1])
        y = np.zeros(M - 1)
        y[-1] = dp[-1]
        for i in range(M - 3, -1, -1):
            y[i] = dp[i] - cp[i] * y[i+1]
        v = y / np.linalg.norm(y)
    # Rayleigh quotient
    Av = d * v
    Av[:-1] += off * v[1:]
    Av[1:] += off * v[:-1]
    e = float(v @ Av)
    # norm on (0,Z) incl. head series part: head ~ int_0^{z1} z^{2p} dz
    z1 = zi[0]
    C = (v[0] / (z1**p * np.exp(-z1**2/2.0)))  # match constant ~1
    head = (C**2) * z1**(2*p+1) / (2*p+1)
    trap = np.trapz(v**2, zi)
    norm = np.sqrt(head + trap)
    # v'(Z): v_M = 0
    vp = (3*0.0 - 4*v[-1] + v[-2]) / (2*h)
    return e, abs(vp)/norm

if __name__ == '__main__':
    print(f"e0={e0:.10f}  Tstar={Tstar:.10f} = (4-sqrt(6))/10 = {(4-np.sqrt(6))/10:.10f}")
    rows = []
    for n in [4, 6, 9, 12, 16, 20, 25]:
        Z = np.sqrt(n)
        M = 15000 if n <= 16 else 20000
        e, B = ground(Z, M=M)
        A = (n**0.75) * B
        rows.append({'n': n, 'e': e, 'e-e0': e-e0, 'A': A,
                     'logA/n': np.log(A)/n})
        print(f"n={n:3d} Z={Z:.3f} e={e:.8f} e-e0={e-e0:.2e} "
              f"logA/n={np.log(A)/n:.6f} (target -0.5 + O(log n / n))")
    with open('rates.json', 'w') as f:
        json.dump({'e0': e0, 'Tstar': Tstar, 'rows': rows}, f, indent=2)
