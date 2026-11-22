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

The proof uses the known balanced-Bier convex realization, an explicit orthogonal Fourier decomposition, the orbit-space fundamental-group theorem, and the three-dimensional Poincaré theorem. The finite five-label calculation is reproducible by running `python check_bier_lens.py` with Python 3 and SymPy.

The executable enumerates the full five-label deleted join with face counts \((10,40,60,30)\); divides by the full free tenfold action to obtain the cellular counts \((1,4,6,3)\); verifies both consecutive integral boundary compositions vanish; and calculates the Smith diagonal \((1,1,1,10)\) for the second boundary. It also constructs the actual restricted integer matrices for the signed cycle and two dihedral reflections, checks all ten powers of the signed cycle, checks determinant one, fixed-plane dimensions two, and the dihedral relations.

The computation checks the concrete three-dimensional example, not all primes. The general freeness criterion, weighted-lens conjugacy, and the underlying topological three-sphere conclusion rely on the written argument and cited standard theorems, not on a finite experiment. Independent validation has not been performed.
