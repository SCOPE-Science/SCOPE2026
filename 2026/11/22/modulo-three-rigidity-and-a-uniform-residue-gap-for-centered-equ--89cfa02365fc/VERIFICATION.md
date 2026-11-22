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

# Verification of the centered-cube triangle result

Execute `python verify.py` with Python 3 and SymPy installed. The checker uses symbolic simplification to confirm the vertex-rounding algebra and all three modular threshold equalities, checks the exact two-, three-, and four-coordinate matrices, and stacks them in 10 dimensions of residue class one, 11 of residue class two, and 10 of residue class zero. It also verifies the rounding inequalities on 30,000 independently sampled rational coordinate triples using exact `Fraction` arithmetic. Its completed execution reported `PASS`.

The analytic proof in RESULT.md, specifically the convexity argument on the centered-coordinate hexagon, the convex endpoint proof of the rounding inequality, and the integer-triple minimum-absolute-deviation argument, establishes the result for every admissible dimension and every centered equilateral triangle. Finite computational tests are consistency checks, not a proof of a universal quantifier. The upper deficit bounds are witnessed constructions, not certified optima in dimensions not divisible by three. No external or independent mathematical audit has occurred.
