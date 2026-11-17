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

The attached `verify_capped.py` is a complete finite-state certificate of the universal equality \(F^{19}=F^7\), the eventual least-period possibilities, their 2187-signature classification, the twelve-cycle size threshold and the three-cycle signature set. It uses exact integer operations and exhausts **all** formal input signatures of the quotient; unrealizable signatures do not weaken the implication.

The separate `verify_vertices.py` applies the original rule to **individually labelled vertices**, without using the truncated-state transition. It exhausts the entire state space for \(K_{1,1,1}\), \(K_{1,1,6}\), \(K_{1,2,6}\), \(K_{1,3,4}\), \(K_{1,4,4}\), \(K_{1,4,5}\), and \(K_{1,5,5}\), with sizes up to \(177147\) configurations, checking period attraction, first entry and the exact period-three count. The independent `verify_weighted.py` recomputes basin counts from explicit multinomial sums for larger dimensions.

Each program requires only Python's standard library. Run from the directory containing these scripts using `python verify_capped.py`, `python verify_vertices.py`, and `python verify_weighted.py`. Their captured outputs are `verify_capped.out`, `verify_vertices.out`, and `verify_weighted.out`. Finite vertex-level examples corroborate but do not by themselves establish the infinite-size theorem: that theorem rests on the exact quotient and its complete finite enumeration. The historical-priority comparison is qualified by inaccessible full-text material; no external independent validation is asserted.
