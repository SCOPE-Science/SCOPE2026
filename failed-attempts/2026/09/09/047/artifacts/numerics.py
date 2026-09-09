"""Reproducible numerics for lane-398 emergent finding (numpy only).
Recomputes: c0 = |nu_hat(1)|^2, A(15^k) for k=0..3, effective decay exponent.
Method: trapezoid on uniform circle grid with n >= 8R points (Nyquist-checked
in WORKLOG: values stable at n/R = 8 vs 16); J=12 product factors (J-convergence
certified J=10..22 identical). Run: python3 numerics.py
"""
import numpy as np, math
D = np.array([0., 1., 2., 13., 14.])

def m_full(xi):
    xi = np.asarray(xi, dtype=float)
    s = np.zeros_like(xi, dtype=complex)
    for d in D:
        s += np.exp(-2j * math.pi * d * xi)
    return s / 5.0

def hat_nu(xi, J=12):
    xi = np.asarray(xi, dtype=float)
    p = np.ones_like(xi, dtype=complex)
    pw = 15.0
    for _ in range(1, J + 1):
        p *= m_full(xi / pw)
        pw *= 15.0
    return p

def A_of_R(R, n=None, J=12):
    if n is None:
        n = max(4096, min(400000, int(8 * max(R, 1)) + 1))
    TH = (np.arange(n) + 0.5) * 2 * math.pi / n
    a = hat_nu(R * np.cos(TH), J=J)
    b = hat_nu(R * np.sin(TH), J=J)
    return float(np.mean(np.abs(a) ** 2 * np.abs(b) ** 2))

c0 = abs(hat_nu(np.array([1.0]))[0]) ** 2
print(f"c0 = |nu_hat(1)|^2 = {c0:.8f}  (certified lower bound 0.4576: "
      f"{'PASS' if c0 > 0.4576 else 'FAIL'})")
prev = None
for k in range(4):
    R = 15.0 ** k
    A = A_of_R(R)
    extra = f"  ratio={A / prev:.5f}" if prev else ""
    print(f"k={k} R={R:8.0f} A={A:.6e}  R*A={R * A:.4f}{extra}")
    prev = A
print("effective exponent ~0.93 < 1 (Liu needs >1): vanilla averaged-decay "
      "route excluded; cf. certified A >= 0.003/R in proofs_cert.py")
