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

The finite classification uses exhaustive exact arithmetic, not statistical sampling. Run `python3 verify_legendre_f13.py`. It checks two independent polynomial presentations of each quadratic and cubic extension of \(\mathbb F_{13}\), independent fourth-power membership predicates, the full \(11\)-parameter point-count table, Newton identities and the genus-three functional equation, all claimed elliptic factorizations, and the three complete cross-ratio orbits. The final line is `GENERALIZED_LEGENDRE_F13_SIX_WEIL_SPECTRA_VERIFIED smooth=11 spectra=6 cross_ratio_orbits=3 two_spectra_per_orbit=3 independent_field_models=2`.

Finite-field irreducibility certificates are complete in degrees two and three because any reducible polynomial of those degrees has a base-field root, and all thirteen candidates are checked. The point-count formula counts every \(x\in\mathbb F_{13^n}\) for each \(n=1,2,3\); the functional equation then determines all six coefficients of the Weil numerator. This does not determine Weil polynomials for parameters outside the prime field or other characteristics. No independent mathematical audit has been performed.
