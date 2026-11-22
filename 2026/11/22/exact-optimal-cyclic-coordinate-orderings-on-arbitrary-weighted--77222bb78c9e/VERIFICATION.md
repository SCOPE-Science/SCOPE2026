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

# Verification record

Run `python verify_cycle.py` with Python 3, NumPy and SymPy. It prints `ALL_TESTS_PASS` if its checks succeed. Executed successfully with the supplied script.

The verifier separately computes four exact weighted-cycle characteristic-determinant identities (heterogeneous five- and seven-vertex systems, two coordinate orders each), two exact characteristic polynomials on a homogeneous five-cycle, and sign changes at four rational root-bracket endpoints. It also explicitly composes Gauss–Seidel single-coordinate update matrices and computes spectra over **all 120 permutations** of a heterogeneous five-cycle and **all 5040 permutations** of a heterogeneous seven-cycle. Each cycle's rates agree within floating precision inside a fixed ascent class; the ascent-imbalance classes are strictly ordered. The exact counts of optimal schedules are 110 and 4228 respectively.

The mathematical proof in RESULT.md, not the finite tests, establishes the general result for every odd dimension and all positive edge weights consistent with positive definiteness. Finite eigenvalue calculations alone would not establish that conclusion. Literature coverage and historical publication priority remain subject to the limitations recorded in REVIEW.md.
