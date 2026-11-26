---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The two covariance formulas and root locations are correct, but the Finding's unqualified k=2 negative-interval width (RESULT.md line 24) is false on the stated probability domain. At n=3,k=2, H=(1−2p)(2−p); on 0<p<1 the covariance is negative precisely on (1/2,1), whose width is 1/2, not 3/(4n−10)=3/2. At n=4 the width is 1/2 and the second root is on the boundary; for n≥5 both roots are interior and 3/(4n−10) is the width. At n=2 the interval is empty. For the core proof, condition on long-run start j: event B_j forces A_j, makes A_i impossible for the other starts in [j−1,j+k] intersected with the word, and is independent of the rest. For i=j−1 the contradiction is a required one against the forced zero preceding the long run, not a required zero as line 43 suggests. Independently, group words by J ones and R positive success runs. There are binom(n−J+1,R) placements of the zeros, binom(J−1,R−1) compositions of the ones, and R binom(J−k,R−1) compositions with a distinguished long run, using zero for impossible binomial entries. Weighting by p^J q^(n−J) gives the ordinary, long and mixed moments and verifies the covariance (also derived directly from the prior PGF below). For k≥3 and s=n−k≥1, H(0)=s+1, H(1/2)=−(k−2)(s+2)/4, H(1)=s−k, and the leading coefficient is positive, so the second root is interior iff s>k. The k=2 factorization and the separate n=k formula give the other stated placements, and division by s gives the limiting quadratic for fixed k≥3. The independent exact bounded replay (python /workspace/replay.py 4) verified 364 covariance instances and gives widths 1/2,1/2,3/10,3/14 for k=2 and n=3 through 6; it is not the general proof. The exact phase conclusion concerns linear iid common-p words and maximal success runs only.

## originality

FAIL

Verified mathematical coverage, not failure of access: Inoue and Aki (2005) give the exact double generating function for the joint distribution of this very pair in their linear iid Bernoulli model, choosing k-vector (1,k) and Type II for both coordinates. Substitution and ordinary differentiation give the stated finite covariance polynomial; all of the valid phase claims follow by elementary evaluation of that polynomial. This is a directly evaluated corollary of their stronger exact result, even if the sign-switch wording and the specialized polynomial are not printed there. The stronger coverage was identified in follow-up to Kamalja's cited-reference entry and checked against the actual full-text Proposition 2.3.

## value

FAIL

The dependence question is naturally motivated, and the sign pattern could be useful as an exposition of this covariance. For an independent finding, however, the exact invariant is mechanically obtainable from the already published exact joint PGF for these counts, followed by the elementary quadratic test. Correcting the missing width boundary or narrowing to that sign test would not leave a distinct scientifically valuable result at the stated standard. No repair is submitted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
