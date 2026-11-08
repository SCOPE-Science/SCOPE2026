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

Run `python3 artifacts/verify.py` in a Python 3 environment. Only the standard library is needed; no network access, datasets, or external files are required.

The program constructs all \(81\) ordered pairs of two-row column states, with transition constraints derived from the local conditions on white, yellow and black vertices. It computes forward reachability from the thirteen left-boundary states and reverse reachability to the thirteen right-boundary states. Their intersection contains exactly seven states, and the program checks their complete graph is one six-cycle and the all-black loop. The start/end phase constraints and six-period increment are checked independently using the edge selections induced by vertex colors.

A separate enumeration directly tests every edge subset of the open ladders for \(2\le n\le7\) against the defining predicate, and verifies the entire cardinality polynomial in these cases. This finite enumeration corroborates, but does not replace, the unrestricted finite-state proof: the latter uses exhaustive local state classification and finite-period arithmetic, not extrapolation from small ladder lengths.

Current limitations: the verifier is ordinary exact Python code, not a formal theorem prover, and no independent external mathematical audit has been performed. The first two cited publications supply foundational definitions and general algorithms; they are not presented as certificates of novelty.
