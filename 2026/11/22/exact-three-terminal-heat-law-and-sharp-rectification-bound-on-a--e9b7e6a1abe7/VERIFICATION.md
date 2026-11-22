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

The stationary moment equations follow directly from the finite-state generator and have the unique explicit solution in `RESULT.md`. The current formula follows by inserting these moments into the expected energy changes of individual flips. Strict positivity of the current conductances and the derivative test prove the three-terminal sign law and the sharp \(4/3\) rectification bound for all finite positive temperatures.

For independent finite checks, run `python3 verify.py` with SymPy. Its exact-rational state-space computation checks 125 parameter triples against direct stationary solutions (all eight microstates, three currents, three pair correlations), all stationarity residuals and state positivity, plus three rectification identities. Expected output:

```
EXACT_8_STATE_CHECKS_PASSED 125
RECTIFICATION_IDENTITIES_PASSED
```

Finite computation is a normalization and implementation check only, not an infinite parameter verification. The proof assumes precisely the heat-bath rates and sign convention in `RESULT.md`. No independent external mathematical audit has been performed.
