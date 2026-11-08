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

# Verification of the finite-size formula

Run `python verify.py` with Python 3.8+ (standard library only). The program generates the finite-state continuous-time Markov matrix directly from the exact birth, death and switching rates, solves its stationary linear system over `fractions.Fraction`, and computes the second central moment. It separately evaluates the closed theorem formula and uses exact rational equality. Across \(N=2,\dots,7\), five input regimes per size include unequal switching intensities, unequal environmental switching rates, same-noise degeneracy, and the zero-herding boundary. Additional exact comparisons of four switching speeds for each \(N=2,\dots,19\) test the direction of the claimed strict trend. Expected output:

```
PASS: 84 exact rational identities / monotonicity inequalities
```

The infinite-population-size quantifier and sign assertions are proved in `RESULT.md` by exact identities. Finite computations are neither exhaustive over parameter choices nor substitutes for that proof. The model and source-reference limitations are recorded in `RESULT.md`. No independently audited proof status is asserted.
