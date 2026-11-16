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

# Reproducibility checks

Run `python verify_two_arcs.py` with NumPy and SymPy available. The script reconstructs the Fourier Gram matrix from the stated arc integrals, verifies the exact determinant identity in symbolic arithmetic, compares each Gram entry with independent Gauss–Legendre integration at 246 admissible aperture–separation pairs, and checks the quantitative bound plus the asymptotic cusp coefficient at six aperture widths. Its expected terminal marker is `TWO_ARC_FOUR_MODE_PASS`. The perturbation argument and global inequality are proved in RESULT.md; a finite numerical sweep alone does not establish either universal statement. No independent audit was performed.
