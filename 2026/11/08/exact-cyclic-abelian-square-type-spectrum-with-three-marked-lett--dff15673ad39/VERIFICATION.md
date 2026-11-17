---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

For every odd n>=3 and exactly three zeros, the proof reduces equal-half zero counts to j=0 or 1. For j=1, the chosen consecutive zero pair gives necessary-and-sufficient integer start bounds floor(g/2)+1<=m<=min(K,g+min(j,h)-1). After sorting a<=b<=c, the intermediate interval is contained in the small-gap interval; the large-gap interval reaches K. Their union and the longest all-ones run give N=K-1_{c even}+max(0,min(K,a+b-1,floor(c/2))-floor(a/2)). The sole even-c baseline deficit m=c/2 is compensated no later than m=c/2, proving EVERY prefix inequality, including n=3 and adjacent zero boundaries. A fresh independent enumerator compared exact types and all prefixes for 1,036 words of odd length 3..15. These finite checks corroborate but do not replace the interval proof.

## originality

PASS

The exact three-gap circular half-Parikh type formula and the full odd-length prefix inequalities are not consequences of the inspected 2026 general distinct-string bound, its two-run special case, the older weaker circular bound, or the published linear fixed-three-marker formulas. The motivating full article explicitly conjectures the prefix inequalities, and proves them only in narrower cases. No equivalent dominating result was identified in the targeted published searches. Priority is qualified by unindexed literature.

## value

PASS

This gives a motivated infinite subfamily of a recent explicitly open prefix-count conjecture, with a complete per-half-length type spectrum and closed three-gap formula, not a finite-table improvement. The distinction between circular and linear factors is structurally important; the result does not claim the unrestricted conjecture.

The dated certificate retains the supplied scientific assessment, sources and limitations.
