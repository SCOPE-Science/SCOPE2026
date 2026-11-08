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
# Verification of the exact coarse-cell dynamical factor

The proof is in `RESULT.md`. Execute `python3 checks/checker.py` using Python 3 and SymPy. The checker performs exact integer counts, SymPy rational-arithmetic total-variation comparisons, full symbolic characteristic-polynomial comparisons, and exhaustive finite-range semigroup tests. All 132 tested \((q,b)\) pairs passed, and all indicated semigroup tests passed. These are finite checks, with no claim that numerical enumeration proves the infinite-parameter result. The proof separately establishes the uniform conditional cell law for every observation history and the Fourier-block decomposition for every finite integer pair. Distributional independence is only for equal-grid observations and only under Lebesgue-initialized externally selected schedules.
