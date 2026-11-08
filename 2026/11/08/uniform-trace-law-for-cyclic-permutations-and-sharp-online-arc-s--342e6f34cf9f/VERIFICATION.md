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

The result has a universal combinatorial proof. The included standard-library Python checker independently enumerates all directed Hamiltonian cycles for each integer \(3\le n\le6\). It constructs all supports contained in at least one directed Hamiltonian cycle, so any support not enumerated has an unrealizable all-one labeling and cannot be shattered. For every enumerated support and every possible trace, the program compares actual counts with inclusion-exclusion. It also checks nonshattering at the top two degrees and all stated polynomial coefficients.

Run: `python3 check_cyclic_permutations.py`.

Successful output ends with `CYCLIC_PERMUTATION_ARC_TRACE_PASS`. Exhaustively checked candidate support totals at \(n=3,4,5,6\) are respectively \(15,79,525,4171\), with class sizes \(2,6,24,120\). Tests do not validate arbitrary \(n\); the proof supplies that generality. Public-date and source checks concern the listed references, not a claim of exhaustive historical priority. No independent audit is available.
