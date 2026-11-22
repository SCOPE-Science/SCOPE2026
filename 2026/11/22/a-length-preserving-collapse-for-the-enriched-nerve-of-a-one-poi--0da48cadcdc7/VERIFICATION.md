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

# Verification of the claimed point-gluing homotopy equivalence

The proof gives a complete finite acyclic matching for each cutoff: select the first change between distinct nonbasepoint factors, then insert or delete the common basepoint directly at that switch. Exact cross-distance factorization preserves the length of every matched pair. The selected lower cell occurs as a unique regular face of its upper cell. Every possible alternating path that continues from an upper paired cell to another lower paired cell strictly decreases its nonbasepoint count; therefore no gradient cycle is possible. The critical cells form the union of the factor nerves, a genuine simplicial subcomplex. Positive off-diagonal distances ensure every cutoff has finitely many nondegenerate cells.

The accompanying dependency-free Python 3 checker independently enumerates tuples, the full directed normalized-face incidence graph, and mod-two boundary ranks. It passed 76 finite parameter instances and 2521 enumerated cells, including asymmetric quasi-metrics, randomized directed shortest-path metrics and two four-cycle summands. Run `python3 check_glued_nerve.py`. The machine experiment does not establish the infinite family; the explicit proof supplies that argument.

The first motivating source is arXiv:2601.03685v1, publicly available on 7 January 2026, primary MSC 55N31. It studies a distinct form of persistence varying finite metric spaces through isometries. The present theorem concerns the scale-indexed **blurred magnitude** simplicial nerve of a fixed pointed metric wedge; the difference is scientifically material. The 2018 ordinary diameter-VR wedge theorem and fixed-length magnitude homology Mayer–Vietoris results are also distinct. No independent validation or exhaustive publication-priority verification has been performed.
