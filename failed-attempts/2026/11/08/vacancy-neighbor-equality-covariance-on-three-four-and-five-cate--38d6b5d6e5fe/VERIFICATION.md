---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-19.md",
      "INDEPENDENT_AUDIT_2026-11-19.json"
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

For each r>=3 and n>=0, B_r(n)=binom(n+r-1,r-1) counts the exact uniform weak-composition sample. Z has expectation r B_{r-1}(n)/B_r(n). If H_r(n)=sum_{j=0}^{floor(n/2)}B_{r-2}(n-2j), the neighboring equal-pair mean is r H_r(n)/B_r(n). The r cyclic edges each have two marked adjacent vacancy indices, contributing 2 B_{r-2}, and r-2 other indices each contributing H_{r-1}, so E[ZE]=r(2B_{r-2}+(r-2)H_{r-1})/B_r. Subtracting means proves the exact general formula, including r=3, n=0 and n=1. Explicit parity expansions for H_2,...,H_5 in RESULT.md reproduce the six displayed rational expressions. A separately written exhaustive enumerator checked cyclic and linear covariances for r=3,4,5 and n=0..14; the general published all-k coefficient identity was independently specialized and checked against the six expressions for r=3,4,5 and n=0..500 (1593 exact comparisons in all). The universal proof rests on exact counting and algebra, not finite extrapolation. Seven real source blobs and the Git tree were inspected; the independent Git-tree hash reconstructed to the assigned f4fc205359ed8462f6f991c6a4b94f7b06f2c035.

## originality

FAIL

Decisive stronger prior coverage. Write n for the nonnegative total and r for the number of labeled coordinates. Adding one to every coordinate maps the submitted uniform weak compositions to the uniform positive compositions of N=n+r into k=r parts used by the published October 25 theorem. The vacancy count Z becomes its unit-part count U. For each i, the indicator of equal neighboring coordinates is unchanged. Since the law is exchangeable and Z is permutation-invariant, Cov(Z,1{X_i=X_j}) is the same for every pair of distinct coordinates, including the closing edge (r,1). Thus the covariance with the r cyclic edges is exactly r/(r-1) times the prior covariance with its r-1 linear edges, for every n>=0 and r>=3. This is an immediate implication of the published all-k exact coefficient identity, not merely matching qualitative signs. With m=n and D=binom(n+r-1,r-1), the previous theorem gives Cov(Z,E_cycle) = 2r * ((r-3)*h_{n-2}^{(r)}-h_{n-3}^{(r)})/((n+r-1)*D), where h_j^{(r)}=[z^j](1-z)^(-(r-3))(1-z^2)^(-2). For r=3,4,5 the coefficient evaluations reproduce all six submitted rational formulas exactly. The older record labels its date October 25, 2026 and its GitHub content was modified on November 1, preceding the submitted November 8 record. Hence no originality of the stated result survives; a mere change from a path to a cycle adds only one exchangeable edge. The published predecessor was inspected in full, not inferred from a title or abstract.

## value

FAIL

The cyclic vacancy/equality covariance is a naturally interpretable statistic, but its complete six-case rational formula and phase behavior are straightforward reindexings and constant multiples of an already published all-k positive-composition covariance theorem. The new circular edge introduces no additional dependence structure because the vacancy statistic and the underlying law are exchangeable; every distinct unordered pair has the same mixed covariance. Consequently there is no independently useful new mathematical invariant, boundary or structural method after excluding covered content. A simpler presentation does not rescue scientific value as an original research result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
