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

The standalone `CHECK.py` uses only exact integer and rational arithmetic. Run `python3 CHECK.py`; the final line must be `CHECK_OK orders=8..17 sets=8512 affine_orbits=122 strict_minimum_all_orders=1`.

Checks performed: all \(8{,}512\) subsets are partitioned into \(122\) invertible-affine orbits, each orbit representative receives a rigorous Fourier-sum interval, and the unique proposed minimizing orbit has its upper endpoint below every other lower endpoint. Trigonometric enclosures derive from rational brackets for \(\pi\), the degree-36 cosine expansion with analytic remainder, and exact integer square roots. The graph formula is inherited from the cited bipartite identity. The script establishes only orders \(8\) through \(17\); no external independent audit or higher-order verification has been performed.
