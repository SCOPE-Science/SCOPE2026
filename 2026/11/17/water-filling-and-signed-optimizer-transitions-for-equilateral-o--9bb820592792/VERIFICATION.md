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

The proof is analytical and covers arbitrary integers \(n\ge2\) and all admissible positive real radius vectors. `checker.py` performs exact rational calculations of the ordered-prefix optimum and the negative-part screening inequality; it independently constructs all nonconstant Boolean Lipschitz potentials and uses SciPy HiGHS linear programming to optimize the unrestricted signed coefficient problem. Verification in the present environment produced:

```
EQUILATERAL_NONUNIFORM_ONE_POINT_EXACT_AND_INDEPENDENT_LP_PASS profiles=60
THREE_PHASE_EXAMPLES_AND_NEGATIVE_COEFFICIENT_WITNESS_PASS
```

Run with `python checker.py` from the directory containing that file. Python 3 and SciPy are required for the LP comparison. Sixty rational profiles with \(2\le n\le6\) were tested; exact rational tests also verify examples at and on both sides of the norm-one threshold. Finite testing cannot establish the full real-parameter theorem or its historical originality. No independent audit has been performed.
