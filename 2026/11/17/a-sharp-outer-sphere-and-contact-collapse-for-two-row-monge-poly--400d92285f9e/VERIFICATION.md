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

# Reproducibility and boundaries

Run `python VERIFY.py` using Python 3.9 or newer. The program uses only `fractions` and `itertools` from the standard library. It reconstructs every candidate vertex as a rational matrix and checks the center's barycentric contact certificate, all exact distance and strict-clearance formulas, and every sphere contact for \(q=2,3,\ldots,32\). It separately enumerates intersections of defining nonnegativity/Monge hyperplanes together with the sum-one hyperplane for \(q=2,3,4\), confirming that no additional vertices occur in those dimensions. Output: `PASS` and `6286` exact checks.

The finite computations do not establish the infinite result by enumeration. The written proof's cone-generation argument establishes the complete vertices for general \(q\); the computed rational gap identities are proved algebraically for all \(q\); the weighted identity proves the optimality statement without numerical optimization. No external or independent validation was conducted.
