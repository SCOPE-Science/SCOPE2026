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

The embedded `verify_cyclic_windows.py` implements the standard exact recursive Littlestone rank for all two-label point queries, independently from the proposed closed formula. For each tested parameter pair it checks the formula, the explicit balanced adaptive-tree witness, the one- and two-point shattering counts, and for small cycles the three-point obstruction. It also tests tree construction on larger cycles.

Run `python verify_cyclic_windows.py` using Python 3 with no dependencies. The expected final output is recorded in `verification_output.txt`.

The general cyclic-block lemma and the rank upper bound are proven in `RESULT.md`; computational tests of finitely many cycle sizes do not prove the all-size theorem. The ultraproduct statement uses the standard Shelah 2-rank/stability correspondence and Łoś's theorem; no finite test is presented as an ultraproduct computation. Independent audit: not performed.
