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

# Reproducibility and limits

Run the two self-contained Python programs from this directory. Both were actually executed on the embedded bytes before packaging:

```bash
python verify_fluctuation.py
python verify_master_equation.py
```

Dependencies: Python 3, NumPy, SciPy and SymPy. `verify_fluctuation.py` constructs the model drift and noise from the three possible deposited-edge types and symbolically verifies the Lyapunov equation, initial conditions, explicit cross-part covariance, and numerical root bracket. `verify_master_equation.py` constructs the complete finite-state generator with \((n+1)^3\) vacant-count states and propagates the exact finite CTMC by matrix exponential for \(n=4,8,12,16\) and \(t=0.2,1,2\). The computed normalized covariance errors decrease as size increases and fall below the programmed tolerances. These tests validate algebra and finite-state consistency; they do not constitute an infinite-size proof, which is in RESULT.md via the bounded-jump martingale limit theorem and uniform integrability. No independent external audit has taken place.
