# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Power-saving exponential upper bound for 4-term progression-free sets in F_5^n via the partition-rank polynomial method
- **Round:** 2026-09-14-hands-on-first-light-01
- **Lane:** 20316
- **Disposition:** NO_RESULT
- **Domain:** Additive Combinatorics
- **Method:** polynomial method and slice-rank analysis

## Problem

Let r_4(F_5^n) be the maximum |A| with A subset of F_5^n containing no four distinct elements x, x+d, x+2d, x+3d (d != 0). Prove there exist constants c with 1 < c < 5 (equivalently gamma > 0) and n_0 such that for all n >= n_0, r_4(F_5^n) <= c^n = 5^{(1-gamma)n}, via an explicit slice-rank / partition-rank upper bound on the associated 4-progression tensor, upgrading the Green-Tao bound r_4 << 5^n/n^{c} to an exponential power saving and pinning r_4 in a two-sided exponential window c_0^n <= r_4 <= c_1^n with 1 < c_0 <= c_1 < 5.

## Attempted claim

Let r_4(F_5^n) be the maximum |A| with A subset of F_5^n containing no four distinct elements x, x+d, x+2d, x+3d (d != 0). Prove there exist constants c with 1 < c < 5 (equivalently gamma > 0) and n_0 such that for all n >= n_0, r_4(F_5^n) <= c^n = 5^{(1-gamma)n}, via an explicit slice-rank / partition-rank upper bound on the associated 4-progression tensor, upgrading the Green-Tao bound r_4 << 5^n/n^{c} to an exponential power saving and pinning r_4 in a two-sided exponential window c_0^n <= r_4 <= c_1^n with 1 < c_0 <= c_1 < 5.

## Research outcome

Target blocked: every concrete slice-rank/partition-rank certificate for 4-APs in F_5^n fails, either provably trivial by the mean-threshold symmetry (budgets exceed ambient dimension for all n) or provably inapplicable by quantified diagonal failure ((81^n+4)/5 non-AP solutions on {0,1,2}^n); no independently valuable emergent increment was produced, so a clean exit with NO_RESULT is returned.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

The negative conclusion is scoped to explicit monomial-counting slice-rank and partition-rank certificates for the 4-progression tensor: exact two-equation, regrouped, and single-equation-relaxation routes are closed, but the investigation does not rule out a fundamentally different future method (e.g. higher-order Fourier analysis or a novel rank notion) proving the conjectured exponential bound.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: The negative conclusion is scoped to explicit monomial-counting slice-rank and partition-rank certificates for the 4-progression tensor: exact two-equation, regrouped, and single-equation-relaxation routes are closed, but the investigation does not rule out a fundamentally different future method (e.g. higher-order Fourier analysis or a novel rank notion) proving the conjectured exponential bound.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
