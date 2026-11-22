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

## Reproduction

Run `python3 CHECK.py` with the standard Python 3 library; it verifies 399 exact one-step identities and the nontrivial rational two-cycle, its exact multiplier and a locally contracting branch point. The proof in `RESULT.md` establishes all positive prime periods without depending on enumeration. The original model is the piecewise quadratic map of arXiv:2103.14834v1, equation (2.2); the closest prior result is Rozikov–Usmonov (2020), Theorem 2 for its different one-cut map.

## Scope

The map may be discontinuous at either cut. The theorem applies only to cycles with all coordinates strictly inside the unit interval and off both cuts. No assertions about border cycles, global basins, or independent certification are made.
