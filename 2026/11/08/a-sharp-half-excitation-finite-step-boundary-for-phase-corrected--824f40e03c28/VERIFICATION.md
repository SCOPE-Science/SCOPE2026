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

Run `python check.py` with Python 3 and NumPy. The checker constructs direct two-qubit exchange unitaries and compares the computed battery excitation to the analytic interference formula for resonant and detuned parameter choices. It builds equalizing measurement bases, checks both output excitations, and checks phase-corrected end states. It also verifies the sustainable fixed-point endpoints and derivatives for rational Pythagorean parameter pairs, and exercises a finite-attainment example and a nonattaining example.

At preparation, the checks completed: 168 exact-rational identities, 450 physical two-qubit/measurement checks, 250 detuned two-qubit checks, and the example trajectories. The checks are finite. The universal claim follows from the symbolic quadratic stationary-population criterion and strict concavity and endpoint derivative in RESULT.md; numerical samples alone cannot establish universality.

Limits: the theorem assumes pure chargers, pure conditional battery states, perfectly observed rank-one charger measurements, and ideal outcome-conditioned energy-preserving phase rotations. It addresses conditional mean energy, not shot noise in projective energy measurement, and excludes measurement and feedback implementation costs. Independent audit has not been performed.
