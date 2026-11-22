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

The claim is established by the proof in `RESULT.md`, not by finite computations. The exact six-pair polynomial, the equality condition for outer links, the strictly increasing root function, endpoint comparisons, and the two asymptotic expansions can be checked algebraically from the displayed definitions.

A standalone Python 3 program, `checker.py`, independently enumerates all eight link-operation states, evaluates the six-pair score, solves the one-variable root by bisection, compares it with many nonsymmetric feasible allocations, and checks special cases and asymptotics. Running `python3 checker.py` from the extracted file directory returned `PASS 40071 supplementary assertions`.

These numerical assertions do not certify the continuum of possible budgets and allocations or establish originality. No independent external validation has occurred. Full text was inspected for the open 2021 ecological connectivity preprint and the accessible 1962 reliability-allocation paper; the 2006 general reliability paper remained an abstract-only comparison, as disclosed in the review.
