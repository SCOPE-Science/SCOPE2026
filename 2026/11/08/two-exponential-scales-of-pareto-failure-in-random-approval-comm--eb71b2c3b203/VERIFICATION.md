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

Run `python3 verify_pareto_rates.py` with a standard Python 3 interpreter. The file uses only the standard library, and the expected last line is `ALL EXACT CHECKS PASSED`.

The script exhaustively constructs all 56 oriented one-candidate and 420 oriented two-candidate comparisons on eight fair approval bits. Among distinct comparisons, the maximum overlap counts out of 256 rows are 160 for sizes \((1,1)\), 160 for \((1,2)\), and 152 for \((2,2)\). Those are complete single-voter enumerations because any pair of comparisons uses at most eight candidate coordinates. For each fixed \((m,k,n)\) in the finite test cases, the script independently computes Pareto domination by directly comparing committee utilities and by exchanging disjoint candidate subsets. It checks equality of the two definitions on all 14,336 profiles, tests the finite-\(n\) error bounds with exact fractions, and verifies the five-voter two-exchange witness without candidate containment.

The infinite-\(n\) result is an analytical consequence of the fixed finite overlap lemma, independent voter products, the exact binomial equality formula, Bonferroni bounds and a union bound. The program is not used to infer an unrestricted infinite conclusion from a partial enumeration. No external validation or independent audit has been performed.
