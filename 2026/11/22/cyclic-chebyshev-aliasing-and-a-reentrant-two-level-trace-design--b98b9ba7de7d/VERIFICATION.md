---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

The Chebyshev recurrence yields T_j(A)=(S^j+S^−j)/2. In the sign quadratic form, each summand z_a z_(a+j) has mean zero for 1≤j<n, and its product with another summand has mean one exactly if the unordered index pairs match. Equal orientations account for n matches if j=k, opposite orientations another n if j+k=n; these are disjoint matches even at j=k=n/2. Each separated distinct alias pair removes 2nr^n from the shared-probe variance; the lower member j of such a pair ranges from 1 to min(k,n−1−k,floor((n−1)/2)). On C4 the variances are (4r²,8r⁴+4r⁶) and (4r²+8r⁴,4r⁶); positive variances and costs ensure a unique positive real allocation by equality in the stated Cauchy–Schwarz bound. The difference of optimized variance–work products has the sign of the stated Δ. In x=r² I independently reconstructed the sextic P(√x), ran rational Sturm with variations 5 and 1 at x=0,1 and a nonzero constant last term, and found exactly one simple root in each squared bracket. Sign agreement of R and U retains only the second and fourth roots. This test is sufficient: the first squaring is reversible because U+2√3 x√(2+4x)=1+x(2√3√(2+4x)−2)>0. Independent exact sign bounds at r=1/100, 1/2 and 99/100 give +,−,+, yielding the displayed strict phases. Rational bisection confirms 0.237180713823998328… and 0.809548040154000412…. Independent exhaustive sign-vector calculations corroborated the covariance and every admissible cutoff at r=2/3 on orders 3 through 8. This proves only the two-block continuous allocation result under the specified one-sided recurrence costs.

## originality

PASS

The allocation theorem, consecutive-degree estimator and one-sided cost convention are already in Hallman–Troester. The distinct claim is the exact cycle alias-only covariance and the certified two-switch cutoff under those particular assumptions, not an estimator design principle or circulant-probing optimum in general. The alias formula is elementary once matched shift entries are identified; the two-switch result requires a matrix-family variance computation and verification that both admissible roots, and only those roots, change the optimum. No equivalent boundary was established in the inspected comparisons.

## value

PASS

The exact covariance identifies when ignoring cross-degree terms is valid and when it misses an entire positive alias pair. The smallest cycle with two possible nonempty degree cutoffs already exhibits a twice-reversing choice, an exact counterexample to monotonic cutoff selection as coefficient decay changes in a standard continuous allocation model. The thresholds describe the full phase diagram, not small numerical gains or an unmotivated instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
