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

# Verification record

The analytic proof in `RESULT.md` establishes the theorem for every two real positive-definite \(2\times2\) matrices with equal determinants; no finite experiment replaces the uniqueness or square-symmetry arguments. Essential identities independently reconstructed are the trace-zero property of \(C=M^{-1/2}(A-B)M^{-1/2}/2\), its eigenvalues \(\pm s\), and the four axis/diagonal contact certificates. The determinant calculation gives the exact sharp ratio and inverse mismatch. Standard John/Löwner existence, uniqueness and affine invariance are used.

Reproduce numerical checks with `python CHECK.py`, with NumPy installed. The checker constructs 187 pairs, including noncommuting and strongly conditioned matrices, independently computes eigenvalues and determinant mismatches, samples complete radial boundaries, tests all four inner and all four outer contacts, numerically bounds intersection area, and tests ratio formulas. The run returned `EQUAL_AREA_ELLIPSE_EXTREMAL_PAIR_CHECKS_OK 187`.

Finite grid checks cannot rule out missing intermediate configurations or establish historical priority. Outer-optimality alone is classical; the specific simultaneous inner/outer formula and spectral mismatch are the claim reviewed here. No independent mathematical audit has been performed.
