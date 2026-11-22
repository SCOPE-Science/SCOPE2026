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

# Verification of the Hardy–Volterra self-commutator theorem

The analytic proof is in `RESULT.md`. It derives the exact monomial representation and the third-order Hermitian finite-band tail; proves a weighted Toeplitz counting lemma by finite-block freezing, section moments and min–max inequalities; and computes the strict three-frequency sign inequality. These are the infinite-dimensional proof steps, not consequences of a finite computation.

## Reproducible diagnostics

From the directory containing `verify.py`, run `OPENBLAS_NUM_THREADS=1 python3 verify.py` with Python 3.10+ and NumPy. The completed run returned exactly:

```text
VERIFICATION_OK 231
```

The tests reconstruct several complex finite Volterra matrices and their self-commutators, compare their interior entries against the infinite formula, verify the n-cubed limits of each band and the angular Fourier convention, test exact rational/radical inequalities for the trinary example, and compare finite signed counts with the predicted angular coefficients. The finite-section truncation and threshold tolerances are reported in the source file.

The strict collective sign is certified analytically by \(3(473)^2>(779)^2\) and, for any pair of derivative-coefficient amplitudes \(u<v\) at degrees \(\ell<m\), by \((v-u)(mv-\ell u)>0\). No finite matrix test is used to infer infinitely many eigenvalues. No external independent mathematical validation has been performed.

## Limits

The result covers fixed finite-degree complex polynomial symbols on classical unweighted Hardy \(H^2\). The critical case \(\max\sigma_g=0\) is not an inertia classification. No optimal spectral remainder estimate, no exact individual eigenvalues, and no certification of absolute historical novelty are asserted.
