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

# Verification

Run `python verify.py` with Python 3 and SymPy in the same directory as the result. The exact checker tests independent enumeration of nine draw pairs, normalization, Rayleigh differences, factored discriminants, eight rational parameter samples, the strict negative-covariance identities and cardinality distribution, the algebraic transition equality, and the rational failure witness. The checked execution returned `PASS: 50 symbolic/rational independent checks`.

The all-real multiaffine Rayleigh criterion and exact sign calculation prove the claim for every positive real parameter. Finite rational tests are only diagnostic. There is no formal-machine or third-party independent verification; an independent audit has not been performed.
