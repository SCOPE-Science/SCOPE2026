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

Run `python checker.py` with a Python 3 standard-library interpreter. The program checks 4,200 finite substitution-prefix block comparisons against the claimed exact digit test, as well as 100 small all-shift censuses. Both test groups passed during preparation.

The checker does not establish any infinite statement; those are proved in `RESULT.md` via the discrepancy identity and composition of digit-column maps. In particular, a successful finite sample alone cannot rule out delayed unequal blocks.

The result assumes positive run lengths and distinguishes complete classification of aligned periods from a restriction to powers of the substitution length for nonaligned shifts. Independent mathematical validation has not been performed.
