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

# Reproducibility

The analytical proof in `RESULT.md` is the evidence for uniqueness in the infinite-dimensional class. `verify.py` is a self-contained deterministic Python 3 program using only the standard library. It numerically checks the finite telescoping Fourier identity at 1,200 randomized response/velocity configurations, the exact low-order moment recovery, 2,600 single-speed convolution aliases, and 1,800 mass-normalization identities, reporting 12,800 successful comparison assertions.

Run `python3 verify.py`. These finite assertions neither establish unbounded-frequency stability nor replace the Fourier-injectivity proof. No field data or independent external audit is supplied. The theorem assumes an exactly stationary full-line source, unit sensor gain, constant known velocities, nonvanishing Fourier factors, noiseless full-line recordings and prehistory correction.
