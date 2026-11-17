---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

PASS. For independent continuous X_1,...,X_n, a record R_i has probability 1/i, an interior peak P_j has probability 1/3; indicators are independent for i<=j-2 by disjoint observation sets and for i>=j+2 by independence of unordered prefix values from its uniform rank permutation. At i=j-1,j,j+1 the exact joint probabilities are 1/[(j-1)(j+1)], 1/(j+1), and 0, respectively, yielding the three displayed covariances after subtracting 1/(3i). The column sum is 1/[3j(j-1)(j+1)] and telescoping gives (n-2)(n+1)/[12n(n-1)] for every n>=3. Independent exhaustive exact-rational enumeration of every entry for n=3,...,7 agreed. The all-n argument, not the finite enumeration, proves the result.

## originality

PASS

PASS only for the position-resolved kernel and its three-diagonal independence law. Ji (2023), following Carlitz–Scoville, supplies aggregate generating functions including interior peaks and record counts, so the displayed total-count covariance is prior-covered, not new. An aggregate bivariate enumerator has no position markers and does not determine individual (i,j) covariances. Resultary searches located record–excedance, record–fixed-point and cycle–peak kernels involving different event pairs, but no theorem establishing this exact record–peak matrix. Historical position-marked sources may exist.

## value

PASS

PASS. This is a natural, complete site-resolved cross-covariance for a global prefix-maximum process against local triple peaks, not a random small case. All distant indicator pairs are independent, the three adjacent signs differ, and exact cancellation yields a strictly positive order-j^-3 column covariance, revealing dependence that an aggregate result hides.

The dated certificate retains the supplied scientific assessment, sources and limitations.
