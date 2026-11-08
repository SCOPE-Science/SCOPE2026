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

The companion standard-library `verify.py` generates the same allowed six-state transfer directly from the local domination rule, checks the two integer potentials on every permitted transition, and verifies the characteristic matrix identity at activities \(z=1,2,3,5\). It enumerates every subset of all \(2n\) vertices for \(n=4,5,6,7,8\), independently tests maximality and independence in the undirected graph, and compares each complete counting polynomial with the transfer result. It verifies both exact cardinality bounds and their end-pattern multiplicities in the covered periods. Separately, symbolic determinant factorization confirmed the characteristic polynomial.

The proof for arbitrary \(n\), the equality-cycle classification and the endpoint Puiseux coefficients are mathematical arguments in `RESULT.md`; finite enumerations do not certify infinitely many periods. Positive-activity analyticity follows from primitivity; the limits concern one-sided activity regimes only. Independent mathematical or bibliographic validation has not been performed.
