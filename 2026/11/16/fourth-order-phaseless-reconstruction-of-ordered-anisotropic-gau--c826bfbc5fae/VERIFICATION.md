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

Use Python 3 with SymPy installed, from the directory containing the included source files:

```sh
python checker.py
```

The checker recomputes the exact second- and fourth-degree logarithmic Fourier expansions, verifies equality of the quartic planar factorizations and quadratic data, checks strict positivity of all planar covariance forms, tests a three-dimensional quadratic factorization and rank-one difference, and constructs a strict lower-order nonidentifiability example. All assertions passed in the recorded execution.

The universal uniqueness proof is mathematical: real polynomial unique factorization, irreducibility of the quadratic factors, and a rank bound for invertible-plus-rank-one matrices. The symbolic examples do not certify these universal lemmas. The planar counterexample uses exact rational coefficients and quadratic radicals, not floating-point approximations. No external independent audit has been performed.
