"""Model tail ledger for Monguzzi-Peloso witness g at beta_* = 3*pi/2.

Verifies the analytic exponents behind Lemmas 4.2-4.3 of arXiv:1611.07734
and shows the L^2 vs W^{1,2} split at the 0-end. This concerns the MODEL
distinguished boundary only; it does NOT prove anything about the smooth
worm topological boundary (transfer is blocked, see WORKLOG).

Run: python3 output/artifacts/model_tail_ledger.py
"""
import math

beta = 1.5 * math.pi
nu = math.pi / (2 * beta - math.pi)
print(f"beta* = {beta:.6f} (= 3pi/2)")
print(f"nu_beta = {nu:.6f}")
print(f"nu/2 (Sobolev threshold) = {nu/2:.6f}")
print(f"L^p range: ({2/(1+nu):.6f}, {2/(1-nu):.6f})")
print(f"s=1 >= nu/2={nu/2}: model predicts W^(1,2) FAILURE on distinguished boundary")

# Tails from Lemmas 4.2/4.3: P11g(x) ~ x^{-(nu+1)/2} (x>1), ~ x^{(nu-1)/2} (0<x<1)
a_inf = (nu + 1) / 2   # 0.75
a_zero = (nu - 1) / 2  # -0.25
print(f"\nTail exponents: x>{1}: x^{{-a_inf}}, a_inf={a_inf}; 0<x<1: x^{{a_zero}}, a_zero={a_zero}")

def quad_power(c, lo, hi, n=2000000):
    # integrate x^c dx on [lo,hi] numerically (log-spaced for singular end)
    import math
    total = 0.0
    # log spacing
    l0, l1 = math.log(lo), math.log(hi)
    prev = lo
    for k in range(1, n + 1):
        cur = math.exp(l0 + (l1 - l0) * k / n)
        mid = math.sqrt(prev * cur)
        total += mid ** c * (cur - prev)
        prev = cur
    return total

# L^2 density exponent near 0: 2*a_zero = nu-1 = -0.5 -> integrable
# W^{1,2} derivative density exponent near 0: 2*(a_zero-1) = nu-3 = -2.5 -> divergent
e_L2_0 = 2 * a_zero
e_W12_0 = 2 * (a_zero - 1)
print(f"\nNear-0 density exponents: L^2: {e_L2_0} (> -1 => converges); d/dx term: {e_W12_0} (<= -1 => DIVERGES)")
# analytic antiderivatives
lo = 1e-8
I_L2 = (1.0 ** (e_L2_0 + 1) - lo ** (e_L2_0 + 1)) / (e_L2_0 + 1)
print(f"Analytic int_[{lo},1] x^{{{e_L2_0}}} dx = {I_L2:.6f} (finite: L^2 OK)")
# divergent one: partial integral from lo to 1 grows like lo^{e+1}/|e+1|
e = e_W12_0
I_div = (1.0 ** (e + 1) - lo ** (e + 1)) / (e + 1)
print(f"Analytic int_[{lo},1] x^{{{e}}} dx = {I_div:.3e} (blows up as lo->0: W^{{1,2}} FAILS on model)")

# L^2 at infinity, p=2: exponent -2*a_inf = -(nu+1) = -1.5 -> integrable
e_inf = -2 * a_inf
I_inf = 1.0 / abs(e_inf + 1)  # int_1^oo x^{e} dx with e<-1
print(f"\nAt infinity: |P|^2 ~ x^{{{e_inf}}}, int_1^oo = {I_inf:.6f} (finite)")

# Numeric spot check with coarse log quadrature
n_num_L2 = quad_power(e_L2_0, 1e-6, 1.0, n=200000)
print(f"Numeric int_[1e-6,1] x^{{{e_L2_0}}} dx ~ {n_num_L2:.6f} (expect ~2.0)")

print("\nConclusion: MODEL witness fails W^{1,2} at 0-end. Smooth-worm transfer: NOT established.")
