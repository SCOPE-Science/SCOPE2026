# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Sharp Gaussian threshold for a benign Burer–Monteiro landscape at exact parametrization
- **Round:** 2026-09-14-hands-on-first-light-01
- **Lane:** 20387
- **Disposition:** NO_RESULT
- **Domain:** Discrete Optimization
- **Method:** Gaussian width and dual certificate analysis

## Problem

Let n→∞ with fixed true rank r*≥1. Let M* in S^{n×n}, M*⪰0, rank(M*)=r*, and let A:S^{n×n}→R^m have i.i.d. N(0,1/m) entries. Consider the exactly parametrized Burer–Monteiro least-squares objective f(X)=(1/2m)||A(XX^T−M*)||^2, X in R^{n×r*}. Call X a spurious second-order critical point if ∇f(X)=0, ∇^2f(X)⪰0, and XX^T≠M*. Let δ*=δ(D(||·||_*,M*)) be the Amelunxen–Lotz–McCoy–Tropp statistical dimension of the nuclear-norm descent cone at M*. Decide the following sharp-threshold statement, by proof or disproof with a corrected threshold if false: For every fixed ε>0: (i) if m≥(1+ε)δ* then P[f has no spurious second-order critical point]→1; (ii) if m≤(1−ε)δ* then P[f has a spurious second-order critical point]→1.

## Attempted claim

Let n→∞ with fixed true rank r*≥1. Let M* in S^{n×n}, M*⪰0, rank(M*)=r*, and let A:S^{n×n}→R^m have i.i.d. N(0,1/m) entries. Consider the exactly parametrized Burer–Monteiro least-squares objective f(X)=(1/2m)||A(XX^T−M*)||^2, X in R^{n×r*}. Call X a spurious second-order critical point if ∇f(X)=0, ∇^2f(X)⪰0, and XX^T≠M*. Let δ*=δ(D(||·||_*,M*)) be the Amelunxen–Lotz–McCoy–Tropp statistical dimension of the nuclear-norm descent cone at M*. Decide the following sharp-threshold statement, by proof or disproof with a corrected threshold if false: For every fixed ε>0: (i) if m≥(1+ε)δ* then P[f has no spurious second-order critical point]→1; (ii) if m≤(1−ε)δ* then P[f has a spurious second-order critical point]→1.

## Research outcome

Target blocked and exited cleanly: the sharp two-sided benign-landscape threshold at the nuclear-norm descent statistical dimension delta* could be neither proved nor refuted. Routes attempted: (1) identifying delta* versus the 2n-1 secant threshold via Monte Carlo bounds; (2) proving part (ii) via generic non-uniqueness below secant dimension; (3) proving part (i) from convex success plus second-order conditions. Bounded small-n probes were inconclusive for the sharp constant; no independently valuable emergent finding resulted.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

No proof or disproof of either part of the sharp (1+/-eps)delta* threshold was obtained. Evidence is limited to loose Monte Carlo upper bounds on delta*, uncertified small-n gradient-descent scans that cannot resolve asymptotic constants, and standard first/second-order derivations; a sharp Gaussian landscape analysis or certified counterexample remains open.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: No proof or disproof of either part of the sharp (1+/-eps)delta* threshold was obtained. Evidence is limited to loose Monte Carlo upper bounds on delta*, uncertified small-n gradient-descent scans that cannot resolve asymptotic constants, and standard first/second-order derivations; a sharp Gaussian landscape analysis or certified counterexample remains open.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
