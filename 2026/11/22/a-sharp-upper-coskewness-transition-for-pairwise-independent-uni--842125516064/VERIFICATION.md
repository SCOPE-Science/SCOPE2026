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
The self-contained `check.py` uses Python's exact `fractions.Fraction` arithmetic and runs without external packages. Execute `python3 check.py`. Its recorded output is:

```
PASS: 1136 exact-rational conditions for 12 thresholds
```

The check exercises all ordered triples at each rational parameter, the two-coordinate Latin margins, the objective values of both attaining laws, complementary slackness, and the structure of tight constraints. For arbitrary real \(t>1\), correctness rests instead on the explicit symbolic dual inequalities and the exact margin-saturation proof in `RESULT.md`. Exhaustive testing of finitely many rational thresholds would not prove the universal claim. No independent audit or validation is asserted.
