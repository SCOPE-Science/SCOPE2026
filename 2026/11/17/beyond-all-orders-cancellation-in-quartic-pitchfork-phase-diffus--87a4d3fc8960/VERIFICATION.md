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

## Reproduction

Run `python verify_phase_diffusion.py` in the extracted directory. It checks the first six exact combinatorial coefficients and finite numerical quadratures using SciPy and NumPy. A successful output reports `QUARTIC_PHASE_ALL_ORDER_CHECK_OK`.

## Analytic check

The actual infinite-order proof is the comparison of the Gaussian-moment expansions of the partition function and of the barrier integral after the substitutions described in `RESULT.md`. Both have coefficient \(a_k=(4k)!/(16^k(2k)!k!)\) at every integer index, with arbitrary-order remainder bounds. Gaussian complementary-error-function tails make the outside-barrier contribution smaller than every inverse power of the barrier parameter.

## Scientific limits

The numerical checks sample finitely many barrier heights and cannot certify an infinite asymptotic series. The exact finite-parameter covariance integral and leading Kramers behavior were available in earlier literature. No external independent validation is claimed.
