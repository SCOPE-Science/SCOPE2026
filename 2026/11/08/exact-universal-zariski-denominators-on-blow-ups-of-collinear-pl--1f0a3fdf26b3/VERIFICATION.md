---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-14.md",
      "INDEPENDENT_AUDIT_2026-11-14.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Bézout against the common line ensures only L and E_i can be negative, and the effective curve cone is their nonnegative span. The mixed support matrix has negative-definite Schur complement -(n−1−k) and determinant magnitude n−1−k, bounding all denominators. For any 1<=r<=n−1, explicit D_r has Zariski negative part coefficient 1/r; added nef Q_r with square r(r+1)>0 gives a big witness. All negative-definite supports occur with big witnesses and count 2^(n+1)−n−1. Independent exact rational intersection checks cover n=3..25; analytic argument is all n.

## originality

PASS

The full ar5iv text of Bauer–Pokora–Schmitz Example 3.4 establishes this precise collinear family and its maximal single denominator n-1. Its negative intersection support determinants have absolute values n-1-k, which imply the upper bound u(X_n)|lcm(1,...,n-1), but neither a greatest common clearing multiple nor witnesses for each intermediate r are stated. The submitted effective/big D_r constructions give exact reduced coefficients 1/r for all r and therefore the reverse divisibility. This produces the sharp least simultaneous denominator-clearing multiple; value is a natural all-divisor invariant, not generic larger maximum denominator.

## value

PASS

Least simultaneous clearing multiplier for all integral divisors is a natural surface-wide arithmetic invariant, distinct from the maximum denominator known from Bauer et al. Uniform big effective witnesses for every 1<=r<=n−1 are motivated by geometric negative supports and establish a genuinely complete finite spectrum for all n, not arbitrary small-slice enumeration. The auxiliary chamber count is mathematically intrinsic.

The dated certificate retains the supplied scientific assessment, sources and limitations.
