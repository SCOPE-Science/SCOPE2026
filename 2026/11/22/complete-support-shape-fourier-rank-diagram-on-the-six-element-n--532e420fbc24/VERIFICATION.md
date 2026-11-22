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

# Verification of the exact support-shape rank diagram

`python3 VERIFY.py` requires Python 3 and SymPy. The script constructs six-by-six regular convolution matrices for \(S_3\) with an independent group multiplication routine, and computes their exact ranks. It compares all 31 explicit canonical witnesses against the separate irreducible-block rank expression and the nine predicted shape spectra. It also checks the two rank formulas across every support of cardinality 1–4 and all coefficient assignments from \(\{1,-1,2\}\). The deterministic stdout is in `CHECK_OUTPUT.txt`.

The algebraic proof, not a finite experiment, establishes the exhaustive absence of any other ranks at arbitrary nonzero complex weights. The computations do not cover other group orders, stability under noise, or historical uniqueness. Independent mathematical audit has not been performed.
