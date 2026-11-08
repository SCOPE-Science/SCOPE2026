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

# Verification details

The exact border equation is obtained by composing the specified affine branches starting at the switching coordinate, not by fitting numerical data. The two leading tent-root constants are 5/2 and 9/4. The relevant derivative difference of the analytic creation curves converges to 1; hence the crossing constant is 1/4. Run `python verify_lozi.py` for an exact finite symbolic recurrence comparison and supplementary numerical crossing checks. The script does not prove an unbounded-parameter asymptotic; the analytical proof supplies that. Source admissibility and C1 convergence are imported explicitly from Ou (2022), Theorem 6.6 and Corollaries 5.11, 5.22, 6.7. This is self-review, not independent audit.
