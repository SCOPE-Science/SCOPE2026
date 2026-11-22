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

# Verification evidence

The package contains `verify_triple.py`, a standalone Python 3 script requiring no external dependencies. Run `python3 verify_triple.py` from the directory containing the scientific files. It constructs the predicted integer histograms from the stated trivariate cylinder mass formulas, and separately enumerates both polynomial arguments and exact prime-power valuations for 400 parameter-and-depth cases, totaling 1,396,368 index triples. Every cell and each histogram's mass passed.

The proof of unrestricted prime, coefficient, lag scale and prime-power depth is in `RESULT.md`, using Hensel roots, the three distinct child balls at the collision depth and exact rational moment identities. The finite checker is independent corroboration, not an infinite certificate. Self-review is passed; independent audit is not performed.
