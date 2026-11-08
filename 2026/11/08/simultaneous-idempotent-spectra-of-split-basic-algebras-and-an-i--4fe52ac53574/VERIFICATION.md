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

The standalone `checker.py` computes full algebra products and idempotents independently of the closed-form orbit formula, filters commuting ordered tuples, and calculates left/right regular ranks from original multiplication matrices. Its recorded run in `checker_output.txt` tests ten finite-field configurations: three-vertex line, radical-square-zero triangle, fork and opposite fork over the prime fields of sizes two and three, for tuple lengths one through three where indicated. The direct rank-frequency dictionaries exactly equal independently assembled color-weight formulas in all cases.

`checker.py` additionally checks that the path algebra and its radical-square-zero multiplication variant have identical refined spectra, and that opposite forks have equal total counts but different refined spectra. An exact symbolic proof appears in `RESULT.md`; finite experiments do not establish arbitrary-field, arbitrary-dimension, scheme-smoothness or historical-priority assertions. No independent audit has been performed.
