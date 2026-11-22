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

# Reproduction and mathematical boundaries

The derivation concerns the exactly stationary, deterministic-between-tumbles active-particle process defined in `RESULT.md`. All positive-real-parameter conclusions follow from its bounded stationary generator identities and explicit rational factorization. The finite tests are independent checks only; they cannot establish continuous quantifiers or publication priority.

Run `python3 checker.py` in the directory containing this note. It needs Python 3 and no third-party packages. The actual package checker reported `PASS: 319 exact-rational and analytic-kernel checks plus 1 seeded path check`. The seeded exact-clock 40,000-path run compared the normalized lag-\(0.7\) covariance \(0.489660005\) with the prediction \(0.494878035\); it passed its predeclared absolute tolerance of \(0.05\). It solves conditional stationary moments for a family of independent four-direction/antipodal heading redraw distributions and positive rational rates; checks polynomial moment invariants, the positive-rate twin transformation, the exact variance difference sign, temporal kernel equality, and the resonance limit. It also checks the illustrative exact variances \(1/18\) and \(1/63\).

The analytic audit verified: the centered, constant-speed hypotheses in every generator equation; the positive variance denominator; the resonant case \(\gamma=\mu\); the positivity boundary \(\gamma=3\mu\), which does **not** admit a second positive redraw rate; and the geometric trace constraint \(1/d\le\operatorname{tr}\Sigma^2\le1\). The inverse map presumes fixed calibrated speed and direction law, and observations in physical time units. Independent external review is not yet performed.
