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

# Verification of the conditional section-type diagram

The analytic proof, rather than numerical sampling, establishes the universal theorem. The standalone `verify.py` is a reproducible consistency test; run `python verify.py` with NumPy installed.

The completed execution reported:

`DISPHENOID_SECTION_OK random_profiles= 18000 polar_checks= 5 Haar_samples= 540000 max_polar_error= 2.64e-16 max_envelope_violation= 0`

The program checks exact endpoint formulas at selected dominant-axis fractions, draws 18,000 positive normalized axis triples, compares five analytic section predictions with independently evaluated polar-tetrahedron vertex solid angles, performs 540,000 Gaussian orientation trials for section side counts, and evaluates the local curvature coefficient near regularity. It checks neither historical priority nor the universal validity of an analytic argument by finite enumeration. All pure mathematical claims and assumptions are spelled out in `RESULT.md`.
