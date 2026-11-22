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

# Reproducibility

Run `python3 checker.py` using Python 3 without additional packages. Expected successful output is recorded verbatim in `CHECKS.txt`.

The checker constructs \(\mathbb F_2\) and \(\mathbb F_4\) arithmetic, all invertible linear maps in dimensions one and two, and all invertible three-dimensional maps over \(\mathbb F_2\). It calculates the actual nullity of the quadratic involution equation for each map, compares Jordan-rank strata and total counts with the closed formulas, and independently composes all \(384\) degree-two substitutions on two generators over \(\mathbb F_2\) to obtain exactly \(88\) involutions. Further seeded conjugate matrices test each Jordan class through six generators. The finite checks cannot certify all dimensions, all field extensions, or historical novelty; those are handled by the symbolic proof and stated literature comparisons.
