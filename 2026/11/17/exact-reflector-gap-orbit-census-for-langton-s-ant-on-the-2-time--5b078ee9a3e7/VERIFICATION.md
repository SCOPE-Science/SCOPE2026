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
# Verification of the exact orbit census

The two accompanying standalone programs were run with their supplied code and outputs. Compile `verification/direct_census.cpp` with `c++ -std=c++17 -O2` and execute; it checks all labelled full states for \(2\le n\le9\), exact cycle counts, permutation closures, and the full state checksum. The largest test has \(18,874,368\) full states. Run `python3 verification/column_invariant.py` to test the separate macrostep derivation on every vertical-heading state for \(2\le n\le7\), including the invariant and reflector direction rule. Standard Python is sufficient.

The full proofs of the invariant, exact return periods, lifted-state counts, and the limiting period law are in `RESULT.md`. Finite checks do not prove arbitrary width; their role is reproducibility and detection of implementation or algebraic errors. Counts are for labelled states, not spatial symmetry classes. No independent mathematical audit has been performed.
