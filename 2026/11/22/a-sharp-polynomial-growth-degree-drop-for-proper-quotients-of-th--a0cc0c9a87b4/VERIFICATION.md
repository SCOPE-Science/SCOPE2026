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

The included `verify.py` is self-contained and runs with a standard Python 3 interpreter. Execute `python verify.py` in the directory containing the file. The expected final line is `MONOGENIC_INVERSE_QUOTIENT_GROWTH_CHECKS_OK`.

The code enumerates complete Munn normal-form word balls through radius ten and verifies their geodesic lengths, the inverse identities, representative eventual-periodicity identities, and the bicyclic homomorphism and ball formula. It does not enumerate all inverse-monoid congruences or establish an infinite theorem by computation. The general bound is justified by the symbolic proof in `RESULT.md`; the checker tests its basic arithmetic and combinatorial primitives only.
