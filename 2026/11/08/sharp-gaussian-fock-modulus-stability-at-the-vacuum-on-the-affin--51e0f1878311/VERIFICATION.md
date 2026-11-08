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
# Reproduction and limits

The sharp constant is proved by exact Hilbert-space minimization and the Rician-modulus convexity lemma in `RESULT.md`. Execute `python3 CHECK.py` with the Python 3 standard library. The checker separately integrates the Gaussian polar expectation, evaluates the modified-Bessel power series, checks the requisite Bessel inequality on an explicit finite mesh, and tests the sharp example. Finite checks do not certify the statement for every real parameter; the first-crossing argument is the infinite proof.

The reference has Gaussian total mass one and the first two Fock modes each have squared norm one. No external validation or independent mathematical audit has been conducted. The result is restricted to affine polynomials and is not a full-space optimal constant.
