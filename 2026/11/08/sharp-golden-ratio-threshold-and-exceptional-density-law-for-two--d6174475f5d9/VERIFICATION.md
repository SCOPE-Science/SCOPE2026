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

# Reproducibility and verification

Run `python3 verify.py`. This standalone Python 3 script uses standard-library decimal arithmetic to construct several irrational moduli at high precision, enumerate the first few thousand twofold floor-map terms, and compare direct membership against both the published twofold test and the new exceptional region. The tested cases include exact-square quadratic structures, a cubic algebraic modulus, and a transcendental modulus; it checks false-positive/false-negative counts, the complete branch identity, and the exact \(\sqrt[3]{3}\) counterexample at \(x=2\).

The reported finite outputs are:

```
DIRECT_RANGE_EQUIVALENCE_OK sqrt2 N= 6000 false_negatives= 0 false_positives= 0 density= 0.00000000 torus_prediction_if_independent= 0.03033009
DIRECT_RANGE_EQUIVALENCE_OK sqrt6 N= 6000 false_negatives= 0 false_positives= 0 density= 0.00000000 torus_prediction_if_independent= 0.00000000
DIRECT_RANGE_EQUIVALENCE_OK cuberoot3 N= 16000 false_negatives= 348 false_positives= 0 density= 0.02175000 torus_prediction_if_independent= 0.02186067
DIRECT_RANGE_EQUIVALENCE_OK pi_over_2 N= 20000 false_negatives= 30 false_positives= 0 density= 0.00150000 torus_prediction_if_independent= 0.00137915
DIRECT_RANGE_EQUIVALENCE_OK phi N= 6000 false_negatives= 0 false_positives= 0 density= 0.00000000 torus_prediction_if_independent= 0.00000000
VERIFY_OK finite_only=True analytic_equidistribution_not_computationally_certified=True
```

Finite enumeration does not certify any unrestricted statement, the natural density limit, or historical priority. The exact proof uses only unique inverse-floor arithmetic, the inequality \(\alpha^2-\alpha-1\ge0\), and classical torus equidistribution. The checker does not perform an independent mathematical audit.
