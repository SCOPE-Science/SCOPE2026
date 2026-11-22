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

# Verification of the marine-reserve effort-cap law

The main proof is analytical: the exact two-eigenvalue representation establishes the survival function, strict effort monotonicity, and a uniform asymptotic expansion. The result does not rely on finite numerical enumeration or an unproved convergence assumption.

## Reproducible checks

Run `python3 verify.py` with Python 3.9+; it uses no third-party packages and does not connect to any network service. It independently reconstructs \(e^{AT}\) by a matrix Taylor series and compares that evaluation with the spectral formula for multiple ecological parameters, efforts, reserve fractions and season lengths. It then computes the reserve boundary via bisection and the unique finite effort threshold and checks convergence toward the proved inverse-gap coefficient for three parameter sets.

Observed run output starts with `PASS: 435 supplementary exact-formula, matrix-series, and asymptotic checks`; example \(c=m=1\), \(q=0.7\), \(T=0.5\), \(r=2\) returns \(R_c=0.876756832620\), coefficient \(0.261680835745\), and effort caps near the singular reserve boundary.

## Exact steps and limits

The checker's matrix-series implementation is separate from its closed-form spectral implementation, so the agreement tests independently exercise the matrix algebra. The proof derives the leading \(1/E\) coefficient uniformly for \(R\) in a neighborhood of \(R_c\) and obtains the cutoff limit with a moving root; numerical convergence alone does not establish that uniform step. The deterministic two-patch model, positive-parameter hypotheses and distinction between zero and positive population equilibria are part of the proof. No independent audit or physical-field validation is claimed.
