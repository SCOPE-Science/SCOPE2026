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

# Verification of Gaussian leaf-corona collisions

Run `python CHECK.py` with Python 3 and the standard library. The exact checker enumerates every labeled core graph through four vertices and compares the limiting partition constant under each single-edge addition. It independently counts all strict uniform rankings for four small full graphs, including two three-core graphs. Its verified success line is `CORE_LEAF_CORONA_EXACT_PASS: graph_mono_k<=4, finite_cases=4`.

The proof of the all-dimensional asymptotic is the dominated-convergence corner argument in `RESULT.md`, not the finite checker. The corner scaling uses a fixed core and two independent isotropic objectives. Unindexed related results, growth of the core with the leaf count, and nonisotropic objectives are outside verified scope.
