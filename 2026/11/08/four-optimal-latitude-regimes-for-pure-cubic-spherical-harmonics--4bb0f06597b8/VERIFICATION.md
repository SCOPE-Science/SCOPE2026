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

# Verification and limits

Run `python3 check_cubic_latitude.py` from this folder with Python 3 and no third-party dependencies. The exact rational verifier checks the finitely many global interval-separation certificates for dimensions \(3\) through \(11\), isolates each active root with exact rational bisection, proves the inactive eigenvalues are strictly above it using interval arithmetic, and checks the polynomial identities underlying the universal \(d\ge12\) inequalities. It prints `CUBIC_LATITUDE_RATIONAL_CERTIFICATE_PASS 201` on success.

The separate numerical Gaussian-Jacobi moment-quadrature cross-check used spherical fourth and sixth moments at dimensions \(3,4,5,11,12,25,100\) and five squared latitudes, agreeing with all four eigenvalue formulas for 140 comparisons to relative tolerance \(2\times10^{-12}\). This numerical check is supportive only and is not needed for the infinite-dimensional quantifiers. The proof of all-dimensional optimization depends on the explicit radial decomposition, strict derivative monotonicity, finite exact interval separations and positive-coefficient polynomial expansions given in `RESULT.md`; code output alone is not offered as a theorem proof.

No independent mathematical audit has occurred. Historical priority is provisional; exact spectral branches can also be inferred from earlier integrated spherical-cap formulas, while the new statement assessed here is the four-regime global E-optimum. The theorem concerns continuous probability-normalized pure cubic harmonic traces on a single latitude, not finite sensors or the full spectral condition number.
