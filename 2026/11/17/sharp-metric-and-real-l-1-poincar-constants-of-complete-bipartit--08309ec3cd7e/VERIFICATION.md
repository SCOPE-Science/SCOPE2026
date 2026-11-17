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

# Verification
The sharp metric inequality follows from triangle inequalities averaged over the opposite bipartition. The real \(L^1\) bound follows from layer-cake integration and the exact polynomial identity in `RESULT.md`. For \(a\ge b\ge2\), each optimizer stratum is obtained by checking equality at each step, so no numerical extrapolation is required.

Run the standalone `check_biclique_cuts.py` with Python 3 to reproduce exhaustive exact-rational finite diagnostics for all \(2\le b\le a\le13\). These diagnostics also check the equality-stratum description and that the metric constant is not smaller than the real \(L^1\) constant. The proof is independent of their finite range.

The earliest qualifying source was submitted on 3 November 2026. The independent audit is not performed. Priority remains subject to specialist literature checking, especially equivalent edge-isoperimetric formulations.
