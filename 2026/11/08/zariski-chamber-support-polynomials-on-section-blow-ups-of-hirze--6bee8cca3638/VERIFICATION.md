---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

The claim counts negative-part supports on the smooth complex blow-up, for e,r=n-e at least two and distinct centers on the section disjoint from the negative section. Any other nonfiber curve has class aS_0+bF with b>=ea; intersecting with the marked fibers and the section gives m_i<=a and sum(m_i)<=b. Thus sum(m_i^2)<=ab, and its transformed square is at least a(b-ea)>=0. The two sections and n pairs of exceptional/strict-fiber curves exhaust the negative curves. In each pair at most one curve can be selected (otherwise the principal block is singular). Eliminating chosen -1 curves leaves a diagonal section block with entries -e+f and -r+a, when the corresponding section is present. The four cases give exactly the four displayed terms, including empty support. Both-section terms have degree at most n; the single-section terms reach n+1 when all n fibers contribute, giving the two binomial tails and hence 2^n-binomial(n,e). Swapping sections and the two kinds of leaves gives the stated symmetry. Independently expanding the integer binomial sums gave totals 198, 618, 2004, and 19526, and coefficient vector (1,10,41,76,60,10) at (e,n)=(2,4). The example calculation checks arithmetic, not the universal classification. The frozen verifier and output were inspected, not executed; their matrix tests stop at n=6, so the n=8 example was checked separately. No formal certification is asserted.

## originality

PASS

The supported content is the uniform two-weight support polynomial and its exact maximal-support coefficient, not the general matrix algorithm, the elementary transformation, or the boundary case. Accessible comparisons do not cover that joint claim. The unresolved full-text risk is explicitly retained.

## value

PASS

The invariant is the graded support census on a natural family of ruled surfaces of unbounded Picard rank. The uniform formula distinguishes the effects of both section weights, yields exact extremes without enumerating growing matrices, and provides closed-form tests for chamber algorithms. This is not merely the evaluated small examples or a substitution into the boundary formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
