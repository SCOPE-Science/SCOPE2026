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

# Reproducibility and verification

Run `python3 verify.py` with `periodicity_certificate.tsv` in the same directory. No external modules are required.

The program constructs and checks all 72 quotient-state entries for \(F_3\) and \(F_5\). Because the size-independent transfer equation holds for every \(w\ge2\), this finite equality is the inductive certificate for the unbounded parity law. The program separately computes the full vertex-labelled game tree for each \(3\le n\le10\), checks both the exceptional boundary and every stated base case, and checks further root values through order 102. All tests are exact integer/set operations. A successful replay ends with `VERIFY_OK`.

The independent vertex-labelled computation is an independently written *algorithmic cross-check within this package*, not an independent mathematical audit. The theorem is not established by finite-order testing alone; it relies on the exact transfer map and the 72-state finite identity. The result does not cover other graph families, nor different optimality or force-preservation conventions.
