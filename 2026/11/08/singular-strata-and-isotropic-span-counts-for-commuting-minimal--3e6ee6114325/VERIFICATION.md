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

# Direct verification

`checks/finite_counts.py` constructs all rank-at-most-one operators as matrices over specified prime fields and compares all pairwise actual matrix products and commutators. For the tested tuple lengths it exhausts all commuting tuples and groups them by the span rank of their images, then compares counts with exact isotropic-Grassmann formulas. `checks/finite_counts.txt` is the recorded stdout.

`checks/tangent_rank.py` builds generators for tangent spaces of each rank-one symplectic cone, directly linearizes matrix commutators, performs finite-field Gaussian elimination, and compares actual tangent dimension with the stated closed formula for several zero/nonzero support cases in dimensions four and six. `checks/tangent_rank.txt` is its recorded stdout.

Reproduce with `python3 checks/finite_counts.py` and `python3 checks/tangent_rank.py`. The programs require only Python's standard library. They do not test arbitrary extension fields or prove any infinite family; the proof establishes the general theorem. The reduced-variety tangent argument and the known literature on symplectic vector nullcones are needed for the global geometric conclusion.
