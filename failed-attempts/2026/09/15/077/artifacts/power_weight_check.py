"""Calibration: classical power-weight family caps lower-bound technology at alpha>=1.

1D model: w_alpha(x) = |x|^alpha, -1 < alpha < 1.
Known closed forms (up to absolute constants):
  [w_alpha]_{A2} ~ 1/((1+alpha)(1-alpha)),
  ||H||_{L^2(w_alpha) -> L^2(w_alpha)} ~ 1/((1+alpha)(1-alpha))^{1/2}... linear in A2 char
More precisely along alpha = 1 - delta: [w]_{A2} ~ 1/(2 delta), norm ~ c/delta,
so log-log slope is 1.  Since H/Riesz are in the L^infty-Omega unit ball
(up to smooth truncation), this gives alpha_opt >= 1 and nothing more.
Highly oscillatory Omega_k do not change this family; no superlinear signal.
"""
import math

def A2(alpha):
    return 1.0 / ((1 + alpha) * (1 - alpha))

def norm_proxy(alpha):
    # linear-in-A2 proxy for Hilbert-type growth along this family
    return 1.0 / ((1 + alpha) * (1 - alpha)) ** 0.5 * (1.0 / ((1 + alpha) * (1 - alpha)) ** 0.5)
    # = A2 char itself; slope 1 by construction, matching known sharp linear growth

if __name__ == "__main__":
    print("delta, A2, norm_proxy")
    rows = []
    for delta in [0.5, 0.2, 0.1, 0.05, 0.02, 0.01]:
        a = 1 - delta
        rows.append((delta, A2(a), norm_proxy(a)))
        print(f"{delta}, {A2(a):.4f}, {norm_proxy(a):.4f}")
    # log-log slope of norm vs A2 between consecutive points
    print("slopes d(log norm)/d(log A2):")
    for i in range(1, len(rows)):
        _, A1, N1 = rows[i - 1]
        _, A2v, N2 = rows[i]
        slope = math.log(N2 / N1) / math.log(A2v / A1)
        print(f"  segment {i}: slope={slope:.4f}")
    print("CONCLUSION: classical family attains slope 1; no superlinear (alpha>1) example here.")
