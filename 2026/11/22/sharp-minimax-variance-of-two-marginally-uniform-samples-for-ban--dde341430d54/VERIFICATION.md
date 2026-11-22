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

# Verification and reproducibility

The analytic proof in `RESULT.md` establishes the universal minimax statement. It uses (i) normalized sine/cosine testing, (ii) a nonnegative geometric-sum/Fejér kernel inequality, (iii) exact finite-character orthogonality for the exhibiting sampler, and (iv) equality and double-angle identities. None requires computational extrapolation.

Run the standard-library-only `verify.py` with Python 3:

```
python verify.py
```

Observed execution output:

```
PASS: 2341 supplementary finite checks
```

It checks the exact triangular Fejér weights through bandwidth \(199\), root-of-unity Fourier moments numerically through bandwidth \(40\), and the normalized mean-square quadrature error of multiple nontrivial coefficient vectors on a phase grid through bandwidth \(16\). These finite checks validate constants and implementation normalization but do not prove a statement for every Borel coupling, arbitrary coefficients, or every integer bandwidth. There is no external independent validation.
