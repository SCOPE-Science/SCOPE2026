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

`artifacts/verify_chvatal_hom.py` and `artifacts/collapse_pairs.json` are standalone, self-contained, Python-standard-library-only reproductions of all finite claims. Run `python3 artifacts/verify_chvatal_hom.py`; the captured successful output is included as `artifacts/verification_output.json`.

The direct independent-set-of-neighborhoods enumerator and the single-valued closed-walk expansion enumerator agree on the identical 1,500 CW cells. The executable checks all 280 proposed free-face collapses, proves the remaining one-skeleton connected, verifies the 61-dimensional cycle lattice, exhaustively enumerates the eight target automorphisms and verifies all five rational character values.

The certificate is exhaustive for this finite model; it does not prove a theorem for other target graphs, source cycle lengths, or integral dihedral representation decompositions. Only self-review has occurred. No independent mathematical audit or validation is asserted.
