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

`verify.py` is a standalone standard-library Python 3 program. Execute `python verify.py` from this directory.

The checker constructs the actual length-\(n\) factors from the \(a+b\) cyclic starts, computes overlapping counts of every letter and digram directly, and partitions signatures by exact tuple equality. It compares the resulting class count with the formula for all \(1\leq a,b\leq14\) and all \(1\leq n\leq2(a+b)+4\), totaling 6,664 factor-length cases. For each of the 196 parameter pairs, it also checks the maximum over one residue period and the claimed phase-identifiability criterion.

The observed output is `PASS: 6664 factor-length profiles and 196 peak/threshold configurations`.

The infinite assertions are established by the period-reduction and run-classification proof in `RESULT.md`. Finite checks are not presented as exhaustive verification for unbounded parameters. There is no independent scientific audit.
