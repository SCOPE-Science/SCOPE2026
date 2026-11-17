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

The accompanying `forest_fixed_verify.py` was executed with Python 3 and NetworkX. It generated finite tree automorphisms, closed their cyclic subgroups, and separately tested generated noncyclic groups. It compared invariant subsets of original independent sets with faces of orbit-conflict models, verified the models are forests, computed reduced simplicial homology over \(\mathbb F_2\) via boundary ranks, and checked reduced Lefschetz numbers and the integral orientation-sign prediction. The exact output is embedded as `forest_fixed_verify.out`.

The checker handled 282 cyclic tree cases and seven other generated-group cases, comparing 6269 orbit faces; all assertions completed. The calculation is finite corroboration, not a proof for all forests or subgroups. Proof obligations are handled in `RESULT.md`.

The proof does not provide an equivariant representation sphere model or a complete orbit-space classification. Independent audit has not been performed.
