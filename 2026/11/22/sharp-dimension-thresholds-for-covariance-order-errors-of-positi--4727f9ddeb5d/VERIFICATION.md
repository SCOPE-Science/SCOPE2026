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

The proof is a closed-form algebraic argument using exact monomial moments, two-by-two determinants, Vandermonde rank and continuity. It does not depend on an external solver, finite enumeration or any unproved numerical conjecture.

The standalone `verify.py` runs exact-rational evaluations of the composite trapezoidal and composite Simpson rules at \(T=7/5\). It independently constructs the numerical and exact covariance matrices, compares the phase-boundary entries and first omitted moments, proves the displayed negative rational principal minors within each tested case, and checks the rank formula. The reproducible command is `python verify.py`; a successful run reports `PASS 56 exact-rational dimension/panel checks; rank and Loewner threshold certificates`.

The 56 finite tests cover \(1\le n\le7\) and \(1\le N\le4\) for both rules. The theorem for all finite dimensions and positive horizons is established in the written proof, not extrapolated from this sample. The perturbation argument establishes existence, not a numeric Hurwitz radius. No floating-point implementation error, stationary covariance claim or independent certification is addressed.
