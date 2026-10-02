---
audit_date: 2026-10-01
status: failed
---

# Independent scientific audit

## Final claim

For a positive reversible Markov chain and one centered observable, the exact first two autocorrelations give the displayed sharp two-point envelopes for every later autocorrelation and finite-horizon variance, plus a sharp long-run lower bound and no finite long-run upper bound when the spectral variance is positive.

## Correctness — PASS

The spectral theorem represents the normalized autocorrelations as moments of a probability measure on \([0,1]\). Quadratic Hermite interpolation at the two canonical support pairs gives the stated lower and upper expectation bounds whenever the third derivative is nonnegative. Substitution of powers and of the finite-horizon variance polynomial gives the later-lag and sample-mean formulas. The long-run lower bound follows by monotone approximation of \((1+x)/(1-x)\), and the explicit two-point family with an atom tending to one preserves the first two moments while sending long-run variance to infinity. The actual verifier was inspected and an independent exact check reproduced the canonical moments and worked lag-three interval.

**Checked sources.** assigned RESULT.md at frozen tree afda3bbce99762d3028b22f274dee11a89bfb54f; artifacts/verify_two_lag_envelopes.py blob 77f72d44d1e2d3b02044699eb346f71f21efdc75; Berg--Song 2023 reversible-chain moment representation; classical Hausdorff and Markov--Krein moment theory

**Residual risks.** No correctness defect was found.

## Originality — FAIL

The mathematical core is already covered at the implication level by two established ingredients: reversible-chain autocovariances are a compactly supported moment sequence, and classical Markov--Krein/truncated Hausdorff theory gives best upper and lower expectations under finitely many moment constraints via canonical finitely supported measures. The displayed later-lag and finite-horizon formulas are direct substitutions into that general theorem; the long-run dichotomy is an elementary two-point specialization. Exact wording in the MCMC literature is therefore unnecessary under the audit's implication standard.

### Equivalent formulations

The audited canonical two-point measures are the low-order principal representations of this classical moment problem.

### Broader coverage

Broader classical coverage dominates the extremal step; finite-state realizations merely show attainability within the chain class.

### Exact database or table

A database/table comparison is inapplicable because prior coverage is theorem-level.

### Claim versus prior implication

Once the first two moments are fixed, evaluating the canonical extremal measures mechanically yields the advertised formulas; the unbounded upper tail follows by moving one feasible atom toward one.

**Checked sources.** https://doi.org/10.1214/23-AOS2335; https://doi.org/10.1090/mmono/050; Resultary semantic search

**Residual risks.** No exact MCMC paper printing every displayed formula was located, but implication-level classical coverage is already decisive.

## Value — FAIL

The chain-specific formulas are useful diagnostics, but after the published moment representation is combined with standard two-moment extremal theory they are routine substitutions and elementary two-point algebra. Under the shared value bar, correctness, sharpness, and reproducibility do not turn that mechanically implied specialization into a separate mathematical gap.

**Checked sources.** Berg--Song 2023; classical Hausdorff/Markov--Krein theory

**Residual risks.** The formulas can still be valuable pedagogically and computationally.

## Limitations

- The Markov operator must have nonnegative spectrum for the observable.
- The statements concern one fixed observable and exact population autocorrelations.
- The long-run upper-bound failure does not remove finite-horizon bounds.

## Disposition

FAILED. Acceptance requires PASS on correctness, originality, and value.
