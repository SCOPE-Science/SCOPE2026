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
# Exact verification and scope

The code file `check.py` requires only the Python standard library. Run `python3 check.py` in the same directory; it independently enumerates the special-linear matrices and counts the allowed second summands by determinant tests, without using the theoretical trace-factorization reduction to obtain the observed counts. Every target is checked at \((p,k)=(3,2),(5,1)\); additional sampled targets are checked at \((3,3),(5,2)\). The square-root formula is checked exhaustively for primes \(3,5,7\) at depths up to four. The uniform lower-bound and minimum-equality count follow from the all-depth proof, not from extrapolation. The external independent mathematical audit has not been performed.
