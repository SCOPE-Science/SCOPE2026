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

# Reproducibility and verification

In the package directory run `OPENBLAS_NUM_THREADS=1 python verify_friendship.py`. NumPy, SciPy and SymPy are required. The script builds the friendship graph, generates the complete eighteen-coordinate Hermitian orbit basis, derives the exact symbolic generator from the structurally affine family, and solves the integrated master equation rationally.

It checks nonnegative coefficients of the exact denominator and numerator in nonnegative variables \(g\) and \(m-2\), independently checks two global coercive inequalities by exact nonnegative coefficients, verifies the limiting rational profile and its derivative, and compares the orbit solution against the uncompressed complex Liouvillian for fifteen finite cases. The checker has passed its self-contained assertions in the supplied environment.

The mathematical reason the size interpolation is exact is that every Hamiltonian commutator coordinate changes one row or column index and hence counts other triangles only linearly; all local dissipators have size-independent coefficients. This argument, not a finite fit, justifies extension to arbitrary integers \(m\ge3\). In particular the full-size numerical checks are consistency tests, not substitutes for the all-size symbolic identity.

The proof's exact boundary conventions are: rate \(g\) for decay of off-diagonal density matrix entries from local dephasing, rate two for physical loss of trap-site population, and uniform hopping amplitude one. The coherent limit \(g=0\) is excluded from finite-capture-time claims. No third-party paper text is bundled.
