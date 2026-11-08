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
Run `python3 verify.py` and `python3 verify_orbits.py` with a standard Python 3 interpreter. Neither program needs external packages.

`verify.py` builds finite-field product multiplication tables, enumerates every nonzero rank-one linear map (with a normalized image vector), directly checks the original associative Nijenhuis identity on all pairs of standard basis vectors, and compares the **full sets** of valid maps with the stated character/idempotent normal forms. It checks fields of orders two and three, split products of up to three factors, pure quadratic extensions, and mixed split/quadratic products. The output ends with `VERIFY_OK`.

`verify_orbits.py` constructs the complete canonical family for selected products, computes the actual orbits of permutations of equal-degree field factors, and checks the orbit-count formula for multiple degrees, multiplicities, and field sizes. Internal Galois automorphisms act trivially on the classified maps because rational projections and primitive factor idempotents are fixed; the proof explains why this suffices. The output ends with `VERIFY_OK`.

**Scientific limits.** These are finite enumerations and do not certify the universal theorem independently. The full proof of arbitrary field size and arbitrary extension degrees is in `RESULT.md`. No independent mathematical audit has been performed.
