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

# Verification of a weighted nodal entropy-limiter classification

The analytic proof in `RESULT.md` uses strict convexity, the normal-cone characterization of nearest points of smooth convex sublevel sets, connectivity of weighted spheres in mean-zero dimension at least two, and a nonvanishing weighted cubic moment. Its quantifiers and the two-node exceptional case are addressed there; no finite test replaces that argument.

Run `python verify.py` using only the Python standard library. The test verifies the full three-node Simpson example with exact `Fraction` arithmetic: quadrature normalization; conservation of mean; the exact radial scaling factor; the equality of radial entropy and the budget; strict entropy feasibility of the comparator; the exact squared correction norms and their rational difference; positivity of all three states; and an explicit nonzero weighted cubic moment. The output is reproducible without downloads.

The numerical example demonstrates nonoptimality for one strictly convex nonquadratic entropy. It does not assert a sharp bound on the correction inefficiency or extend to arbitrary non-scalar entropy constraints. Historical-priority comparison is not a proof of novelty; independent mathematical validation has not been performed.
