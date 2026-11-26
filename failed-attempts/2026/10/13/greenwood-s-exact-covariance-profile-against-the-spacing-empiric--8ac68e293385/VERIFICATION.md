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

FAIL

RESULT.md:57 says the Pearson correlation is given at every allowed threshold. It is undefined at x=0 and m and also at the interior point (m,x)=(2,1): the two spacings sum to 1, so exactly one is at most 1/2 almost surely and F̂_2(1)=1/2 almost surely. Here both the covariance and CDF variance are zero, not a zero correlation. These are the only exceptions: writing t=x/m, if mt<1 the all-above configuration and an open configuration with one below are both possible; if mt>1 use all below and one above. For mt=1 and m≥3, open configurations with exactly one or exactly m−1 above give different counts. The covariance, sign classification, two variance formulas, and fixed-x limit formulas otherwise check. The uniform-simplex shift conditions D given D_1>t into te_1+(1−t)Y and gives E[G|D_1>t]=t²+2t(1−t)/m+2(1−t)²/(m+1); exchangeability and the complement give the stated result. The one- and two-coordinate tails and Dirichlet fourth moments give the variances. Expanding the log of (1−2x/m)^(m−1)/(1−x/m)^(2m−2) gives −x²/m+O(m^−2), while m³ Var(G_m)→4. The limiting CDF variance coefficient is positive for every x>0 since e^x−2x>0 and e^0−1=0. Fubini and ∫(1−F̂_m)=1 give zero area. `python3 /workspace/branches/independent_examples.py 3` confirmed the integrated unequal-threshold CDF kernel identity at 198 sampled pairs and the interior zero-variance exception. Finite replay only. The frozen checker tests nonnegativity, not strict positivity or whether correlation is defined.

## originality

FAIL

The central exact mixed profile and its crossover are explicitly given in two other indexed results in an equivalent exceedance form and in a strictly broader Dirichlet family. One also gives the joint Gaussian law with the matching covariance coefficients. The separately presented elementary variance and zero-area identities do not establish a substantive distinct remainder. This conclusion is based on the inspected formulas, not on dates or on inaccessible papers.

## value

FAIL

The exact mixed crossover is a natural and useful target, but already covered. The remainder is a marginal count variance from one- and two-coordinate simplex volumes, normalization of corresponding covariance coefficients, a fixed-sum integral identity, and a small degeneracy correction. None makes a separately motivated substantive claim surviving the comparison. Correcting the correlation domain alone would not create a valuable distinct result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
