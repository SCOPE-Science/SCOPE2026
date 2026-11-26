---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

The closed-neighborhood identity, explicit masks, and block-composition argument in `RESULT.md` prove the uniform construction. The lower bound uses the constraints imposed by empty rows and columns. No finite alphabet cutoff is used to deduce the uniform conclusion.

The Python 3 programs `check_bounds.py` and `check_adjacency.py` use only the standard library. They check the construction for alphabets 3 through 100 by the signature and explicit adjacency formulations, respectively. The first also produces the masks and tests the 84, 1820 and 53130 size-q candidates at q = 3, 4 and 5. Those finite exclusions reproduce the minima in Horan–Adachi–Bak (arXiv:1504.08011v2, Figures 8–9) and are not separate results here.
