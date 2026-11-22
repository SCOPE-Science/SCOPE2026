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

## Reproducible checks

Run `python checker.py` with Python 3 and the standard library. The program verifies exact rational Hamming-shell Fourier coefficients, harmonic antipodal identities, strict monotonicity, Parseval angular energy, and the full ambient Euclidean facet-normal calculation, using a separate matrix inversion implementation. Its exact domains are \(2\le d\le18\) for Walsh formulas and \(2\le d\le4\) for independent Gram reconstruction. Printed larger-d ratios are numerical diagnostics only.

The proof for all \(d\ge2\) is in RESULT.md. No finite check purports to establish an infinite statement; binomial moment expansions, the heat-kernel ordering and the harmonic identity are proved analytically. No external audit has been performed.
