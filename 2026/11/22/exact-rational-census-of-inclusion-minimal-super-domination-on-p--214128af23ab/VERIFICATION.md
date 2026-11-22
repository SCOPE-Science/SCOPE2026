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

Run `python3 verify_path_census.py` with standard-library Python 3. The checker constructs the same 9-letter local acceptance rule as the proof, evaluates exact integer suffix-state vectors, and confirms the 111-state vector identity at index 18. Its fixed transition extends that identity to arbitrary path length, as shown in RESULT.md. The program also checks initial coefficients and the recurrence through index 74. A second, separately implemented graph-level predicate exhaustively enumerates all subsets for \(0\leq n\leq15\) and checks the super-domination and inclusion-minimality definitions.

The finite direct enumeration is **not** an infinite proof; the propagation of the all-state equality is the unrestricted certificate. Full historical priority and independent audit have not been established.
