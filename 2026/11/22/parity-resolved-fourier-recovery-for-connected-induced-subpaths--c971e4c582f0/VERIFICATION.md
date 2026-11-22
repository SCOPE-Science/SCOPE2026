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

The `verify.py` file accompanying this result is a self-contained exact-integer check. It enumerates even- and odd-cardinality vertex intervals independently of the derived prefix-sign formulas. For every frequency at each path size from 2 through 13 it verifies equality of both expressions, then sums zero frequencies and compares the results with the binomial formulas. It checks the arithmetic singularity criteria up to 999 vertices using the independent two-square search.

Execute `python verify.py` with Python 3.10 or later. Its output ends in `PASS` on successful completion. The proof, not the finite tests, supplies the all-order result. No computer-assisted proof of the classical two-square theorem is attempted. No independent mathematical audit is represented as having been completed.
