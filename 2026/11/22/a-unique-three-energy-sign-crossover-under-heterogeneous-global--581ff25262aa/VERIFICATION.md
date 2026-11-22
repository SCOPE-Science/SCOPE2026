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

# Reproduction and limits

The complete proof and assumptions appear in `RESULT.md`. From the directory containing this file, run `python3 check.py` (only the Python standard library is needed) and `python3 symbolic_check.py` (requires SymPy).

The first script computes exact stationary moments from an independent Markov-generator subset recursion and compares their connected cumulants with the claimed closed expressions. It passed **6,082 exact-rational assertions** from 550 seeded heterogeneous parameter instances, pair covariance comparisons, permutation and balancing tests, and isotropic specializations. The second script directly factors the symbolic seven-term Laplace cumulant, verifies its isotropic limit, lower-bound polynomial and pair-smoothing identity, printing `PASS: 4 symbolic identities`.

All test files are complete and self-contained, with no external data or hidden dependency. Exact computational identities support the proof; finite case checks do not establish the universal parameter quantifiers. The universal sign, uniqueness, association and strict Schur ordering are proved in `RESULT.md`. No external auditor has independently validated the result or its publication priority.
