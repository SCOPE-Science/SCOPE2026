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

# Reproducibility

Run `python3 verify.py` using Python 3.9 or later with only the standard library. This enumerates every vertex and literal irredundant edge in \(\mathbb F_2^n\) for \(3\le n\le8\), direct products with heterogeneous residue sizes \((2,3,4)\), \((2,2,3,2)\), \((2,3,2,4)\), and the nonreduced ring \((\mathbb Z/4\mathbb Z)\times\mathbb F_3\times\mathbb F_2\). For each enumerated vertex it compares its **actual** incidence degree with the claimed formula, and it checks the independently established total-edge identity as a cross-check rather than as a novel assertion. The arithmetical maximum-degree formula is checked for \(3\le n\le30\).

The exact expected output is included in `verification_output.txt`. A successful run terminates with `VERIFY_OK`. The direct enumeration covers only the stated finite cases, and the separate maximum-mode enumeration covers only the thirty-factor cutoff. The all-dimensional theorem is proved in `RESULT.md` through monotone inequalities. This is a same-model mathematical and computational review, not independent certification.
