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

FAIL

The independence wording in the Finding is false if applied literally to the normalized residual Z defined in the assumptions. The padded n-vector Z has its unique zero at I almost surely, so P(Z_i=0 | I=i)=1 while P(Z_i=0)=1/n. The proof instead establishes mutual independence of m, I, and the (n−1)-tuple of nonminimum residual coordinates read in original-index order after deleting I. This distinction does not invalidate the majorization or covariance. On the minimum-i chamber, retaining all but one of the other coordinates gives a Jacobian proportional to (1−nt)^(n−2), so the deleted tuple is uniform on its simplex, independent of t and i. The equal chamber masses give uniform I; integrating or taking the volume of {X_j≥t all j} gives P(m≥t)=(1−nt)^(n−1). Thus nm is Beta(1,n−1), with Var(m)=(n−1)/(n^4(n+1)). Padding the independent tuple at the sampled index gives the correct conditional coupling X_t=t1+(1−nt)Z. For s<t<1/n this mixes X_s with the barycenter with weight λ=(1−nt)/(1−ns) on X_s; all top-k sums are pulled toward k/n and X_s≠X_t. This proves simultaneous Schur order (and strict inequality for strictly Schur-convex statistics), using a regular conditional version. The residual maximum of n−1 components has mean H_(n−1)/(n−1), via integrating the inclusion–exclusion survival function. Hence Cov(m,M)=Var(m)[1−n H_(n−1)/(n−1)]=(1−H_n)/(n^3(n+1)). Independently the minimum of n iid exponentials has rate n and is independent of the maximum of the n−1 exponential excesses; E[min·max]=2/n²+H_(n−1)/n, and the gamma total has independent square moment n(n+1), confirming the formula. At n=2 the deleted tuple is the constant 1, M=1−m and the covariance is −1/48. The finite rational checker was inspected rather than executed. If 'residual simplex point' is read as the deleted tuple in the proof, that intended independence statement is correct; it is not independence of the defined Z and I.

## originality

FAIL

The October 18 Resultary record 254686d5bc83 explicitly gives the intended full minimum–deleted-residual independence and already couples the conditional laws with the same residual. Although its stated application is exceedance counts, the entire frozen majorization conclusion is a direct one-step consequence of the very same affine coupling, with no further distributional input. The extreme covariance is a routine conditional-moment calculation from that published conditional law and the classical maximum mean. This establishes mechanical prior coverage, not an assertion that sources print identical terminology or the identical covariance expression.

## value

FAIL

A simultaneous dependence statement has a natural interpretation, but here the stronger-sounding order is the direct barycentric contraction of a previously given conditional sample. Once this is recognized, the exact extreme covariance is a beta variance multiplied by an affine slope involving a classical first moment. Correctly distinguishing the deleted and padded residuals repairs the wording only; it leaves no independently new and substantive remainder to accept.

The dated certificate retains the supplied scientific assessment, sources and limitations.
