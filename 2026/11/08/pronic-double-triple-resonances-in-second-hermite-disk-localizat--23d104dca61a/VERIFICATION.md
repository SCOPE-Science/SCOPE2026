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

# Verification of the adjacent-gap and pronic resonance theorem

Reproduce with `python checker.py`. Requires Python, SymPy and SciPy; the local check returned `SECOND_HERMITE_RESONANCE_CHECKS_PASS 1180`.

The checker exactly verifies the two-variable polynomial identity used to differentiate the adjacent gap and the exact polynomial divisibility governing the neighboring slope ratio. It compares independently integrated Laguerre-square densities with the closed adjacent-gap formula over 261 index/radius pairs, checks the two prescribed polynomial roots at 24 pronic areas plus surrounding integer indices, tests the two real root branches for 39 indices, and numerically checks triple-integral values at the first four pronic areas. The infinite quantifiers and uniqueness of the two-center parameters are proved symbolically and arithmetically in `RESULT.md`; finite computations are only corroboration.

Known limitations: the source radial eigenvalue formula is previously published; the claimed contribution is the exact all-area consecutive-index degeneracy and slope classification, not original derivation of general Landau radial diagonalization. The theorem neither rules out nonconsecutive accidental coincident values nor establishes sorted spectral-cutoff multiplicities. No independent mathematical audit has been performed.
