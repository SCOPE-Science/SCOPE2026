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

Kummer counts outgoing carries including the last place, and subtracting the initial run T of 2s gives the Catalan valuation. Marking each initial canceled carry by x and every other carry by z=xy gives the stated two-state resolvent and numerator, including the all-2 word and L=0. The explicit digit witnesses realize every proposed support cell, and with a carry at every place the first non-2 digit must be 1 and each later digit 1 or 2, giving the top counts. Independently, for r=1/3 and q=r^L, outgoing carries c_i have Cov(c_i,c_j)=r^(j-i)(1-r^(2i))/4 for i<=j; conditioning on T>=j forces the first j carries and gives E[A|T>=j]=(L+j)/2+(1-r^(L-j))/4. These sums give Cov(A,T)=5/8-(L/2+3/4)q+q^2/8 and subtracting from Var(A) gives the claimed exact covariance. The dominant eigenvalue has the asserted logarithmic expansion near 1, and T is bounded in mean, giving the stated diagonal Gaussian limit by Slutsky. Fresh replay: python3 -B /workspace/reviews/reproduce.py 5 passed the digit-sum census through L=9, coefficients, support, boundary, moments and 729 direct binomial checks; finite computations do not prove the limit or unlimited depth.

## originality

FAIL

The earlier ternary Catalan record already gives the exact indexed slices by the initial run T of digit 2, not merely their marginal sum. Those slices contain exactly the joint table's information because H is the Catalan valuation and A=H+T. The proposed rational series is the direct regrading of that exact proof-level decomposition; the boundary, covariance and Gaussian pair are evaluations or consequences of the same coverage, not a separate surviving novel claim.

## value

FAIL

The dependence interpretation and covariance are mathematically meaningful, but as a standalone finding the exact law mechanically re-marks already evaluated trailing-run slices and the proposed joint limit is immediate from the scalar limit and the known tight difference. The finite derivatives and support readings do not identify an independently nontrivial residual gap beyond the existing exact decomposition.

The dated certificate retains the supplied scientific assessment, sources and limitations.
