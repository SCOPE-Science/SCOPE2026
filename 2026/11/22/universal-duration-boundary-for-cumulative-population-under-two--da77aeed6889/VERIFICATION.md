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

# Verification of the two-stage logistic comparison

Run `python3 verify.py` with a standard Python 3 installation. The exact rational witness with \(r=1\) and growth exponent \(E=3\), capacities \(2\) and \(1\), and inverse initial abundance \(y=7\) yields the common cumulative biomass \(\log(16/7)\). The program independently computes stage integrals, direct numerical quadratures, all-time inverse-state differences, final-state dominance, the negative/positive temporal contribution ratio and the exact polynomial limiting-integral identity. The replay completed **144,156 deterministic assertions** without a failure.

The analytical argument in RESULT.md covers all \(r,\tau,N_0,K_H,K_L\) satisfying its strict hypotheses; the finite checks are not a proof of any universal statement. Reported numeric tolerances are explicit in the script. External independent validation has not been performed. Historical priority against general temporal ordering/rearrangement theorems is unresolved.
