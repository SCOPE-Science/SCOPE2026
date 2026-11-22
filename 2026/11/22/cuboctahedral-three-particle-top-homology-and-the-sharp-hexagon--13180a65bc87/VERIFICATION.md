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

# Reproducibility and exact-computation limits

The supplied `verify_cuboctahedral.py` uses the Python standard library only, reconstructing the twelve-vertex line graph of the three-cube from its eight binary-labeled vertices. Run `python3 verify_cuboctahedral.py`; its deterministic output is the JSON object in `checker_results.json`.

The verifier constructs every weight-three degree-three reduced Świątkowski basis element, and all nonzero rows of the signed boundary to degree two. Integer column elimination produces 5916 coefficient-one or coefficient-minus-one pivots, leaving 24 exact integral kernel coordinates. Independently, it enumerates all simple cycles, all vertex-disjoint cycle triples, and their oriented product chains, checking each boundary is zero. An exact 24-by-24 determinant of -1 proves integral torus generation. Rational rank 20 of the 44 short-cycle torus columns and a 20-by-20 unit minor prove the sharp, primitive short-torus obstruction.

The weight-three model has no degree-four chains; the top kernel is therefore top homology. The result depends on the established theorem identifying the homology of the reduced Świątkowski model with unordered graph configuration-space homology. No assertion about lower-degree homology, homotopy type, unseen literature or independent external validation is made.
