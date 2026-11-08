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

The included `verify.py` has been executed with a Python environment containing NumPy. It checked Krawtchouk recurrences for every dimension from 2 through 60, exact rational orthogonality through dimension 18, the local zero set and endpoint binomial weights, and 72 independently assembled non-Hermitian spectra. All checks passed. The general-dimension statements rest on the proof in `RESULT.md`, not on these finite experiments.

The check assumes the explicitly specified one-excitation chain and positive independent imaginary onsite loss. Neither physical hardware performance nor independent scientific audit is certified.
