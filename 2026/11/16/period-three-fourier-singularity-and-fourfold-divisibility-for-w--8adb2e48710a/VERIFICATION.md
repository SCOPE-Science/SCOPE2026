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

The standalone `verify_wheel.py` script (Python standard library only) enumerates every spanning tree and every Walsh frequency for \(3\le n\le9\), verifies the Lucas-number counts, the predicted zero-free residue classes, the congruence modulo four when \(3\mid n\), and oddness otherwise. It checks several frequencies against exact integer determinants of their signed reduced Laplacians.

The script also enumerates all explicitly constructed singular sign assignments for rim lengths \(3,6,9,12\), checking the stated integral nullvector row by row and the distinct-signing counts. For the first three lengths it separately verifies the determinant vanishes.

`checks.txt` records the output of an actual run of this package script. The experiments are finite; the proof in `RESULT.md` establishes the all-dimensional assertions. Independent audit has not been performed.
