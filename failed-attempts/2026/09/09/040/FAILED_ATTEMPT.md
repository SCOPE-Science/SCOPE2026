# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Explicit entropic-crystallization density regime for symmetrized multi-marginal Coulomb transport plans
- **Round:** 2026-09-07-first-light-01
- **Lane:** 377
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Calculus of Variations and Optimal Transport
- **Method:** entropic-regularization Gamma-convergence with exchange-symmetry reduction and Lieb-Oxford-type correlation estimates

## Problem

For the symmetric N-marginal Coulomb optimal transport (SCE) problem with uniform single-particle density on a reference cell, determine an explicit density regime (critical Wigner-Seitz radius interval) where entropic-regularized minimizers Gamma-converge to a lattice-concentrated Kantorovich minimizer versus remain diffuse, witnessed by a two-point correlation order parameter, using exchange-symmetry reduction and an explicit correlation lower bound.

## Attempted claim

For uniform density on the reference cell, there exists an explicit critical value rs* (with stated numeric bounds) such that for rs > rs* any limit of symmetric entropic-regularized minimizers concentrates near a specified lattice-like support (two-point correlation witness above threshold), while for rs below a second explicit value the minimizer is certified diffuse; proved via entropic Gamma-convergence, exchange-symmetric 2-body reduction, and an explicit Lieb-Oxford-type constant.

## Research outcome

Partial theorem (one-sided diffuse regime) for two-marginal Coulomb transport on the uniform cube cell: explicit per-pair correlation lower bound 1/(sqrt(3)L)>0.577/L, explicit product-cost upper bound <3.571/L, and certified diffuse regime eta=eps*L>=150 (equivalently eps*r_s>73.9 for N=2) where the unique entropic minimizer satisfies TV<0.1 to the product and mass <0.11 in every Monge tube. Full two-sided rs* crystallization threshold NOT claimed; crystallization side stated as conjecture with obstruction isolated.

## Why this attempt failed

Failed axes: value.

value: Headline judged alone, honestly delimited as one-sided N=2 diffuse lemma (full rs* crystallization, N-marginal reduction, Gamma recovery all explicitly open) — honesty does not rescue value. FAIL as textbook restatement + arbitrary-scope loose sufficient condition, not an exact invariant worth retrieving: (1) Proof is generic 3-line Pinsker argument applicable to any cost with finite product cost + pointwise lower bound: V_eps<=I, S<=(I-Cmin)/eps, TV<=sqrt(S/2). No Lieb-Oxford constant (1.58) used despite brief; lower bound is trivial diameter 1/(sqrt3 L), not LO-type density bound; product cap pi/2+2 at arbitrarily chosen a=1/2 with crude pi<3.142 is far from sharp (replayed MC mean ~1.883 vs cap 3.571, interval [1.877,1.890] inside [0.577,3.571]); tube cap is crude ball volume. (2) Thresholds eta>=150, tau=0.1, d/L=0.1, TV<0.1/<0.11, 73.9 are arbitrary sufficient-condition artifacts, not intrinsic exact order/constant/witness; varying tau/d gives continuum of equally trivial bounds. Mechanically implied once gap is bounded; future researcher needing diffuse control would re-derive sharper bound in minutes, not retrieve 150/73.9. (3) No transferable crystallization obstruction: N=2 symmetrization vacuous, no exchange-symmetric 2-body reduction proved, no lattice ansatz upper bound, no two-point symmetry-breaking witness beyond ball volume, no Gamma-convergence, regime is regularization-dominated (large eps*L) not low-density Wigner order. Falls under STANDARD reject categories: textbook Pinsker instantiation, mere parameter substitution (Coulomb cube plugged into generic bound), arbitrary slice of (tau,d/L) choices, certification of loose numbers does not rescue per instructions. Narrow-datum allowance does not apply because value is mechanically implied, not exact, and not reasonably needed later.

## Conditions for a legitimate retry

supply independent motivation and a materially stronger contribution; address the recorded limitation: One-sided only: proves an explicit DIFFUSE regime at strong regularization (small L / large eps), not lattice crystallization at low density; no lower rs* crystallization threshold claimed. N=2 only (symmetrization vacuous); no exchange-symmetric N-marginal 2-body reduction proved. No full entropic Gamma-convergence with recovery at singular graph plans (constant sequence fails there; marginal-preserving smoothing not constructed). Monge-tube exclusion uses the crude ball-volume cap and the dia…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
