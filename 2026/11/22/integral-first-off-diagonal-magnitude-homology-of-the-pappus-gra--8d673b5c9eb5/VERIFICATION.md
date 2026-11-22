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

# Verification of the integral calculation

Run `python3 pappus_exact.py` in an environment with SymPy. The code enumerates all 324 endpoint pairs and computes the exact integral Smith normal forms of the signed boundaries in degrees three and four. It verifies their composition is zero, checks that all nonzero elementary divisors are one, and counts precisely 108 endpoint groups of free rank two and 36 of free rank one, all other groups vanishing. The terminal replay appears in `pappus_exact_output.txt`.

The result is specific to the Pappus graph and bidegree (3,4). The output is not an external certification or independent mathematical audit. The complete integer proof is finite enumeration of explicitly specified matrices; no inference from a sample to a larger graph class is made.
