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

## Reproduction
Run `python checks/pentad_inverse.py` using Python 3 and its standard library. This checks exact rational inverses for four values of \(n\) and four nondegenerate samples at each size, plus invariance under diagonal torus rescaling and projective coordinate normalization. The expected final output lines are:

```
EXACT_RECOVERY_AND_TORUS_INVARIANCE_OK 16
CERTIFICATE_OK
```

## Evidence limits
The program is not an exhaustive test for all parameters and cannot establish rationality or generic uniqueness by computation alone. The formal proof is the algebraic elimination and normalization in `RESULT.md`; the verification program independently exercises the central equations at exact finite rational samples. The theorem is valid on a Zariski dense open over \(\mathbb C\), not on every boundary point. No independent audit has been performed.
