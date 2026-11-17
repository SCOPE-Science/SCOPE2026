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

# Reproducible checks and limits

Run `python3 verify.py` with Python 3 and the standard library. The program independently enumerates setwise-invariant Hom cells via first-coordinate support subsets for all target cycle types through ten colors, comparing directly with the predicted residue-class face poset for all source lengths from two to five (or the number of colors). This checks 531 parameter pairs and 1,987 nonempty invariant supports. It additionally computes reduced mod-two simplicial homology for nine joins of discrete sets, and tests mixed target cycle lengths of different divisibilities.

`verification.txt` stores the program's observed output. The checks validate the finite instances and the computational implementation. The universal result rests on the symbolic fixed-point equations, the orbit-divisibility argument, the PL gluing construction, and the shellability of joins; these steps do not depend on finite enumeration. An integral homology check for every parameter is unnecessary because the join model and homotopy splitting are proved generally. An independently performed mathematical audit has not occurred.
