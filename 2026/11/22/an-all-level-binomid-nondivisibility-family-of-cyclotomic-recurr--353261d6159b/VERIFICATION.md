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

# Verification notes

The proof establishes the theorem for all positive integers \(q\ge2\), \(t\ge1\), all primes and every column width and binomial index. Critical formal steps are the exact periodic solution, the cancellation identity for a column's generalized coefficient, the 27-case mod-three count, and the sharp four-unit lower bound on the exponent \(ckm\) at the sole negative count. The explicit necessity witness is at original generalized-binomial entry \((4,2)\), and the nondivisibility witness is the index pair \((2,4)\).

Execute `python3 artifacts/check.py` in the directory containing this file. Only Python's standard library is required. The file `artifacts/check_output.txt` records the deterministic result of the performed computation. It constructs the recurrence using its defining iteration and evaluates generalized coefficients through exact rational products, across eight admissible parameter pairs, ten column widths, and complete checked triangles to row 31. It separately checks the full residue table and large representatives of the period reduction; four inadmissible parameter pairs show nonintegral base-level witnesses.

Finite checks neither prove all positive indices nor establish absence of earlier equivalent published theorems. The first is handled by the elementary infinite proof, and the second is assessed against the material actually inspected. External independent audit has not been performed.
