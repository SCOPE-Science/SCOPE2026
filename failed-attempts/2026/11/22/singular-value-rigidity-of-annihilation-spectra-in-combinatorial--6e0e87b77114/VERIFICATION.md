---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Rees multiplication gives B_(i,lambda),(j,mu)=Z_(lambda,j)Z_(mu,i), including exactly the square-zero loops. The operator X→(ZXZ)^T in the two singular bases annihilates every matrix unit outside the leading r by r block; it acts on diagonal units by s_a² and interchanges off-diagonal pairs with multiplier s_a s_b. The asserted polynomial, inertia, trace powers and energy follow even with multiplicity, zero rank or rectangular dimensions. Reverse recovery also follows directly: for each x>0 subtract the multiplicity of −x from that of x in B's spectrum; this equals the multiplicity of x among the squared singular values. This works even when off-diagonal products coincide with squared singular values. Ordered pairs correspond bijectively to two chosen zero positions, with z of the z² choices yielding loops. Fixing a vertex leaves independent choices from one row and one column. These are exact checks, not deductions from the numerical transcript.

## originality

FAIL

The central spectral theorem is already covered by the full rectangular pure-state partial-transpose spectrum theorem, not merely similar to it. Set v_(i,lambda)=Z_(lambda,i). Partial transpose of vv^T on the second factor has entries v_(i,mu)v_(j,lambda)=B_(i,lambda),(j,mu) exactly. If Z≠0, normalize v by its Euclidean norm to apply the prior theorem; multiply the spectrum by ||v||² afterwards. Its Schmidt coefficients are exactly the normalized singular values of Z, and its zero multiplicity is mn−r². Undoing normalization gives the entire spectrum; all stated spectral summaries and the reverse direction are immediate from that known multiset. Z=0 is trivial. The particular semigroup label need not appear in the prior theorem, and no earlier paper on this exact semigroup invariant is being asserted.

## value

FAIL

The identification is convenient for notation, but unlike a new representation theorem it is the immediate cross-product identity in the defining Rees multiplication. It exposes exactly the existing rank-one partial transpose, not a new invariant beyond that theory. The remaining moment, degree, or reverse statements are direct sums, index counts, or cancellation from the old multiset. The frozen result provides no independently valuable remainder to repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
