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

Run `python3 check_psl.py --catalog OPTIMIZERS.json` using a standard Python 3 interpreter in the directory containing both files. This performs exhaustive phase normalization, computes all twelve distinct nonzero autocorrelation shifts, evaluates scores in exact algebraic representations, confirms the seven sharp minima and all normalized-equality counts, then checks every entry of the supplied optimizer catalog. The successful final lines are:

```
HOLLOW_SQUARE_PSL_EXACT_PASS cases=61775
OPTIMIZER_CATALOG_EXACT_MATCH
```

The six-phase witness is additionally certified by direct integer correlation norms: the squared norms at displacements \((0,1)\) and \((1,0)\) vanish, and those at the other ten selected shifts are \(1\). The compulsory corner shift \((2,2)\) has squared norm \(1\) for every unimodular array.

The checker requires only Python's standard library, performs no network access and makes no floating-point decisions. Its q=7 comparison uses the rational interval \((1246979603717467,1246979603717468)/10^{15}\) for the unique root in \((1,2)\) of \(x^3+x^2-2x-1\), with inequalities proved by integer polynomial evaluations. The supporting manuscript proves why the finite case enumeration is exhaustive. The stored optimizer catalog is a consequence of the complete exact enumeration, not a collection of sampled candidates.

The classification is limited to the seven alphabet sizes \(2\) through \(8\) and to aperiodic correlations on the specified zero-centered support. Independent external mathematical review has not been performed.
