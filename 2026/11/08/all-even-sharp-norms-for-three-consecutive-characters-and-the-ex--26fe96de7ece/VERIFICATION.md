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

# Verification and reproducibility

Run `python3 artifacts/verify.py` from the extracted package root using Python 3. The expected successful terminal line is:

`THREE_MODE_EVEN_MOMENTS_PASS exact_and_grid_checks=108 h=2..15`

The checker reconstructs multinomial-power coefficients with exact arithmetic, verifies the closed polynomial and derivative coefficient identities for all integer exponents in the stated finite test range, checks coefficient sign patterns and numerical maximizers, compares aliased and nonaliased root-of-unity grids, and tests representative large-exponent drift.

The independently relevant analytical steps are (i) the character-orthogonality identity; (ii) monotonicity in the endpoint product through the zero-step expansion of a nonnegative trigonometric polynomial; (iii) uniqueness of the positive derivative root by Descartes' rule; (iv) strict finite cyclic aliasing using two positive coefficients in one congruence class; and (v) one-dimensional uniform Laplace expansion near the unique peak. All parameters \(h\ge2\) and qualifying compact abelian groups are covered by those arguments, not by finite enumerations.

The result does not give the exact constants in the aliased regimes \(3\le q\le2h\). The large-moment estimates are asymptotic and do not assert certified finite-\(h\) uniform error constants. No independent mathematical audit has been performed.
