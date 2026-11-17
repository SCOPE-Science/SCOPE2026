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
The public standalone `verify_marker.py` uses only the Python 3 standard library. Execute `python verify_marker.py` to check exact finite indicator-language counts for lengths one through sixteen, exact indicator minimal-forbidden patterns at those lengths, and periodic-point counts over four- and six-letter alphabets at periods one through six. Expected final line:

```
VERIFY_OK indicator_languages=16 indicator_minimal_layers=16 fixed_period_censuses=12
```

The mathematical proof, not the finite enumeration, establishes the universal claims for arbitrary \(q\), length, and period. The symbolic calculations use an indicator projection that retains independent \(q\)-fold color choices at each coordinate. Independent audit and validation are not performed; historical-priority assessment is provisional.
