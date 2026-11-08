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

# Reproducibility and evidence boundaries

To replay the numerical checks, run `python3 verify.py` with Python 3.9 or later; only the standard library is needed. `verification_output.txt` contains the actual checker output. The checker exercises exactly represented rational duration weights and mean constraints, cosine-spectral identities, mixed quadratic multipliers, Fejér pointwise identities, and explicit nonuniform optimal distributions for finite sizes. It does not constitute a proof for arbitrary \(K\). The all-\(K\) argument is the analytic Fejér, harmonic-Gaussian, and Fourier-inversion proof in `RESULT.md`.

The sampler uses ideal Hamiltonian evolution and counts Markov transitions. Finite-step Hamiltonian integration, Metropolization and general Gaussian spectra were not tested or proved. No independent external scientific audit has been performed.
