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

# Reproducible checks

Execute `python verify_franklin_four_cut.py` and `python verify_franklin_homology.py` with Python 3.9 or later; only the standard library is needed. The scripts are supplied as complete standalone files. The two exact terminal markers are `ALL_VERIFY_OK` and `ALL_HOMOLOGY_OK`.

The primary verification enumerates all 495 four-subsets, detects the 45 independent four-sets, generates all 2533 augmented simplices out of 4096 subsets, constructs 1245 matched pairs, and topologically sorts the full 12780-incidence directed Hasse graph. After removing the empty-face pair it independently topologically sorts 2532 nonempty faces. The only critical nonzero-dimensional faces are 43 four-simplices; there is one critical vertex. The proof's integral homotopy conclusion uses this acyclic matching, not numerical extrapolation.

An independent checker computes boundary ranks over three finite fields, recovering unreduced Betti vector `(1,0,0,0,43,0,0,0)`. The first checker also enumerates 48 graph automorphisms, their ten conjugacy classes, and the signed fixed-face Lefschetz trace on each. Their class-weighted trace sum is zero. Finite-field calculations alone would not establish torsion-freeness, and rational character values alone do not determine an integral representation lattice. The complete executable output is in `verification_output.txt`.

No independent audit or external validation is represented by these checks.
