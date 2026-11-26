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

The result uses all m gaps, including the boundary gaps, with sum one and the uncorrected Gini normalization. An independent check is to work on the descending ordered simplex: its density is constant, and Z_r=r*(X_[r]-X_[r+1]), with X_[m+1]=0, is a linear bijection onto the standard simplex since sum_r Z_r=sum_i X_i=1. Thus Z is again Dirichlet(1,...,1). The coefficient vectors of M and G in Z are a_r=1/r and b_r=1-r/m: r(m-r) pairs cross the r-th gap. For any two such linear forms the covariance is [m*sum(a_r*b_r)-sum(a_r)*sum(b_r)]/[m^2*(m+1)]. Here the three sums are H_m-1, H_m and (m-1)/2, respectively, and the same formula with a,a or b,b gives the stated two variances. In particular the exact covariances at m=2,3 are 1/48 and 1/54. Positivity follows from the numerator being 1/2 at m=2 and increasing by H_m-1+1/(m+1). At m=2 there is the affine identity M=G+1/2; for m>=3, affine dependence on the simplex would require the vector 1/r to be affine in r at three or more ranks, which is impossible. The harmonic limits give the coefficient 3*sqrt(2)/pi in the correlation. The frozen verification script and recorded output were inspected, not executed; their seeded checks are corroboration, not the general argument.

## originality

FAIL

An earlier indexed exact upper-share covariance theorem gives the identical covariance at k=1 with the same Gini normalization and the same simplex law. The additional Pearson formula and decay constant follow by elementary normalization using the marginal variances, and the strict inequality classification is the standard affine-equality test. The inspected primary papers supply older distributional context, but the decision relies on the demonstrated exact coverage and the routine nature of the remaining deductions, not on an assertion of historical priority.

## value

FAIL

Comparing two natural irregularity measures is well motivated, but the exact covariance is already furnished by the complete upper-share profile. The Pearson normalization, strict affine-equality test and harmonic asymptotic are routine additions and do not leave an independently useful new exact claim under the required standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
