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

Run `python verify.py` with Python 3 (no external packages). The self-contained script checks the two exact rational covariance expressions against every labeled tree on three through five vertices and all independent uniform ball allocations with one through four balls. It also checks the exact two-ball formula, integer sign profiles for tree orders through twenty-three, and noncritical load-limit diagnostics. The successful output is `PASS 1738 exact rational, enumeration and asymptotic assertions`.

The proof for all orders and continuously varying crossing locations uses the exact vacancy-event identities, forest Euler identity, generalized Descartes sign-variation rule, and uniform Taylor expansions; it does not follow from finite enumeration. No independent audit has been performed.
