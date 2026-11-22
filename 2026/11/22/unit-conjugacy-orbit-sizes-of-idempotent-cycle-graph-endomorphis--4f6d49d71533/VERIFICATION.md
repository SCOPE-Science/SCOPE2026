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

The mathematical proof is in `RESULT.md`. The independent programmatic route used to check finite cases is `verify.py`: it directly generates all nearest-neighbor cycle maps, tests idempotence by function composition, computes all dihedral conjugates, then compares the exact orbit-rank spectrum with separate adjacency-walk dynamic programming. Complete dimensions \(4\le n\le16\) passed, including every orbit size (not just total counts). The exact output is included as `verify_output.txt`, ending with `CYCLE_ORBIT_CLASSIFICATION_VERIFIED`.

The finite computation cannot establish correctness for every \(n\), historical novelty, or statistical asymptotics. The general argument relies on the fixed-path retraction bijection, reflection midpoint condition, and orbit-stabilizer theorem; its exponential consequence additionally uses an elementary Fibonacci lower bound.
