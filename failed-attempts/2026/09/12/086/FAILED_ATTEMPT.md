# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Transverse KP-II stability threshold for KdV cnoidal at m=1/2
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1293
- **Disposition:** AUDIT_1_REJECT
- **Domain:** KP-II transverse stability of KdV periodic waves
- **Method:** Baker-Akhiezer Lax pair / linearized KP-II Floquet analysis

## Problem

Let u_cn(x,t) be the real KdV cnoidal wave of elliptic modulus m=1/2 and speed c fixed by the genus-1 Its-Matveev formula u_cn=-2 d_xx log theta(Ux+Vt+W|B)+C, viewed also through its KP Baker-Akhiezer extension with transverse coordinate y. Under the KP-II flow with transverse wavenumber k in R, decide the exact transverse stability threshold k_c>=0 such that u_cn is spectrally stable to perturbations proportional to exp(i k y) for |k|>k_c and spectrally unstable for 0<|k|<k_c, or prove no such positive threshold exists. A complete answer is a rigorous computation of the linearized KP-II spectrum about u_cn at m=1/2 from the Baker-Akhiezer Lax pair yielding the numerical value of k_c with certified error bounds, or a proof that stability changes at k=0 only.

## Attempted claim

Let u_cn(x,t) be the real KdV cnoidal wave of elliptic modulus m=1/2 and speed c fixed by the genus-1 Its-Matveev formula u_cn=-2 d_xx log theta(Ux+Vt+W|B)+C, viewed also through its KP Baker-Akhiezer extension with transverse coordinate y. Under the KP-II flow with transverse wavenumber k in R, decide the exact transverse stability threshold k_c>=0 such that u_cn is spectrally stable to perturbations proportional to exp(i k y) for |k|>k_c and spectrally unstable for 0<|k|<k_c, or prove no such positive threshold exists. A complete answer is a rigorous computation of the linearized KP-II spectrum about u_cn at m=1/2 from the Baker-Akhiezer Lax pair yielding the numerical value of k_c with certified error bounds, or a proof that stability changes at k=0 only.

## Research outcome

Exact KP-II transverse stability threshold k_c=1 for the KdV cnoidal wave at m=1/2: analytic zone-boundary eigenvalues plus certified Hill-matrix numerics.

## Why this attempt failed

Failed axes: correctness.

correctness: FAIL: the headline KP-II threshold k_c=1 is not established and the linearization sign is wrong for KP-II. From (u_t+6uu_x+u_xxx)_x+3u_yy=0 with exp(iky+lambda t)v, lambda v'+(L0 v)''-3k^2 v=0, so lambda D a=-D^2 L a+s a and the true Hill operator is M_true=-D L+s D^-1 (s=3k^2), not M=D L+s D^-1 stated. The report's zero condition (DLD+sI)w=0 and high-k Hamiltonian H=L-sQ^-1 inherit this sign; the independently verified exact pair DLD[sn dn]=-3 sn dn (sympy reduction gives (6cn^2+d_xx)cn^3=3cn exactly, hence DLD w2=-3w2, and F1/s=-3/4) therefore pins a zero of -DLD-sI=0, i.e. the KP-I operator M_KPI=-D L-s D^-1, not KP-II. Numerics showing closure at k=1 and gamma>0 on (0,1) match the wrong-sign operator and reproduce the expected KP-I long-wave instability, contradicting KP-II stability consensus. Separately, global KP-II stability on (1,sqrt(3)] rests on 6 sampled k values and dense-grid scans with noise floor 5e-10, not interval enclosures, so the two-sided exact cutoff lacks rigorous certification despite honest limitations.

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; address the recorded limitation: Global stability on (1,sqrt(3)] and instability on all of (0,1) rest on dense-grid numerics (noise floor ~1e-9), not interval-arithmetic enclosures; minimality of the DLD eigenvalue -3 (gap to -0.75) and the Krein-stable character of the s=3/4 crossing are numerically verified rather than analytically bounded; threshold value 1 is stated in the u_t+6uu_x+u_xxx=0 normalization and rescales with other KdV conventions.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
