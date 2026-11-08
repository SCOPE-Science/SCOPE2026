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

The analytical reduction is: continuous Fourier-magnitude equality of pixelized interval unions is equivalent to equality of the complete integer aperiodic autocorrelation; the factorization in `RESULT.md` produces the explicit exceptional equality. The minimum and uniqueness are finite, exact and fully covered by the bijective seven-width parameterization and the exhaustive `CHECK.py` certificate.

Execute `python3 CHECK.py` with Python 3.10 or newer. Expected summary: `CHECK_OK raw_compositions=6435 reversal_classes=3270 first_span=22 exceptional_unordered_pairs=1`; additional lines print the nine individual counts. The test uses integer bit intersections, independent convolution and pair-count checks, and a separate Burnside count of reflection classes. The verified domain is exactly four occupied runs with four occupied widths and three gaps all at least two, and spans \(14\) through \(22\).

Finite enumeration is exhaustive only for this specified finite domain. It is not evidence for arbitrary real endpoints or longer spans. Potential historical priority gaps remain, and no independent audit has been performed.
