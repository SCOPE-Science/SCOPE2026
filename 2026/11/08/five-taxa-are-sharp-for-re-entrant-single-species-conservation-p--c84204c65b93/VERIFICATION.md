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

Run `python verify.py` with Python 3.9 or later; only the Python standard library is needed. It constructs rooted binary tree classes with respectively \(1,1,3,15,105\) labeled shapes for one through five tips, checks all 100 small-tree tip comparisons for the structural condition used in the proof, and evaluates the witness against independently enumerated survivor subsets with rational arithmetic at nine distinct rational probability parameters (45 gain comparisons and nine cross-point/ordering comparisons).

The analytic proof in `RESULT.md` is valid for every real \(p\in(0,1)\), every positive edge length, and all rooted full-binary trees up to five tips. The finite checks test its implementation and witness, not the universal quantifiers. The formula for expected-PD gain is derived directly by edge-indicator expectations. No external certification or independent expert validation is claimed.
