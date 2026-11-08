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
# Verification

From a Python 3 environment with no external dependencies, run:

```
python verify_vertex.py
python verify_counts.py
python verify_ratio.py
```

`verify_vertex.py` independently constructs every edge of \(K_{n,n,n+1}\), updates every labelled bit by its actual neighbor majority, and checks all \(74,896\) labelled initial states for \(1\le n\le5\). It asserts eventual period at most two by update two, precisely two fixed states, the exact periodic-point count, and the all-size formula evaluated at each tested \(n\).

`verify_counts.py` independently implements the part-count evolution and the binomial-tail expression; the programs agree for all \(1\le n\le20\). The latter also prints exact basin probabilities at \(n=30,50,100,200\) and evaluates the claimed arcsine limits. `verify_ratio.py` checks a second imbalance regime on \(K_{n,n,2n}\) at five finite sizes. Captured standard output is provided in `verify_vertex.out`, `verify_counts.out` and `verify_ratio.out`.

The infinite-family arguments, case exhaustion and Gaussian limit are mathematical deductions in `RESULT.md`; these checks are finite corroboration, not external proof or independent validation. No conclusion about biased initialization, randomized tie breaking or all finite \(K_{n,n,m}\) basin populations is certified here.
