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

# Verification information

`check.py` is a standalone Python 3 / SymPy program. Run `python check.py` in the directory containing the script. The observed output was:

```
PASS: 116 supplementary exact-arithmetic assertions
```

The program compares the proposed closed formula against direct inversion of the six-state chain's stationary equations at ten rational switching speeds, verifies the two exact crossover points and signs, checks exact Lagrange interpolation at prescribed positive crossover speeds for mode counts two through eight, and verifies adjugate-degree claims on additional rational irreducible generators. In particular, tests use rational arithmetic rather than approximate roots.

**Limits.** The general theorem is established by the displayed algebraic proof in `RESULT.md`; 116 finite assertions are not exhaustive evidence for all mode counts or real parameters. The model does not claim empirical calibration, numerical stability under noisy observations, or independent scientific validation.
