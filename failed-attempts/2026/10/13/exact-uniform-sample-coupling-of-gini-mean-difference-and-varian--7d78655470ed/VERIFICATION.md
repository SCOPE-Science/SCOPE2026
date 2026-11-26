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

The proof is correct for iid uniforms on a nondegenerate interval and all integer n≥2, with the ordinary pair-average Gini difference and unbiased variance. Rescale to [0,1] and put T=|X−Y|; its density is 2(1−T) and its r-th moment is 2/((r+1)(r+2)). The kernels h=T and g=T²/2 have means 1/3 and 1/12; the same-pair variances and covariance are 1/18, 7/720 and 1/45. Their conditional means are A(x)=x²−x+1/2, B(x)=(x²−x+1/3)/2. The corresponding variation and covariation are 1/180, 1/720 and 1/360. Counting each pair once against itself and 2(n−2) times against different overlapping pairs, and discarding independent disjoint pairs, gives the three moments with denominator binomial(n,2) and scaling ℓ², ℓ⁴ and ℓ³ respectively. Division gives the positive correlation and deficit (n+1)/((n+3)(2n+3)); the successive decrease has numerator 2(n²+3n+1)>0 over the positive product denominator. A−2B=1/6 pointwise, so subtracting 1/6 as in the frozen C_n removes the whole first projection. The centered pair kernel variance is 1/180 by the triangular density, hence the contrast variance is 1/(90n(n−1)), including n=2. The supplied exact-rational script and recorded output were inspected, not rerun. Its bounded checks supplement, rather than prove, the identities for every n.

## originality

FAIL

A distinct indexed result on the same iid uniform order statistics and the same unbiased variance supplies a stronger mixed covariance profile. Its weighted sum gives exactly the headline covariance, not just similar parameters. In combination with prior marginal moments, it also yields the entire correlation and contrast variance, and the first-projection cancellation follows from the variance order. The same-day ordering of the two records is not established. The failure is demonstrable equivalent coverage and no supported distinct claim in this audit, not a finding that the other record was published first. The explicitly overlapping November result is later and is not used to infer October priority.

## value

FAIL

Joint finite-sample behavior of two standard scale estimators is a motivated question, and the degenerate contrast gives a clear explanation. But the specific finite moments and projection cancellation are mechanically implied by the stronger indexed profile and known marginals, as shown above. The record adds an elementary direct derivation, not an independent joint-law consequence, distinct invariant, or nontrivial new method that meets the scientific-value standard after accounting for the overlap.

The dated certificate retains the supplied scientific assessment, sources and limitations.
