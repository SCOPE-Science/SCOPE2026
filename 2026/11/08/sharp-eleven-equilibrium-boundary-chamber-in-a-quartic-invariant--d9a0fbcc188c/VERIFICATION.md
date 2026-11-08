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

# Verification of the boundary equilibrium theorem

The complete proof is in `RESULT.md`; reproduction uses `CHECK.py` from the same package with Python 3 and no external dependencies. The checker carries out exact rational arithmetic with the standard-library `fractions.Fraction` type.

The script establishes, for the eight explicit witnesses, boundary counts \(4,5,6,7,8,9,10,11\), respectively. It independently checks \(17{,}998\) exact rational parameter choices against the ceiling and maximal-chamber criterion; tests \(1{,}330\) nonzero rational quadratic coefficient triples against the strict two-interior-root inequality; and checks four exact Sylvester determinant resultants and all four corner Jacobian eigenvalue pairs for the hyperbolic eleven-point witness. These deterministic finite checks were executed successfully from the packaged file.

The proof of the universal assertions instead uses: (i) reduction to four univariate quadratics; (ii) a sign incompatibility for two double-root-bearing horizontal edges; (iii) exact vertex/discriminant/end-value criteria for two roots in an open unit interval; (iv) explicit rational attainment of every finite count; and (v) resultant nonvanishing and diagonal corner spectra to verify hyperbolicity. Endpoint roots do not count as non-corner points; repeated roots count once.

The checks do not enumerate arbitrary real parameters and do not establish independent validation, classification of interior equilibria, limit cycles or full phase portraits. No independent audit has been performed.
