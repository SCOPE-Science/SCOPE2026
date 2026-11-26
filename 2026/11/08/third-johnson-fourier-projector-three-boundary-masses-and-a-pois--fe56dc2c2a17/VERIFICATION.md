---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The limit and the derivative jump follow from the overlap factorial moments, the exact kernel second moment and the Poisson series argument in `RESULT.md`. The existing `verify_johnson3.py` numerically compares the local second difference at \(\sqrt3\) to \(6e^{-3}\) and compares a large-mean Poisson–Charlier expectation with the limiting Gaussian constant. Its exact rational kernel checks also corroborate the finite normalization used in the proof. The finite boundary-summation tests in that script concern a classical Hahn-polynomial identity, not a claim of novelty. Neither the finite tests nor the floating-point checks establish either asymptotic limit or differentiability properties.
