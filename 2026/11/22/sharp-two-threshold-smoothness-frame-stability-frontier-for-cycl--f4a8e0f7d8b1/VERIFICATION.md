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

Run `python3 verify.py` with Python 3 and no third-party modules. The checked program is a supplementary finite test, while the analytic proof in `RESULT.md` covers all allowed integers and budgets.

The script tests exact rational harmonic Green-kernel identities for every missing-arc length from two through thirty; tridiagonal resolvent agreement with independent sine spectral sums; the two threshold values and sharp analysis-frame bound; zero-padding and harmonic endpoint energies; feasible randomly sampled completion competitors with a nonendpoint column; and finite-cycle unitary Fourier/Parseval conservation. The extracted script printed:

```
PASS: 6242 exact-identity, spectral, numerical and feasible-competitor checks
```

The analytic argument uses positive-definiteness of the Dirichlet tridiagonal Laplacian, strict convexity, reflection invariance and an exact rational inverse. A finite test does not establish novelty or replace the proof. The coverage is restricted to the unweighted cycle/path geometry, all complex-linear completions, isotropic trace energy and a full Parseval analysis; external mathematical validation has not been performed.
