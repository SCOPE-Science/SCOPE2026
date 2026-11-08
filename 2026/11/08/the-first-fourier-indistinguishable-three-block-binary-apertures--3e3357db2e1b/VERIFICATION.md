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

Execute `python3 CHECK.py` with Python 3.10 or later; no third-party modules are needed. It enumerates exactly \(\sum_{n=5}^{12}\binom{n-1}{4}=792\) normalized three-run binary words, uses independent pair-count and bit-shift integer autocorrelation calculations, confirms all reversal and signature counts, and isolates the sole two-class ambiguity at span 12. It also verifies both examples' correlation vectors and inequivalence.

The separate direct bitmask check over binary words with occupied endpoints and exactly four internal 0/1 transitions matched the same eight rows, independently of five-part composition enumeration. The analytic implication from Fourier magnitude equality to autocorrelation equality uses a common nonzero-on-a-dense-set unit-cell Fourier factor and equality of Laurent polynomials; the converse follows by the same identity. The finite checker does not prove anything about spans greater than 12, noninteger endpoints, or uniqueness against signals outside the stated class.
