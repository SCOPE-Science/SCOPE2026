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

# Verification and limits

The included `verify.py` uses only the Python standard library. Running `python3 verify.py` yields:

```text
VERIFY_OK: 6 complete enumeration checks; 12 hypergeometric/integral identities; central rational examples
```

The independent finite paths are (i) direct permutation-by-permutation and insertion-gap counting, (ii) a hypergeometric overlap formula using integer combinations, and (iii) a rationalized logarithmic-integral coefficient sum. In addition to checking equality, the code checks symmetry, normalization and four exact central rational coefficients.

The proof of the all-order formula uses the conditional-binomial representation, not extrapolation from enumeration. The infinite Gaussian crossover and Euler-constant correction are established analytically by the beta central limit theorem, a uniform bound on rescaled beta densities and second moments, and uniform integrability of the logarithm. The verifier does not replace these infinite arguments.

All new checks concern a uniform parameter permutation and individually named positions; a realized histogram need not equal its expectation. No independent mathematical audit has been performed.
