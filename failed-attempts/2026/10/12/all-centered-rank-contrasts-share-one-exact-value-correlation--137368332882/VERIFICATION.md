---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

For atomless iid values, Stuart’s diagonal rank–value covariance is (N−1)G/4. A constant rank sum forces every off-diagonal to −G/4; contraction against any deterministic zero-sum c gives NG||c||²/4, and the permutation-rank variance is N(N+1)||c||²/12. Combining gives the claimed common correlation and the Mann–Whitney two-sample identity. Sharp Gini bound follows from Cauchy–Schwarz between X and F(X); equality iff X is affine in F(X), i.e. uniform on interval. Independently exactly enumerated uniform order-rank conditional expectations for N=3,4,5, recovering expected covariances 2,20/3,50/3 for centered arithmetic contrasts. The final RESULT.md has a form-feed character corrupting one displayed LaTex command in the sample specialization, but the intended identity is otherwise unambiguous.

## originality

FAIL

The complete centerpiece follows as an immediate linear-algebra corollary of the prior full-distribution single-pair correlation formula of Stuart (1954), explicitly reproduced as Eq. (2) by Maturi–Elsayigh (2009). Recover Cov(X_i,R_i) from their correlation; since rank sum is deterministic and pairs are exchangeable, the off-diagonal is −diag/(N−1). Hence the entire centered covariance operator is a scalar and every contrast/Mann–Whitney formula follows by one-line contraction; the claimed “all contrast directions” extension is already mathematically implied. No novel nontrivial structural ingredient survives the earlier theorem plus standard rank-variance identities. This is a scientific coverage rejection, not an access failure.

## value

FAIL

The object, contrasts, and Mann–Whitney comparison are naturally motivated, but the claimed universal contrast formula is entirely forced by the classical single-coordinate rank–value identity, exchangeability, and the deterministic rank sum. The uniform-parent extremum is the standard sharp Cauchy–Schwarz case. The purported contribution adds no unknown/non-implied invariant or motivated nonstandard lemma; it is a useful instructional corollary but does not meet the bar for a new mathematical finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
