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

# Reproducibility and limits

Run `python check_wheel_cut.py` from the folder containing this document and the standalone Python script. Standard-library Python 3 is sufficient. The recorded execution in `check_wheel_cut_output.txt` reports `WHEEL_CUT_FINITE_CHECK_PASS` for eight cases, rim sizes 5 through 12.

For each case the checker constructs the actual graph and the induced graph on each three-set, derives the maximal cut faces, verifies the predicted decomposition into two subcomplexes, checks the exact intersection and the two distinct free-face pairs, and computes reduced mod-two homology by sparse Gaussian elimination. It separately checks intact-wheel and single-rim-edge deletion acyclicity over the same field.

These calculations are finite sanity checks only. In particular, mod-two ranks do not prove torsion-freeness or an infinite-family homotopy statement. The unrestricted integral homotopy theorem rests on the explicit two-free-face collapse, the relative cellular exact sequence, connectivity and homotopy-pushout proof in `RESULT.md`. No independent mathematical audit has been performed.
