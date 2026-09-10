# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Quantified all-vector QUE variance rate for random 3-regular graphs via eigenvector moment flow
- **Round:** 2026-09-07-first-light-01
- **Lane:** 643
- **Disposition:** NO_RESULT
- **Domain:** Random Matrix Theory
- **Method:** eigenvector moment flow / Dyson Brownian motion comparison with Kesten-McKay resolvent input

## Problem

Establish a quantified all-vector QUE variance rate for uniform random 3-regular graphs in a fixed central bulk window: a polynomial equidistribution-error decay for bounded zero-mean observables proved via short-time eigenvector moment flow / Dyson Brownian motion comparison with Kesten-McKay resolvent input — a fluctuation question the known sup-norm theorems do not imply.

## Attempted claim

For uniform random 3-regular graphs on n (even) vertices with l2-normalized adjacency eigenvectors, let I0=[-1,1] be the fixed central bulk window. With probability >=1-n^{-1/2}, every eigenvector psi with eigenvalue in I0 satisfies |sum_{i=1}^n a(i)*psi(i)^2| <= (log n)^{C1} / n^{alpha} for all deterministic test vectors a with sum_i a(i)=0 and ||a||_inf<=1, with explicit stated alpha=1/4 and explicit stated integer C1, proved via a short-time eigenvector-moment-flow / Dyson Brownian motion variance comparison with Kesten-McKay resolvent input.

## Research outcome

Target (per-vector alpha=1/4 QUE rate at d=3 via moment flow) blocked: missing fixed-d=3 gap lower bound, regularity-breaking DBM comparison, compounding uniformization. Exact fallback (mean-square beta=1/4 for canonical half-volume a*) attempted directly and blocked on the same gap/comparison inputs (sup-norm route excluded by qualification); seeded probes consistent with rates but not proofs. Clean exit with NO_RESULT.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

['No analytic variance/moment-flow inequality proved; exact fallback certificate (N0,beta=1/4,C0) not met — binary criterion requires proof, not numerics.', 'Numeric evidence is small-scale (n<=800, few trials, configuration-model sampling) and diagnostic only; one n=400 mean-square outlier (nY=1.33) shows sampling noise.', 'No emergent original theorem/obstruction banked; half-localized separator and gap/comparison gaps are cited priors/analysis, not new results.']

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: ['No analytic variance/moment-flow inequality proved; exact fallback certificate (N0,beta=1/4,C0) not met — binary criterion requires proof, not numerics.', 'Numeric evidence is small-scale (n<=800, few trials, configuration-model sampling) and diagnostic only; one n=400 mean-square outlier (nY=1.33) shows sampling noise.', 'No emergent original theorem/obstruction banked; half-localized separator and gap/comparison gaps are cited priors/analysis, not new results.']

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
