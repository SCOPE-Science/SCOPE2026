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

The standalone `verify.py` constructs the exact set of one-duplication descendants directly for every source avoiding `11` at lengths 2 through 18. It separately derives polynomials from the three-term recurrence and checks the entire histogram, the derivative output-count identity, and all symbolic extreme-count formulas through length 60. Local invocation completed with `VERIFY_OK enumerated_sources=17706 exhaustive_lengths=2..18 recurrence_lengths=2..60`.

The all-length conclusions rest on the invertible two-step derivative representation, the three-state transfer matrix, and a residue-class leading-degree induction. The computer checks do not establish claims for lengths above those tested. No separate external verification or independent audit has been performed.
