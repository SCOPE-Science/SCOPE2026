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

Two specified distinct domain points determine a unique signed affine extension; rank-one nonfixed maps are counted only as translations and the empty map only once. For shift d>0 the n-d domain positions split into b_d residue strings of length a_d and d-b_d of length a_d-1. A k-arrow path exists exactly at a selected k-run, and concatenating zero-terminated blocks and a final run yields the rational forbidden-run series. A nilpotent reflection omits fixed points and uses at most one point of each transposed pair, so each nonempty such restriction has index two. Its polynomial removes ranks zero and one to avoid duplication. The pair-count levels below floor(n/2) occur four times each for positive levels, with multiplicities one or three at the top; summing the binomial coefficients gives the stated parity formulas (n=1 directly gives only zero as nilpotent). The ambient order gives a limiting density, not an exact density, of 1/3. The non-translation contribution is O(3^(n/2)) while nonzero translations number 2^(n+1)-2n-2. Within translations the absolute shift has a uniformly geometric tail. At each fixed shift, a union bound over at most n starts rules out runs longer than (1+epsilon)log_2 n with high probability; at least n/(2r) disjoint length-r windows for r=floor((1-epsilon)log_2 n) make a shorter maximum improbable. Conditioning on nonempty domains does not affect this limit, and the index is one plus the maximum run. Independent bounded literal composition checked the joint counts, closed counts and ambient order through n=9. Replay: python3 /workspace/branches/87e35433-f3e4-0fba-83d6bdce1f8a/independent_census_check.py 9. Those checks do not establish the asymptotic claim on their own.

## originality

FAIL

A distinct Resultary record contains the equivalent joint census, parity rank counts, totals and limiting density in the full monoid. The remaining leading depth law is implied by an earlier sharper order-preserving result: the additional nilpotent reflections have vanishing weight, so the order-preserving law transfers in total variation. No substantive part of the finding survives these comparisons.

## value

FAIL

A rank-index census and a typical-depth theorem are meaningful for this monoid, but the census is already available and the depth statement is a weaker consequence of the stronger translation limit and the negligible reflection mass. No additional structural or quantitative result beyond the available claims is shown.

The dated certificate retains the supplied scientific assessment, sources and limitations.
