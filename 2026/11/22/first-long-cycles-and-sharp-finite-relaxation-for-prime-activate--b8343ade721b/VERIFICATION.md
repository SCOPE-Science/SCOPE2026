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
# Verification of finite classification

The provided code uses only integer and bitwise operations. It exhausts \(2^{\binom n2}\) labeled tournament encodings and all \(2^n\) Boolean initial conditions at each \(1\le n\le7\). No experiment on smaller graph samples is used to infer facts about larger graphs.

For each encoded tournament, `tournament_scan.cpp` detects cycles by stack-based successor following; `tournament_census.cpp` independently detects periodic states by repeated indegree-zero pruning and calculates each transient distance in reverse pruning order. Both produce identical maximum-period graph-count vectors. `tournament_extremes.cpp` independently exhausts all vertex relabelings of exactly those graphs attaining period nine and all graph–state pairs attaining first-entry depth 23. `tournament_witnesses.py` validates the exact listed cycles and longest transient from the recurrence itself.

The principal outputs at seven vertices are maximum period 9, maximum first-periodic-entry time 23, exactly 10080 labeled tournaments attaining period 9, two permutation classes each of size 5040, and 5040 extremal graph–state pairs in one permutation orbit. An explicit state path attains the transient maximum.

**Limits:** code execution and mathematical reasoning here provide a reproducible finite proof but do not constitute an independent mathematical audit; correctness beyond seven vertices is not claimed. Source/priority comparisons are subject to unindexed earlier calculations.
