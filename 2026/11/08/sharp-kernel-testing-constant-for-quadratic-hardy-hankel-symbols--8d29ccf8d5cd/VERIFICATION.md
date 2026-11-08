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

The exact singular-norm formula follows by diagonal phase reduction of the displayed two-by-two Hankel block. Squared kernel outputs follow directly from the two Taylor coefficients of each normalized Szegő kernel. The factorization used in the proof is a polynomial identity in the parameter \(u^2\in[0,1]\), and sharpness is proved by a strictly negative second derivative of the radial extremal function.

To repeat the diagnostic checks on a clean Python 3 standard-library installation, run `python3 check_quadratic_hankel.py` from this directory. The actual check run printed `QUADRATIC_HANKEL_CHECK_OK 2621`: 2,002 exact rational assertions, coefficient-phase checks against the direct two-by-two matrix, and tests of the sharp example. These checks are finite and do not substitute for the all-parameter proof.

Scientific scope: arbitrary complex coefficients for the quadratic polynomial with no constant term; no assertion about degree three or higher, arbitrary rational finite-rank symbols, or general bounded Hankel operators. No external or independent mathematical review has been performed.
