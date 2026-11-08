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

# Symbolic and numerical verification

With SymPy installed, run `python verify_ns_euler.py`; NumPy enables the optional forward-orbit checks. The executable constructs the actual polynomial Euler map, differentiates it symbolically at the interior coexistence equilibrium, and checks the exact translated quadratic jet. It verifies the eigenvectors and dual-row normalization, nonresonance of orders one through four, invertibility and identities of the two quadratic homological resolvents, the complex resonant coefficient and the exact radial coefficient \(-17/4\), and the modulus-crossing and leading-radius factors \(3/8\) and \(3/34\).

Observed output from the packaged checker:

```
VERIFY_OK exact_jacobian=1 eigenpair=1 nonresonance=1 quadratic_jet=1 resolvent_identities=2 exact_cubic_coefficient=-17/4 radial_slope=3/34 numerical_curves=3
```

The last field refers to three 20,000-step finite trajectories at Euler steps \(2.001\), \(2.003\), and \(2.01\). They agree with the predicted leading horizontal radius to within four percent and remain in the positive quadrant in the sampled windows. These samples are not exhaustive, cannot establish an invariant circle, and do not imply global positivity. The mathematical existence statement relies instead on the analytic nondegeneracy checks plus the standard Neimark–Sacker theorem. No independent review or validation has taken place.
