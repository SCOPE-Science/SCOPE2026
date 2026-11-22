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

# Verification record

## Reproducible checks
Run `python3 verify.py` using Python 3.10 or later. The program uses standard-library rational arithmetic and no external data or network. It reconstructs the Volterra polynomial kernel and the antidiagonal coefficients at orders 1 through 6, verifies the finite Gram-matrix spectral product, and checks 28 sampled noninteger Vandermonde determinants. The actual package-path replay returned:

```
PASS: m=1,...,6 exact polynomial-kernel and spectral-product identities;
PASS: 28 noninteger finite Vandermonde consistency certificates.
```

## Mathematical and scientific limits
The exact-arithmetic computations are finite checks, not proofs for all orders. The general proof uses a noninteger fractional-power expansion, a Vandermonde independence argument for arbitrarily many columns, midpoint reflection anticommutation, and polynomial coefficient plus Hilbert determinant identities for integers. Noninteger decay rates and nullspaces are outside the claim. A relevant archival article was not available in full text, so historical priority is not independently certified. The review is same-model only; no independent audit has been performed.
