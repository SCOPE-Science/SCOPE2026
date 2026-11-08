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

The standalone `check.py` was run using Python 3 with SymPy. Output: `CHECK_OK: 6 rational parameter witnesses; 54 exact conjugacy tests; tent fixed-point proof corroborated through n=10; primitive periods through n=9`.

The checker symbolically expands the full scalar conjugacy relation and substitutes the defining parameter locus, checks the algebraic simplification, and checks six distinct nondegenerate rational parameter examples. It additionally verifies every branch-fixed-point identity for tent iterates through period 10 and primitive-period classification through period 9 using exact fractions. These finite checks corroborate the algebra and indexing. They do not replace the all-parameter/all-period analytic argument in `RESULT.md`. The only noncomputational ingredients are classical full-tent exactness and the Borel–Cantelli endpoint distortion estimate, both spelled out in the proof. No independent audit has been undertaken.
