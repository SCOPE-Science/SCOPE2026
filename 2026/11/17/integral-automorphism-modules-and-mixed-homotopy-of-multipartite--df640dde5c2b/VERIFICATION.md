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

# Reproducible checks

Run `python3 gp_multipartite_check.py` using the Python 3 standard library only. The script performs graph-level breadth-first searches for all pairwise distances; enumerates vertex subsets and tests the actual geodesic-triple predicate; separately verifies the exact structural face classification; and constructs simplicial boundary matrices over \(\mathbb F_2\).

It checks 15 size profiles, 641 nonempty simplicial faces and 480 legal graph automorphisms, including swaps among equal-sized parts. For each action it computes the reduced signed Lefschetz trace from all oriented simplices and compares it with the character predicted by the integral augmentation-module statement. The final stdout marker is `GP_MULTIPARTITE_INTEGRAL_MODEL_CHECK_PASS cases=15 faces=641 actions=480`. Complete recorded stdout is in `gp_multipartite_check.out`.

**Limitations.** Mod-two homology alone does not prove integral torsion-freeness, and 480 finite group actions are not an exhaustive check for arbitrary parameters. The proof of integrality and the formula for all automorphisms use long exact sequences and join signs in `RESULT.md`. The script was replayed in its package location and the recorded stdout compared byte-for-byte.
