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

# Verification

The standalone `verify.py` uses only Python's standard library and checks exact arithmetic branch conditions against independently evaluated two-step Volterra coefficients for nine integer pairs, including coprime, noncoprime and equal indices. It verifies output injectivity, the disjoint branch singular lists, positive monotonic cubic weights, rational identities, and numerical agreement of the first two inverse-power coefficients. The diagnostic run passed **16,166** finite checks.

The infinite-dimensional statements are proved in `RESULT.md`: multiplication-index injectivity diagonally determines \(K^*K\); exact lattice counts determine the quadratic branch; inversion of a strictly decreasing rational function yields the cubic branch and its constant; comparison of growth rates and monotone inversion give the two singular-value orders. These analytical steps establish compactness, infinite rank, and failure of every finite Schatten exponent. Finite checks cannot verify the infinite theorems or guarantee novelty.

No external verification or independent mathematical audit has been performed.
