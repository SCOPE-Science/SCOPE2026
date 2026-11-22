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

# Reproducible exact checks

Run `python VERIFY.py` with the Python standard library. The script constructs the complete twenty-pair state graph from the Stern recurrence, proves its closure by finite exhaustive generation, checks strong connectivity by reverse reachability and aperiodicity using the initial self-loop, solves the exact rational stationary equations and compares all twenty weights, calculates each of the six gap frequencies using the full eight-offset table, and directly checks a finite initial index segment through \(2^{16}\). It returned:

```
CHECK_OK 20-state exact stationary law; six sharp gap values; 65537 indices
gap probabilities: 2:2/7, 3:1/7, 4:1/7, 5:2/7, 6:1/14, 8:1/14
```

The finite-state verifier is not a formal proof of natural density: that step additionally uses the explicit primitive uniform substitution and aligned-dyadic-block exhaustion proved in `RESULT.md`. Finite numerical tests do not establish statements for unbounded indices. Earlier exact enumeration of the zero-index set is credited; historical novelty has not been independently established. No independent mathematical audit or certification is represented.
