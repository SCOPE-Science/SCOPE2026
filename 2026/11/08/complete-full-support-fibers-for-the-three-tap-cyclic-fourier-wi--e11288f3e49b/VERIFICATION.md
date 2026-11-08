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

The exact proof is in `RESULT.md`: an invertible five-frequency Fourier extraction, odd parity-cycle rigidity, the nontrivial relative-phase equation, and a converse using all three autocorrelations. Neither a finite experiment nor a numerical tolerance is used to prove the all-order classification.

Run `python3 checks.py` with a standard Python 3 interpreter to check integer-exact cyclic correlations, numerical sample magnitudes for four odd half-lengths and nontrivial roots of unity, generic negative controls, and recovery of the correlation coefficients by a discrete Fourier transform. The expected terminal marker is `THREE_TAP_FIBER_PASS`. The floating-point tests use absolute tolerance \(4\times10^{-9}\); the integer-complex correlation tests are exact. The classification beyond the checked lengths and the absence of other solutions are analytical, not computational conclusions.

No independent audit has been performed. Bibliographic priority is assessed only against the cited searchable sources; an unindexed earlier exact classification remains possible.
