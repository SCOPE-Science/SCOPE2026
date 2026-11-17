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

# Reproducibility and verification scope

Execute `python verify.py` in an environment with Python and SymPy installed. The checker constructs all Catalan triangulations of each convex polygon with between one and six triangles. It computes oriented triangle-to-edge boundary matrices (not merely abstract dual trees), verifies the exact Gram identity and positivity, computes inverse matrices over the rationals, and checks all sign normals against the constant signs. There are 196 distinct instances in total, 84 with nonpath dual trees, and 10,064 facet-sign comparisons.

It also checks the tridiagonal closed form for eleven positive integers and both nonisomorphic four-triangle examples. The proof's use of the external all-walk extremal theorem is an analytical citation, not a claim that finite tests establish its all-size validity. No independent audit or computational proof of infinite cases is asserted.
