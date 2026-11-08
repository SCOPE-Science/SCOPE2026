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

# Reproducibility and verification

Use a Python 3 interpreter (standard library only) and run `python3 verify_orbits.py` in the same directory. The checker constructs every codeword in seven small extension-field realizations and groups words into actual constacyclic orbits. It also checks, for each divisor of the action order, the complete Hamming-weight distribution of the fixed words and compares it with the theorem's closed polynomials. No external solver, web data, or certificate service is required.

Tested pairs are \((q,r)=(2,2),(2,3),(2,4),(3,2),(3,3),(4,2),(5,2)\). The largest exhaustive test contains 59,049 words. The formula is universal because of the proof in RESULT.md, not because any finite set of tests is exhaustive over all parameters. In particular, polynomial identities are not numerically tested for arbitrary prime powers or redundancy.

The sources [1]–[4] in RESULT.md provide literature context. Counts of total orbits alone, including previously established general formulas, are not represented as novel. Self-review is recorded in REVIEW.md; independent audit has not been performed.
