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

# Reproducibility and scope of checks

`verify.py` uses only the Python 3 standard library. It checks the determinant area identity on 400 independent-angle draws; a 300,000-sample direct three-direction Monte Carlo comparison at seven fixed thresholds; the exact mean; and the endpoint and interior cusp coefficient trends. The mean is \(6/\pi\). The numerical checks passed in the actual package preparation environment and are not infinite proofs. The mathematical arguments in `RESULT.md`, including the local three-boundary threshold derivation, are the proof.

Unproved limits: independent priority certification, extensions to unequal segment lengths, and a closed elementary expression for the one-dimensional quadrature.
