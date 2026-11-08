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

The analytic proof separately checks (1) same-position clients cannot split between distinct facilities; (2) the crossed configuration always admits a strict improvement; (3) pooling and segregation conditions including equality boundaries; (4) minimum social cost across all allocations; and (5) the exact maximum welfare ratio across positive separation and opening-cost parameters. The proof applies to all integers \(m\ge1\) and all real \(C,d>0\).

The accompanying `verify.py`, running solely on Python's standard library with `fractions.Fraction`, enumerates all labeled strategy assignments for \(1\le m\le5\), at two building-cost values and boundary-sensitive distances. It independently computes every direct unilateral deviation, actual welfare, the minimum over all assignments, and worst equilibrium inefficiency. It reports 24,536 assignments and checks sharp fixed-size formulas through \(m=7\). It does not enumerate all parameter choices or prove statements beyond its tested range; these are covered by the mathematical proof.

Command: `python3 verify.py`.

No independent external audit has been performed.
