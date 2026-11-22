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

The symbolic derivation and the critical point count are included in `RESULT.md`; all asymptotic statements follow from analytic variation estimates rather than sampling. The independent-from-the-proof finite diagnostic implementation `inverse_count_verify.py` uses only the Python standard library. Running it with Python 3 yielded:

```
case b=1.3, V=0.7, phase-target=0.2: [(20, 107), (40, 425), (80, 1686), (160, 6747)]; coefficient=0.26343508
case b=1.3, V=0.7, phase-target=1.0: [(20, 53), (40, 212), (80, 843), (160, 3374)]; coefficient=0.13171754
case b=0.8, V=-1.1, phase-target=0.0: [(20, 68), (40, 260), (80, 1040), (160, 4148)]; coefficient=0.16211389
COSINE_MEMRISTOR_INVERSE_VERIFY_OK
```

These computations are finite consistency checks only. They do not certify all parameters, all targets, or the \(R\to\infty\) limit; the proof in `RESULT.md` establishes those statements. The target and parameter ranges, one-step-only scope, possible literature duplication and lack of independent external audit are explicit limitations.
