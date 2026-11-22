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

The theorem's all-length proof identifies the nearest admissible word with a maximum disjoint-occurrence packing, constructs an optimal substitution set, and enumerates all distances with a three-state weighted automaton. Running `python3 verify.py` reproduces the finite comparisons without dependencies.

The program tests every binary word through length fifteen against an independent Hamming-distance dynamic program, verifies a constructive optimum edit sequence, and checks full distance histograms. Coefficient recurrence and deep-hole identities are tested through length 180. Finite tests are not an infinite proof; the structural and generating-function arguments establish the universal claims. No independent audit has been performed.
