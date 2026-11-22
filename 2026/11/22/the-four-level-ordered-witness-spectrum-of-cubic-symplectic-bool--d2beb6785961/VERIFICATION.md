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

# Reproduction and verification

Execute `python3 checker.py` with Python 3.8 or newer and no third-party dependencies. The script evaluates the actual Boolean form, rather than directly invoking the theorem's case-analysis formulas, and checks every ordered distinct nonzero pair and its complete witness set.

Expected standard-output markers:

```
EXACT_WITNESS_SPECTRUM_OK m=1 Q=4 n=32 hist={4: 330, 8: 384, 12: 210, 20: 6}
EXACT_WITNESS_SPECTRUM_OK m=2 Q=16 n=128 hist={16: 1506, 32: 13440, 48: 1050, 80: 6}
EXACT_WITNESS_SPECTRUM_OK m=3 Q=64 n=512 hist={64: 6210, 128: 249984, 192: 4410, 320: 6}
```

The enumeration tests three finite dimensions; it does not prove the formula for every \(m\). The full all-dimension argument in `RESULT.md` follows from explicit seed-polar supports, linear independence of two nonzero distinct symplectic functionals, and five disjoint types of pairs. The theorem covers all quadratic refinements and linear terms because the second polar is unchanged by those choices. An independent mathematical audit has not been performed.
