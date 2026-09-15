"""Bounded recovery test for GHPUL full-loop-ensemble target.

Question: can the "small bubbles / small loops are uniformly negligible" step be
closed with only the inputs behind Gwynne-Miller Thm 1.2 (3/2-stable boundary-length
Levy process + Brownian-disk scaling of bubbles)?

Test A: expected total diameter of epsilon-small swallowed bubbles per unit
quantum-natural time, via Campbell's formula, using:
  - jump (bubble-boundary-length) density  nu(dx) = c_* x^{-5/2} dx  (3/2-stable,
    as in the GM peeling boundary-length process),
  - mean disk diameter scaling  E[diam | length x] ~ K x^{1/2}.
If this diverges as eps -> 0, the naive "sum of diameters" route to loop-ensemble
approximation fails and a genuinely loop-level tightness input is needed.

Test B: expected NUMBER of eps-small bubbles with diameter > delta (fixed delta),
assuming a Gaussian-type disk diameter tail  P(diam > delta | x) <= C exp(-c delta^2/x).
This tests whether even diameter-scale (not loop-level) uniformity is available in
principle, and what inputs it needs.
"""
import mpmath as mp

mp.mp.dps = 30

C_STAR = 1.0  # overall constant irrelevant for convergence/divergence
K = 1.0

# ---- Test A: E[sum of diameters of bubbles with length in (0, eps)] ----
def total_diam_integrand(x):
    return K * x**mp.mpf('0.5') * C_STAR * x**mp.mpf('-2.5')  # = x^{-2}

for eps in ['0.1', '0.01', '0.001']:
    e = mp.mpf(eps)
    # integral_e^1 x^{-2} dx = 1/e - 1
    val = 1 / e - 1
    print(f"Test A: eps={eps}: E[total diam of eps-small bubbles per unit time] ~ {val} (const factors omitted)")

print("Test A conclusion: diverges like 1/eps -> naive diameter-sum route FAILS.")
print()

# ---- Test B: E[count of bubbles with length < eps and diam > delta] ----
def expected_bad(eps, delta, c=1.0, C=1.0):
    f = lambda x: C * mp.e**(-c * delta**2 / x) * C_STAR * x**mp.mpf('-2.5')
    return mp.quad(f, [mp.mpf('0'), mp.mpf(eps)])

for delta in ['0.5', '0.2']:
    for eps in ['0.1', '0.01', '0.001']:
        print(f"Test B: delta={delta} eps={eps}: E[N_bad] = {float(expected_bad(eps, mp.mpf(delta))):.3e}")

print("Test B conclusion: diameter-scale uniformity would follow IF a uniform")
print("Gaussian-type disk-diameter tail held for Boltzmann quadrangulations uniformly")
print("in n AND conditional independence held at discrete level. Even then, GHPUL")
print("needs loop-level equicontinuity (arm-type) estimates, which are absent.")
