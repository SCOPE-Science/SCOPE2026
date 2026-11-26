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

The unique John ellipsoid is invariant under permutation of the n residual coordinates, so in the affine (x_1,u) coordinates it has separate axial radius s and circular radius rho. The end constraints are s<=c and c+s<=h. Each residual coordinate has center (n−c)/n and squared support radius s²/n²+((n−1)/n)rho², giving the sharp feasibility constraint s²+n(n−1)rho²<=(n−c)². For fixed feasible s, lowering c to s preserves feasibility of the end constraints, and maximizes the allowable rho strictly unless c=s. At c=s the volume objective is proportional to s[n(n−2s)]^((n−1)/2), which has its unique unconstrained maximum at s=n/(n+1). The cap imposes s<=h/2, giving both branches and contacts by active supports. The Gram matrix of the restriction of an orthonormal zero-sum embedding to the last n−1 coordinates has determinant 1/n, giving the 1/sqrt(n) volume factor. The logarithmic derivative 1/h−(n−1)/(2(n−h)) vanishes at h_* and its derivative there on the lower branch is negative, proving C¹ and failure of C². The strict inequality in proof line 62 at c=h/2=alpha is a nonessential endpoint slip: the derivative is zero exactly there and positive before it, and the constrained optimum and Finding are unchanged.

## originality

FAIL

Demonstrably covered, not a priority or access judgment. Resultary d34d69923786 gives the same John ellipsoid and all contact regimes in every dimension n>=2 after an invertible affine change of coordinates. The volume, its regularity, and the one-capped arbor example mechanically follow from those exact branches. A second, broader frustum result specializes to the same family in dimension at least three.

## value

FAIL

The frustum and its inscribed ellipsoid are natural, but this record delivers no independently useful unknown exact fact beyond the covered geometry. The one-capped arbor instance is a single substitution, the Euclidean volume is an immediate determinant conversion, and the smoothness description is routine differentiation of the known exact branches. The concise optimization is useful as exposition but does not provide a new structural conclusion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
