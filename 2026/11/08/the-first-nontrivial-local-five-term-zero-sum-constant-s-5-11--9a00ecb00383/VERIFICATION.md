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
The full claimed statement concerns every length-eleven unit sequence modulo twenty-five. The reduction to \(364\) residue count profiles (and to \(286\) ten-term profiles) is a mathematically exhaustive reduction because there are four nonzero residue classes modulo five and every lift has unique fine digits in \(\mathbb F_5\).

`verify_zero_sum.py` reconstructs the affine equation system for every five-index set whose coarse residue sum vanishes, reduces each row modulo five, and reports all consistent ten-term profiles and eleven-term contradictions. `verify_zero_sum.cpp` reconstructs the same systems via bit masks with independently implemented modular elimination. The full output files are embedded and match actual executions. No floating-point arithmetic, sampling, hidden dataset or external network dependency is required.

Python output:
```
TEN_PROFILES_EXHAUSTED 286 SOLVABLE 12 RANK2 6 RANK8 6
ELEVEN_PROFILES_EXHAUSTED 364 DIRECT_CONSISTENT 0 DELETION_CONSISTENT 0
DIRECT_GAUSS_EQUATIONS_PROCESSED 19619
TEN_TERM_SHARPNESS_OK 2_ONLY_ZERO_MOD_25_FIVE_SUMS
VERIFY_OK exact_exhaustion=True independent_audit=False
```
C++ output:
```
CPP_TEN_PROFILES 286 CONSISTENT 12 RANK2 6 RANK8 6
CPP_ELEVEN_PROFILES 364 CONSISTENT 0 EQUATIONS 5029
CPP_VERIFY_OK exact_rank_exhaustion=True
```
The two programs process rows in different orders and may short-circuit an inconsistent system at different points; their counts of equations processed need not match. The complete twelve-profile list is written in `verification_output.txt`, reproduced in RESULT.md, and asserted in Python.

Scope: prime \(5\), exactly five selected indices; arbitrary integer lifts and arbitrary repetition. Independent mathematical audit remains unperformed. The accessible journal abstract is not a substitute for inspecting its inaccessible full body for priority.
