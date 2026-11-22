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

# Reproducible verification

Run `python3 verify.py` in a directory containing the standalone script. It requires only Python 3 standard library. The script constructs the precise 16-by-16 transfer, computes its integer characteristic polynomial using Faddeev–LeVerrier/Newton identities, and checks exact trace values at cycle lengths 3–12. It independently enumerates every two-layer spin state for four cubic networks (including prisms of length 3 and 4), checking the microscopic update inequalities against the classification at coupling magnitude 2.

Expected ending: `16x16 transfer polynomial verified exactly; counts n=3..12 verified; PASS`.

The polynomial computation is an exact finite symbolic certificate whose source matrix is generated within the script. The universal regular-graph absorption statement is proved analytically and not inferred from a finite census. Numerical approximations to the largest quartic root are explanatory, not proof. The evaluation concerns absorbing microstates only; historical priority and independent mathematical validation remain open.
