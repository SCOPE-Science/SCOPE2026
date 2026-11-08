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

# Reproducibility and verification

The finite-state verification uses the standalone `verify.py` file in the same package. Reproduce with Python 3, NumPy and SymPy installed by running `python verify.py`.

The program constructs explicit labeled complete rooted trees, computes the greedy two-offer transition matrix, and solves the associated root-hitting time system numerically for nine branching/height instances. It independently computes exact finite-deadline Bellman-optimal hitting probabilities for all labeled non-root states for twelve deadlines, comparing them with the fixed parent-first policy; the equality is tested using exact rational arithmetic. A distinct tridiagonal absorbing-chain calculation evaluates the hitting-time generating function and compares it at two rational arguments per instance to the closed continued fraction, again exactly. The total is 2,538 exact state/deadline and PGF checks. Further large-height moment/cycle-constant comparisons are numerical/asymptotic consistency tests.

The infinite-height central limit theorem and exponential limit are proved analytically in `RESULT.md`: the latter is not deduced from finite simulation or finite-horizon enumeration. No formal proof assistant or independent review is claimed. The checks do not establish historical priority.

Self-review completed; independent audit not performed.
