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
# Verification

Run `python3 CHECK.py` from the directory containing these files. It requires only the Python standard library. Exact expected output includes `ambiguous_spectra=4 orbit_sizes=(2,2,2,2)` and the per-length count table. The checker independently multiplies the Gaussian-integer witness factors and exhausts the 1,365 globally normalized QPSK sequences of lengths one through six. All correlation arithmetic and comparisons are exact integer operations.

The analytic bridge is the Laurent expansion of squared Fourier magnitude into its full aperiodic autocorrelation vector. The finite-loop certificate exhausts the **stated finite set only**; no inference about larger alphabets or longer sequences is made. The witness factor-flip identity can be checked term-by-term; a modulation identity explains the four distinct buckets. No automated experiment is used as an infinite theorem proof. Independent audit: not yet performed.
