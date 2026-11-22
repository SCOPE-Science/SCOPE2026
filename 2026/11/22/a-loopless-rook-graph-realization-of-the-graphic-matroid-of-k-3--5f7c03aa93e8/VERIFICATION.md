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

The scientific proof in `RESULT.md` uses the explicit invertible affine map over the three-element field, all nine four-cycle neighborhoods, and the chord decomposition of each six-cycle of the complete bipartite graph. It proves equality of closure operators for every starting set and the count of bases via the spanning-tree formula. The proof is not contingent on finite testing.

`python verify.py` runs the original vertex-neighborhood forcing process independently of the union-find graphic-closure process, for all 512 initial subsets. It checks that exactly 81 five-element initial sets are forcing and no smaller sets force all vertices. Expected terminal line: `VERIFY_OK`.

Limitations: no classification of other nine-vertex realizations or of larger rook graphs, and no external independent audit. The source search assesses historical priority only provisionally.
