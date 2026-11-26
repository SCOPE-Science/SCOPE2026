---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Uniqueness of the maximizing inscribed ellipsoid forces coordinate-permutation invariance, hence the stated center and two-eigenspace matrix. For fixed axial sum half-width R, the allowed center sums satisfy a+R≤s≤1−R, and β²≤(s²−R²)/(d(d−1)); maximizing first over s and β gives s=1−R and β²=(1−2R)/(d(d−1)). The remaining log derivative of R(1−2R)^((d−1)/2) has the sign of 1−(d+1)R. Thus the global optimum is at min{1/(d+1),(1−a)/2}; substituting gives the two phase formulas, equality at a_*, and all facet contacts including lower-facet contact at equality. The denominator is (1−a^d)/d!. In the upper phase the reciprocal of the varying quotient is Σ a^(j−(d−1)/2), decreasing strictly by pairing the exponents t and −t for t>0. This gives strict increase, including across the common transition value, and evaluating the geometric sum at 1 gives the stated boundary limit.

## originality

FAIL

The exact unrestricted ellipsoid, threshold and contact regimes are already covered by an earlier same-family statement and an earlier arbitrary-base frustum theorem. The ratio is an immediate normalization of the latter's volume formula, with strictness by a one-line pairing argument. A separate indexed arbitrary-base result explicitly states the strictly increasing normalized fraction and covers the whole frozen claim; it is dated the same day and no within-day priority is inferred.

## value

FAIL

The family and its affine-invariant ratio are natural, and the scalar derivation is useful exposition. As a separate finding, however, the work repeats already determined ellipsoid data and a mechanically implied ratio profile, which is also stated explicitly in stronger generality. No independent new invariant or surviving substantive refinement is demonstrated.

The dated certificate retains the supplied scientific assessment, sources and limitations.
