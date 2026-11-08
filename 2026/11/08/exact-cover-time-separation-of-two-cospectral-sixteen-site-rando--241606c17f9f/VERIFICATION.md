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

The strict numerical separation is certified by rational, not floating-point, computations. Run `python3 verify.py` in this directory with Python 3 and `g++` supporting C++17. The script recompiles `exact_cover.cpp` and `cover_dp.cpp`, checks all graph parameter identities, recomputes all \(32767\) hitting-set determinants per graph and the exact rational sums in `CERTIFICATE.json`, checks the positive rational difference and interval, and compares with an independently formulated visited-set expectation recursion.

The proof uses a finite graph with exactly 16 labeled vertices. It does not assert any infinite-size limit, nor does numerical agreement alone establish the rational inequality. The signed integer determinant calculation and rational comparison do. Exact-certificate results remain unverified independently of the self-review.
