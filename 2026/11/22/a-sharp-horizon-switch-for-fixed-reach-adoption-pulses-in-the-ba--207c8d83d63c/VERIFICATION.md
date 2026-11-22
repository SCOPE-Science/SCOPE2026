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

# Verification of the fixed-reach Bass pulse theorem

This package includes `verify.py`, executable directly with Python 3 and no third-party modules:

```bash
python3 verify.py
```

The checker uses exact `fractions.Fraction` arithmetic to verify the independent projective Bass-flow formulas, the exact parameter witness, endpoint tie and saturation boundaries, algebraic difference identity, and inequalities at rational interior time factors. It tests 12,000 deterministic rational parameter quadruples and five within-horizon pulse times, including deliberately selected tie and cap cases. It also tests strict early optimality for proportional remaining-market pulses and reports the exact assertion count. The general theorem is analytically proved in `RESULT.md`; no finite checker establishes it on an infinite parameter domain.

The checker was replayed from the bundled source file. Scientific limitations: the theorem assumes an instantaneous deterministic pulse, constant positive Bass rates, fixed market capacity, no attrition, and a terminal adoption objective. No independent audit has been performed.
