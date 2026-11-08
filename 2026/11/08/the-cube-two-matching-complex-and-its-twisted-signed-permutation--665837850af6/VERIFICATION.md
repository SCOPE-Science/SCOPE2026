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
# Reproducible verification

In a directory containing `verify.py` and `certificate.json`, run `python verify.py` with Python 3.10 or later. No additional Python packages are needed.

The script constructs the twelve cube edges from Hamming-distance-one pairs, compares two independent membership predicates on all 4,096 edge masks, recomputes the deterministic discrete-Morse pairs and critical cells, and verifies that all 7,980 covering relations produce an acyclic directed graph. It checks a second vertex ordering, independent sparse mod-two boundary ranks, and exact Lefschetz traces for 48 cube automorphisms. It recomputes all certificate bytes and fails if the embedded certificate is inconsistent.

The expected diagnostic is `Q3_TWO_MATCHING_WEDGE_THREE_S5_AND_SIGN_TWIST_CHARACTER_VERIFIED`, also present in `verification_output.txt`. The output file alone is not evidence of mathematical correctness: the actual reproducible checks are in the self-contained script and its certificate.

**Scope of computation:** exhaustive for this explicitly defined 12-edge graph and all 48 of its graph automorphisms. It is not a proof for other graphs, larger cubes, or integral equivariant structures. The scientific review is not an independent audit.
