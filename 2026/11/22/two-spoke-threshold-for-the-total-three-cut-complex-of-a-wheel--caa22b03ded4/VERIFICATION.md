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

Run `python3 wheel_fault_verifier.py` with Python 3.9 or later and no third-party packages. It creates the total three-cut complexes directly from independent triples of explicitly generated wheel graphs, then tests all pairs of missing spokes for each rim length six through twelve. For nonadjacent pairs, it checks the stated two-piece decomposition, the intersection complex, and mod-two reduced simplicial Betti ranks. The complete test has 266 cases and passed.

The file verifies finite models only. The proof of the uniform sphere theorem is the explicit classification of all relevant independent triples for arbitrary rim size; it does not infer an infinite assertion from a bounded computation. An independent audit has not been performed.
