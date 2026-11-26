---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

Over GF(2), successive rows on a path determine a kernel vector from its initial coordinate, so a singular branch has nullity one and its endpoint coordinate is nonzero. The leading-minor determinant recurrence D_s=d_s D_{s−1}+D_{s−2}, with D_0=1, yields 11 invertible and 5 singular P_4 perturbations. At an internal root, a kernel vector with root coordinate 1 requires both arm matrices to be invertible: otherwise a nonzero arm kernel vector has its endpoint coordinate 1, making the arm equation inconsistent. Conversely, if both are invertible, their solutions determine the unique root diagonal making a kernel with root coordinate 1. The arm counts 1 and 3 give three visible singular perturbations, leaving two invisible. For a global perturbation with K singular branches, if none is visible at its root, all branch equations are solvable for either hub value and the hub row either imposes its vanishing or imposes no condition, once each as the hub diagonal varies. If at least one is visible, the hub value is forced zero and the hub row then removes one dimension of the K-dimensional branch kernel for either diagonal. Summing these cases and reversing coranks to ranks gives both frozen polynomials. Independently extracting coefficients gives the six minima 135, 1476, 10864, 63840, 295872, 749440 and the first failing triple (128, 5056, 242234), with defect −5442816 on 29 vertices. For m≥7, the positive quadratic part of the first-defect bracket grows by a factor at most (8/7)² while the exponential part grows by 5/2; the defect remains negative. In the endpoint sequence, only indices 2 and 3 of the reversed sequence can have non-binomial interior triples. With v=5/11 the reversed coefficients are 2 binom(m,j)v^j plus 1 at j=1,2. Direct expansion gives the two displayed defects, each strictly positive by writing m=4+t, t≥0; the m=3 sole defect is 7646111 and m≤2 is vacuous. The support is consecutive after the initial zero powers are removed. RESULT.md and the independent coefficient extraction establish the claims; the supplied VERIFICATION.md and rank checker were inspected, not executed.

## originality

PASS

Credit belongs to the exact position-dependent phase diagram: the all-order endpoint result and the sharp m=7 first internal failure with strict positivity of all inequalities below it. The two generating polynomials, branch counts, first-defect formula and eventual internal failure are covered by specializing the earlier attachment theory; they do not count as original findings on their own.

## value

PASS

P_4 is the first path with geometrically distinct endpoint and next-to-end attachments beyond the three-vertex case, and keeps the branch graph and order fixed while changing only the attachment position. The comparison converts eventual failure into a sharp finite boundary and explains why the endpoint regime never fails. This is more than repackaging the rooted generating formula or exhibiting an isolated defect: the small-m positivity and the endpoint all-order result certify the two regimes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
