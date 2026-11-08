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

Run `python3 checker.py` with Python 3.10 or later; the implementation uses only the standard library. The executable is self-contained and reads no external inputs.

It enumerates each binary approval matrix for five finite instances: \((n,m,k)=(3,3,2),(4,3,2),(4,4,2),(5,3,2),(6,3,3)\). These contain \(512+4096+65536+32768+262144=365056\) profiles. The program computes the true DR count, quota candidate count, and pair obstruction event; verifies that a count mismatch entails the obstruction; and verifies the exact rational probability bound under independent fair approvals.

For the first two cases (\(4608\) profiles), a separate implementation directly enumerates *all cohesive groups of voters*, without using the uncovered-voter characterization, and checks identical DR counts. An additional weighted enumeration for \((4,3,2)\) at \(p=1/3\) verifies the bound with the true nonuniform profile probabilities. The program also evaluates critical-window constants and verifies convergence of several finite binomial local masses to their stated analytic leading term.

All assertions passed in the executed checker. The finite enumerations do not prove the results for unbounded \(n\); the infinite statements depend on the complete proof in `RESULT.md`, including the rare-event coupling and the binomial local central limit theorem. No independent scientific audit was performed.
