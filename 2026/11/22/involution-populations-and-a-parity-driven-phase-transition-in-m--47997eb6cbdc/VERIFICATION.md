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

# Verification and scope

Run the standalone file as \(\texttt{python verify.py}\) with Python 3 standard library. The file \(\texttt{verify-output.txt}\) is the exact console output obtained from that program. Tests exercise real finite-field substitution composition, coefficient equations independent of class-size formulas, invariant-monomial coefficient counts, and conjugation identities. Boundary regression cases are not part of the claimed new domain. Recorded tests pass, but no finite collection of computations proves the quantified theorem; the unrestricted argument is in RESULT.md.

No external independent audit or certification has been performed. In particular, published literature priority beyond the compared primary results is not fully settled.
