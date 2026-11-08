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
# Reproducibility and mathematical limits

Run \(\texttt{python3 checks/verify_boundary.py}\) with Python 3 and its standard library from the package root. The checker uses rational arithmetic and checks the exact branch congruence, both critical couplings, both signs, and pointwise radius invariance for finite examples, including discontinuity boundaries. It also enumerates finite exact residue grids; the continuous uniform-radius law is established analytically from uniform modular fractional parts. The code does not prove the result for all slopes or points. The arbitrary-parameter statement follows from the one-step modular integer identity in the proof, while the invariant-measure statements follow from ergodicity and measure restriction. Independent validation has not been performed.
