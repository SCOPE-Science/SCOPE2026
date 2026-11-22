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

# Verification notes

- Source: `verify.py`, executable with standard Python 3.9 or newer and no downloaded packages.
- The rooted-tree generator produces nondecreasing multisets of child rooted trees of all total sizes; by induction it enumerates each unlabelled rooted tree exactly once.
- The script computes ideal-rank polynomials using the root recursion independently of full one-point diagram generation.
- The separate direct generator checks every subset pair as a possible ideal/filter one-point extension and verifies all admissibility conditions, without using the recursive rank polynomial for that test.
- Replayed output is preserved in `verification_output.txt`; all 85 rooted shapes through seven vertices and all depth coefficients passed.
- Exhaustiveness of the sharp cutoff rests on the complete generator and comparisons through seven, and *not* on any extrapolation to larger trees.
- The all-finite-tree leaf-depth formula is proved in `RESULT.md` by a direct singleton-filter/ancestor-prefix bijection.
- Historical originality has residual risks; neither these computations nor the mathematical review are independent certification.
