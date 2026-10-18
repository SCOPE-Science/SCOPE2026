---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

Cortez's exact invasion formula is R0=C E[Theta(Theta-1)]. For every integer n the factor (n-k)(n-k-1) >=0 yields lower affine support and equality at k,k+1; n(K-n)>=0 yields upper chord and equality exactly 0,K. Taking expectations gives bounds, and the explicitly constructed two-point laws with masses 1-delta/delta and 1-m/K/m/K satisfy the mean constraint; their mixtures fill the interval because the expectation is linear. The no-cap 0/L mixture gives Cm(L-1)->infinity. Checked sample K=10,m=3,C=1/10 giving exactly 3/5 vs 27/10. This is a valid universal discrete-moment theorem, not a numerical extrapolation.

## originality

FAIL

FAIL: Theorem 3.4 in Klebanov (2024) supplies the EXACT SHARP upper/lower range of E f(X) at fixed E X for ANY finite support/domain/function as vertical sections of the graph convex hull. Apply it with support K={0,...,K} and f(n)=n(n-1): its lower faces join consecutive integer points and its upper face joins (0,0) to (K,K(K-1)). It therefore IMPLIES the entire purported new sharp envelope, attainability, equality laws, and mixtures; Cortez (2024) already provides the factor C. The threshold tests are immediate comparisons with 1 and no-cap unboundedness immediate 0/L law. The exact original statement is thus a routine specialization of stronger prior results, even though Cortez does not write it verbatim.

## value

FAIL

FAIL: Sharp random-variable second-moment envelopes at a fixed mean and support are classical convex-hull/Jensen consequences, explicitly covered by a 2024 general theorem. Multiplying the inherited envelope by an existing epidemic reproduction formula and comparing it to 1 is a routine immediate exercise; the policy interpretation alone is not a substantive mathematical gap or independently unknown exact invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
