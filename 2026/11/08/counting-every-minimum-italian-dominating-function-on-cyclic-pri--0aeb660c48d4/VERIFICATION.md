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

The finite integer certificate is `artifacts/verify.py`, using only the Python 3 standard library. Replayed against the included program, it returned:

```text
ZERO_REDUCED_COST_GRAPH_OK states=81 edges=161 cyclic_SCC_sizes=12,4,2
EXACT_COMPONENT_DETERMINANTS_OK degree_10+4+2
TRACE_GENERATING_SERIES_FIRST_40_OK [6, 12, 10, 34, 42, 68, 132, 214, 330, 630]
INDEPENDENT_BRUTE_FORCE_OK 3 6
INDEPENDENT_BRUTE_FORCE_OK 4 12
INDEPENDENT_BRUTE_FORCE_OK 5 10
INDEPENDENT_BRUTE_FORCE_OK 6 34
CIRCULAR_BINARY_WITNESSES_OK n=3..40
VERIFY_OK
```

The mathematical proof reduces every cyclic length to 81 transfer states and the exact characteristic polynomials of its three cyclic components. This finite reduction, not extrapolation from the four directly enumerated prisms, supports the unrestricted formula. No independent audit was performed. The historical novelty assessment remains provisional despite inspection of the complete motivating preprint HTML and the directly applicable 2018 prism theorem, because older equivalent enumerations under alternate terminology may exist.
