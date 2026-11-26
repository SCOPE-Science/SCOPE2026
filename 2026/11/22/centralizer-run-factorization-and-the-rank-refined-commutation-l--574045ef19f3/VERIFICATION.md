---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

Re-audited the complete replacement RESULT.md and associated scientific wording. For shift-minus-one maps both products shift by minus two; comparison of composite domains gives a_i b_{i−1}=b_i a_{i−1} with no omitted boundary condition. At every position the paired bits form one of four symbols; any adjacent unequal nonzero symbols are forbidden and 00 separates runs. The disjoint first-block decomposition is G=1+zG+Q(1+zG), with constant term one, and at x=y=1 the resulting recurrence has initials 1,4. This proves the stated ranks, total and probability equivalent. In the established individual factorization the exponent at y=1 is s+d−f, where f counts the adjacent zeros. The internal gaps cost at least s−1, with equality exactly when internal gaps are singletons and boundary gaps empty; positive compositions of r into d+1 parts count all such maximizers. If d≥r this equality is impossible, and a boundary block with f=s=1 attains the next exponent d. The full-rank, empty-word and one-position cases check. The proof covers arbitrary lengths; a separate finite direct-map check agreed through N=6. The uploaded verify.py and stored VERIFY_OK output were inspected but not executed; the unchanged optional replay is python3 verify.py from the package directory. Source evidence was preserved.

## originality

PASS

This PASS is for the narrowed finding only. The original claim's standalone per-support rank factorization is mathematically correct but directly covered by the classical initial-segment to terminal-segment theorem; its scope difference from an ambient rank polynomial alone does not avoid that implication. The replacement explicitly treats it as prior specialization and credits the source, leaving the joint two-rank census and fixed-rank sharp extremal result. Those require a different bivariate aggregate and an optimization over spatial gaps, and are not given by the inspected stronger centralizer descriptions or exact tables.

## value

PASS

The two retained findings answer complementary natural questions about the same rank-stratified ideal-generator family: how many ordered commuting pairs each pair of ranks allows, and how large an individual restricted neighborhood can be at prescribed rank. The rational series works across arbitrary lengths and rank strata, while the sharp transition and its dense-regime equality configuration are not generator-cardinality calculations. The individual factorization provides background but is not relied on as a separate contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
