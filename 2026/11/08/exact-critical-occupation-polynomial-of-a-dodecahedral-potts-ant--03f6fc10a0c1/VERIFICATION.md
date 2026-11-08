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

# Computational and analytical verification

Execute `python3 verify.py` with Python 3 and its standard library; no graph packages, networks, or external input files are required. The verifier explicitly constructs the 20-vertex, 30-edge generalized Petersen graph \(GP(10,2)\), checks a two-color assignment having six monochromatic bonds, and performs two independent integer calculations of the 7-coefficient critical occupation vector.

The first calculation propagates partial exact integer coefficient dictionaries along all 81 diagonal states of the cyclic two-column transfer; only monomials with total exponent at most six can contribute to the requested coefficient. The second enumerates all vertex assignments via depth-first recursion, pruning a branch only when its **nondecreasing** accumulated count \(b+k\) already exceeds six. Every completed and admissible assignment is counted exactly once. Equality of the two calculations, plus the independent proper-coloring transfer and exact rational moment identities, is asserted in the executable itself.

Expected terminal summary: `VERIFIED: critical polynomial coefficients [250, 3000, 13800, 30400, 32760, 15840, 2720]`, proper three-coloring total `7200`, critical degeneracy `98770`, and exact mean and variance `34836/9877` and `119729580/97555129`. A failing check raises an exception. The proof's parameter-uniform low-temperature limit is an analytic finite-sum estimate; numerical testing is not used to infer it.

This is same-model computational and proof review only. No independent scientific audit or validation is represented.
