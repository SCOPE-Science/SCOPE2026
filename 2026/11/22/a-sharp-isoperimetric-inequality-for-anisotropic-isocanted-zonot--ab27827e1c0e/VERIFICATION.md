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

The proof's critical steps are the exact facet-volume identities, strict one-parameter minimization, normalized Newton inequalities, and rigidity of the equality case. The proof in `RESULT.md` handles every integer dimension at least two and arbitrary strictly positive generators.

Run `python check_zonotope.py` using Python 3, NumPy and SciPy. It constructs the full zonotope vertices independently, invokes SciPy/Qhull to compute volume and boundary area for 35 unequal-length configurations in dimensions two through six, and compares them with the asserted formulas. It also tests the dimensionless quotient and equality at the sharp optimizer in dimensions two through ten, with directed perturbations. The numerical tolerance is a verification convenience, not a proof of exact equality in higher dimensions.

No computer formalization, symbolic proof assistant, expert assessment, or independent external audit has been performed.
