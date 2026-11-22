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

Use a standard Python 3 interpreter and run `python proof_check.py` in the directory containing this document. No third-party dependencies or downloaded files are needed. The test suite evaluates 79,922 exact rational assertions for single-, double- and triple-scale Poisson mixtures, harmonic orders up to eight, negative-cutoff sharpness, every finite tested Fourier ratio and the exact closed-form two-rate spectral identity. It also checks a log-convex positive sequence outside the Hausdorff moment class whose active constraint does not occur at the modulation harmonic. The check was replayed successfully from the packaged path.

The universal criterion, exact boundary support, strictness, and two-rate identity have independent analytic steps in RESULT.md. The finite checker does not enumerate uncountably many measures, infinitely many frequencies or all finite point configurations; those domains rely on the proof. No machine formalization or independent mathematical audit is claimed.
