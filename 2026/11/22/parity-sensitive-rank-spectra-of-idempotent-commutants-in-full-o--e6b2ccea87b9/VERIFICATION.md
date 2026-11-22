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

# Verification record

The delivered `checker.py` is a standalone standard-library Python program. It constructs all order-decreasing distance-preserving partial maps of each chain of size \(1\le n\le8\) as unique map tuples, recomputes both compositions with each partial identity, and accumulates a histogram by the rank of the second map. The resulting histograms agree coefficient-by-coefficient with the two parity formulas. The final output marker is `ORDER_DECREASING_REFLECTION_COMMUTANTS_OK`.

The all-size proof is not a finite case analysis: it uses a disjoint-path transfer for translations, a disjoint-pair transfer for reflections, and a finite binomial identity. The checker does not establish originality or replace a separate independent audit. Historical-priority searches were bounded and cannot prove absence from unindexed publications.
