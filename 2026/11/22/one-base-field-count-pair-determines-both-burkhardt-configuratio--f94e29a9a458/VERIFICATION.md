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

# Reproducible exact checks

Place `check.py` and `spectra.csv` in the same directory and execute `python3 check.py` with Python 3.9 or newer. The check uses only the Python standard library. It constructs all 40 projective points of the symplectic four-space over \(\mathbb F_3\), all 90 nondegenerate two-planes, all 45 unordered orthogonal decompositions, and checks the 360 point–decomposition incidences. Six transvections act faithfully on the 85 objects and preserve incidence. Full closure under their products produces exactly 25920 elements. Closure under generator conjugation partitions these into exactly 20 classes; the class sizes sum to 25920.

For every class, the program calculates the full cycles on 40 and 45 labels, reproduces the bundled 20-row CSV in order, and verifies that exactly 15 rational-count pairs correspond bijectively to exactly 15 complete pairs of zeta cycle spectra. Exactly five pairs of distinct classes collide. The final success output is `BURKHARDT_40_PLANES_45_NODES_25920_GROUP_20_CLASSES_15_JOINT_SPECTRA_VERIFIED`.

The classification of geometric nodes and planes and the bijection between forms and conjugacy classes rely on the cited algebraic geometry and finite-field descent results; the program tests and exhausts the discrete symplectic calculation, not a direct enumeration of quartic equations over each finite field. The full Hasse–Weil zeta function of the threefold is not computed, and the finding has not undergone independent mathematical audit.
