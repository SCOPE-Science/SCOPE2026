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

# Verification and reproducibility

The standalone finite checker is a Python 3 standard-library script supplied at `VERIFY.py`; run it next to this file with `python3 VERIFY.py`. The expected complete deterministic output is included in `checks.txt`, ending in:

`CLOSED_ROOK_ALL_FINITE_TESTS_PASS boards 21 individual_support_decisions 144135 size_counts {1: 266, 2: 2506, 3: 19254, 4: 122109}`

For all integers \(1\le m\le n\le6\), the program iterates every selected cell support of cardinality one through four; it builds each possible center's closed row–column cross and records all Boolean trace masks. Independently it classifies the support's selected-edge bipartite graph by degree, number of occupied rows and columns, and component shape. The observed truth values agree for each support, and the aggregate counts agree with the symbolic polynomial. The published homogeneous \(4\times4\) coefficient list is checked separately. The script does not decide any unbounded case: the universal proof is the four-step argument in RESULT.md.

Scientific limitations: The coefficient theorem is for full rectangular graphs and inclusive radius-one balls only. Previously published equal-side results and dimension-only facts are not independently re-proved as novel. Literature indexing and independent third-party audit remain incomplete.
