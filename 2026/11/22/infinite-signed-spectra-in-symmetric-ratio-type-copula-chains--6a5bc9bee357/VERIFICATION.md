---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Mathematical verification notes

The analytic proof is in `RESULT.md`. Its critical checks are the covariance integration-by-parts formula, the \(\theta>0\) summable rank-one expansion, the Cauchy determinant formula for negative parameters, the alternating \(LDL^\mathsf{T}\) pivot signs, and bump-function transfer to a compact self-adjoint Markov operator. The finite calculations do not substitute for those infinite-dimensional arguments.

Run `python3 CHECKER.py` with Python 3 and its standard library. The script verifies exact rational determinants and inertia-sign pivots for every dimension from one through six, tests strictly positive Gram matrices for positive parameters through dimension six, and evaluates an independent two-node sign witness at \(\theta=-1\) for \(f(u)=(1-u)e^{-u}\). Its last line should read `ALL EXACT CHECKS PASSED. The analytic proof covers every matrix size.`

The 2024 exponential ratio copula's source parameters are \(-e^2\le\theta\le1\), but the spectral theorem deliberately excludes the positive endpoint where \(1-\theta f(0)^2=0\). No exact spectral gaps, eigenfunction formulas, or independent mathematical validation are asserted.
