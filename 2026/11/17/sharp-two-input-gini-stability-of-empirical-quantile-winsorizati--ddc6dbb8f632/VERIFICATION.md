---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

PASS: Reconstructed sample rank clipping for real n-vectors and integer 1<=a<b<=n, strict order chamber coordinate-replication multiplicities a and n-b+1 (others singleton), and exact all-cut Gini norm. Verified nonstandard replication lemma: for any m_j>=n/2 choose S or its complement containing j, then mass phi(u)<=phi(m_j); otherwise all m_j<n/2 and choose cut side with u>=s, select j in S with m_j>=u/s and use phi monotonicity and the algebraic inequality n(s-1)(u/s-1)>=0 to bound arbitrary cuts by a singleton. Discrete coarea yields global bound and single-pivot rank perturbation attains max{a(n-a),(n-b+1)(b-1)}/(n-1). Pairwise one-input clipping contraction is distinct. Independently enumerated all integer replication multiplicity compositions of n for 2<=n<=7 (3,10,35,126,462,1716 compositions) and every nontrivial binary cut, all agreeing with the lemma; checked rank boundary formulas and trivial a=1,b=n. No inference from a finite test to all dimensions.

## originality

PASS

PASS (best of knowledge): primary Winsorized-statistic publications concern estimator bias, robust dispersion/control charts or distributional properties, not the deterministic two-input Gini seminorm of the entire coordinatewise clipping map. Rank rearrangement, two-cell averaging, and same-day morphological Gini results supply related cut methodology but do not imply this exact all-rank Winsorization coefficient from their stated theorems. Generic replication cut reduction is a methodological antecedent and not claimed novel; the sharp general replication single-column capacity lemma and its application to order-statistic clamping survive the checked comparisons.

## value

PASS

PASS: Empirical-quantile clipping is a standard robust-statistical preprocessing transformation. The exact finite-sample perturbation condition, the three nonexpansive rank-pair cases and linear n-amplification at a fixed trimming fraction identify a quantitatively important discrepancy between dispersion contraction and data-set sensitivity. Universally sharp exact fact with natural motivation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
