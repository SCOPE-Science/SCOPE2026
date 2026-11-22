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

# Reproducibility and checks

Run `python verification/check.py` from the package root with Python 3 and SymPy available. The standalone checker constructs rational symbolic weighted-divergence matrices for locally polynomial fields and verifies twelve exact kernel dimensions (for all four canonical-correlation regimes at degrees one, two and three), as well as two exact rotation substitutions at resonant and nonresonant correlations. The output obtained during this review was:

```
PASS: 12 exact polynomial nullity checks, degrees 1-3
PASS: exact resonance/anisotropy rotation comparison
```

No numerical rank tolerance or external network resource is used. The checker makes finitely many algebraic assertions; it does not certify the classification for arbitrarily differentiable functions. The general proof instead rests on Gaussian integration by parts, mixed derivatives, and a separate integrability argument at rank one. The stationary-process realization is independently checked algebraically through the Lyapunov equation and the skew-symmetric rotation generator. Independent external mathematical review has not been performed.
