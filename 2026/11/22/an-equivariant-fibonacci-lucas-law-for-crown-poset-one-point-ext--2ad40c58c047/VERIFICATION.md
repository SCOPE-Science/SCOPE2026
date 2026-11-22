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

The finite checker `verify.py` generates nonalgebraic types from ideal/filter pairs and the cycle's common-upper-neighbour incidence relation, then enumerates each symmetry orbit and each group-element fixed set directly for all \(5\le n\le9\). The actual output appears in `verification_output.txt`. Further divisibility checks cover the range \(5\le n\le50\). `verify.py` uses only Python's standard library and has no external dependencies. Reproduction command: `python3 verify.py`.

The mathematical assertions for all \(n\ge5\), including uniform reflection counts and the exponential generic-stabilizer law, rely on the explicit transfer-matrix/Burnside proof in `RESULT.md`, not on extrapolation from finite computations. First-public source date was checked against the 2025 arXiv submission record. A 2002 full-text comparison was not completed; historical priority and independent verification remain open.
