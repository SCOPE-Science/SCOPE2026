---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproduction and limits

Run `python CHECK.py` with Python 3, using only its standard library. The code generates all eligible attachment histories for several small clique sizes, constructs adjacency sets directly, and computes exact degree moments and common-face counts as rational numbers. It then checks the mathematical formulas independently and tests strict signs for additional finite parameter ranges, plus a numerical limiting-correlation check. The recorded successful run returned `PASS: 2645 independent exact or numerical assertions`.

The checker does not prove an infinite statement; the independent argument in `RESULT.md` establishes the precise general recurrences, the strict negative forcing condition and the gamma-product asymptotics. The historical originality comparison examines Gao's full accessible draft and the same-process Darrasse–Hwang–Bodini–Soria paper and the distinct Panholzer–Seitz model, with additional search evidence detailed in `AUDIT.json`. No independent external mathematical validation has been performed.
