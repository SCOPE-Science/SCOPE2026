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

# Verification

The included `check_exterior_hom.py` independently multiplies the eight exterior-algebra basis monomials, computing both signs and disjoint-support products. It directly tests the defining square-zero and anticommutation identities on images of free generators. It does not invoke the alternating form criterion in its accept/reject routine. The exact console output is included in `check_output.txt`.

Run `python check_exterior_hom.py` using Python 3 (standard library only). Exhausted cases: two-generator and one-generator input over the prime fields of sizes three and five, and the two-generator input over the field of size two. Additionally the checker exhausts all quadratic coefficients above the four canonical rank representatives for three input generators over the field of size three. These finite computations verify the stated examples and fiber dimensions, not the theorem for arbitrary fields or generator count.

The general correctness argument is given in `RESULT.md` and does not depend on computational extrapolation. Historic novelty remains subject to independent review. No independent audit was performed.
