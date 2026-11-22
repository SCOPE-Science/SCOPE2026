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

# Reproduction

From a directory containing `check.py`, run `python3 check.py`. The Python-only implementation checks an explicitly independent branch-based implementation and a permutation-lookup implementation of the published nine-entry local rule for every prefix state through length four. It exhaustively partitions all \(81\) four-site states and checks the exact profiles \(\{3:1\},\{9:1\},\{27:1\},\{27:3\}\), the three return words and monodromies, the \(27\)-step identity on the four-site factor, and disjointness and coverage of the three \(27\)-orbits.

The executable finite calculation is small enough to inspect completely. The infinite-space topological conclusion requires the separate exact proof in RESULT.md: the three finite-factor orbits pull back to nonempty proper clopen invariant sets. No higher-dimensional claim, infinite orbit census, or external formal certification is made.
