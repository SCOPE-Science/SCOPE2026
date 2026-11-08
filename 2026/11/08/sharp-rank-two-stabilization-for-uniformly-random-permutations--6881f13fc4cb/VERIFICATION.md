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

# Verification
Run `python3 checker.py` from a directory containing the standalone file. The script uses only Python's standard library and exhaustively enumerates every permutation on one through eight points. It computes masks directly, compares them to independently constructed two-move quadrant types, checks the Stirling/record identity for at most two records, verifies the direct-sum-pivot upper bound, and tests the nine-point generic witness. Expected terminal line: `ALL_FINITE_CHECKS_OK`.

The infinite proof is in `RESULT.md`: it uses Ehrenfeucht--Fraïssé equivalence, record statistics, extremal-element union bounds, hypergeometric sampling and a factorial-moment Poisson limit. The checker is a finite consistency test and does not prove these infinite steps. The historical-priority comparison remains incomplete for the inaccessible 1990 chapter. Independent audit has not been performed.
