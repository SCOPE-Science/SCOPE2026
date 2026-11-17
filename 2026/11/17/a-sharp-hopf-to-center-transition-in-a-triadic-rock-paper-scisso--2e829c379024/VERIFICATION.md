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

# Reproduction and limits

Run `python check_hopf.py` using Python 3 and SymPy. The code constructs all three explicit triadic payoff matrices, evaluates the exact quartic replicator field, and checks the four linearization entries, five complex polynomial coefficients at the Hopf surface, the vanishing real quadratic normal-form correction, and both full-vector-field reversing identities at \(\beta=1\). It also checks 18 exact-rational parameter triples as supplementary examples.

The observed successful output was:

```
TRIADIC_RPS_HOPF_EXACT_OK jacobian=4 complex_coefficients=5
TRIADIC_RPS_HOPF_EXACT_OK quadratic_correction=0 reversal=2
TRIADIC_RPS_HOPF_EXACT_OK endpoint_and_parameter_samples=18
```

The symbolic identities are for arbitrary formal parameters where the denominators are defined, not merely 18 sampled cases. A standard local Hopf theorem gives the nondegenerate repelling cycle and its amplitude. At the endpoint, the exact reversing involution, positive linear angular frequency and fixed-line half-return give the local center by uniqueness of solutions. These analytic deductions are not certified by executing a finite number of trajectories. The result has not undergone independent mathematical review.
