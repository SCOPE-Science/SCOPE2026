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

# Reproducibility

Run `python3 verify.py` with Python 3.8 or newer. There are no third-party dependencies. The exact captured output is in `verification_output.txt`. The verifier independently forms finite-field involution matrices, solves the tensor-square linear constraints by Gaussian elimination, and compares the resulting counts with the closed formulas. For the small exhaustive cases, it squares actual full algebra automorphism matrices for every possible lift. In characteristic two with two generators it explicitly enumerates all identity-linear shear-conjugation orbits.

The tested fields are prime fields of orders 2, 3 and 5. The source proof applies unchanged to arbitrary finite extension fields because it uses only the module decomposition of involutions in the relevant characteristic. The finite tests are corroborating evidence, not a proof in all ranks and fields. No independent audit or external certification was performed.
