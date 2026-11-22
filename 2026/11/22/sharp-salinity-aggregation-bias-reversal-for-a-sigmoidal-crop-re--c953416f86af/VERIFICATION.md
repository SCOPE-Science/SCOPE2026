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

The exact identity for the area-aggregation bias, the increasing positive/negative ratio, endpoint Jensen inequalities, and the cubic two-class factorization are written in `RESULT.md`. These prove the claim for the full stated domain without reliance on finite computation.

To run supplementary checks using ordinary Python 3, execute `python3 checker.py` from this directory. The seeded assertions cover multiple sample sizes, dispersed salinity classes, response exponents on either side of one, explicit symmetric cubic thresholds, strict sign tests and a numerical illustration. Floating-point checks are diagnostics rather than formal, exhaustive or independent validation.

The original 1993 crop-response article was inspected in full via its lawful author-hosted copy; published spatial aggregation literature and a general variation-diminishing result were compared. A relevant 2015 aggregation paper was accessible principally through its abstract, and an equivalent theorem in uninspected literature cannot be excluded.
