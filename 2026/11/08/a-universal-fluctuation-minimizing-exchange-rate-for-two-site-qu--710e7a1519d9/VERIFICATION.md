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

# Mathematical verification

The finite-dimensional transient generator \(B=-A\) is formed from the populations and the imaginary single-excitation coherence. The first-passage survival integral yields \(\mathbb ET=w^\top B^{-1}e_3\) and \(\mathbb ET^2=2w^\top B^{-2}e_3\). An excitation-number supermartingale estimate bounds survival by \(2e^{-\min(\gamma_1,\gamma_2)t}\), ensuring moment finiteness and the validity of these integrals. Both moment expressions and the factorized derivative appear in the accompanying result.

## Reproduce checks

With Python 3 and no external packages, run:

```bash
python3 verify.py
```

Expected observed output:

```
PASS: 2135 exact-rational identities / independent spectral assertions
```

The checker independently solves the transient-generator equations twice for \(210\) exact-rational triples of positive decay rates and exchange couplings; it checks all rational moment and gradient identities, all optimized-value formulas, the distinct/symmetric-rate cases, and additional independent spectral-mode calculations. The standalone script was executed successfully from its packaged contents.

## Proven domain and limits

The proof applies for all \(\gamma_1,\gamma_2>0\), all real \(J\ge0\), no detuning, zero-temperature independent local amplitude damping, and initial state \(|11\rangle\langle11|\). It does **not** establish any analogous optimality for detuned or driven systems, coupled baths, more sites, discrete time bins, or minimum absolute variance. Exhaustive real-parameter coverage follows from the algebraic sign factorization, not from the finite test grid. No independent audit has been performed.
