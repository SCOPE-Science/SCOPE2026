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

# Exact reproducibility

Use Python 3.9 or newer, standard library only: `python3 verify_triangle.py`. It prints `PASS 34286 exact integer tests, exhaustive set-partition transforms n=3..9 and algebraic recurrence checks through n=180` on successful execution.

The checker independently generates every restricted-growth-word partition through nine labels, for each of two distinct triangular unicyclic graph attachments; computes their profile multiplicities, then applies an integer Walsh butterfly and checks every character against the analytic formula. It also checks the exceptional negative indices and sharp gaps, the Bell-moment differences, triangle-sector recurrence and boundary separation through 180 vertices, and a finite collection of instances of the strict domination bound.

These finite computations corroborate rather than prove the quantified infinite theorem. The infinite part of the proof is supplied in `RESULT.md` by Poisson size-bias, the two exact recurrences, a base row and a normalized monotone term domination inequality. No independent mathematical audit was performed.
