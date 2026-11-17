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

# Verification guide

The mathematical proof is in `RESULT.md`. The central equalities are the connected-cut facet area \(A(F)=\sqrt{st}\tau(G[S])\tau(G[T])\), the centered support distance \(h(F)=k\sqrt{N/(st)}/2\), and the cactus spanning-tree product \(\tau(G)=\prod_C |C|\). Combining these with pyramid volume \(A(F)h(F)/d\) gives the exact claimed masses and full classification.

Run `python checks/cactus_cone_volume_check.py` under Python 3 with `networkx`, `sympy`, `numpy` and `scipy` available. It checks exact rational masses and edge-bond classification for eight explicit cactus graphs, plus five separate Euclidean convex-hull facet reconstructions. The expected last output line is `CACTUS_CONE_VOLUME_PASS`.

These finite checks cannot certify all cacti or historical originality. The unbounded claim rests on the written cut and determinant arguments. All Euclidean volumes use the unscaled standard graph-incidence segments and the centered hyperplane; translating the apex or rescaling edge weights changes the interpretation.
