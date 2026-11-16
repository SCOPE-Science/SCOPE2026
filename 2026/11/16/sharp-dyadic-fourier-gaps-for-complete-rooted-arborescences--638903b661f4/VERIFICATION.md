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

## Reproducible exact checks

`python3 verify_finite.py` uses Prüfer-word tree generation and integer determinant calculations to compare every reduced frequency at vertex orders three through five, 83 signed frequencies at order six, and both all-order extremizing sign constructions through order eighteen. It also verifies the even-order vanishing root-star signs at every even order from four through eighteen.

`g++ -O3 -std=c++17 verify_reduced_n6.cpp -o verify_n6 && ./verify_n6 6` evaluates all 1,048,576 reduced frequencies at vertex order six with integer-only subset-determinant arithmetic. The expected zero count is 514,800 and the smallest positive magnitude is 16. This reduced enumeration is exhaustive for its specified finite case because multiplying all signs in a nonroot row only changes the coefficient's sign.

## Boundaries of verification

Neither finite computation is an infinite-dimensional certification. The symbolic divisibility, two extremizer constructions, and singularity witnesses are established in `RESULT.md`; the programs are independent reproducibility checks of specific finite cases. No external independent mathematical audit has been performed.
