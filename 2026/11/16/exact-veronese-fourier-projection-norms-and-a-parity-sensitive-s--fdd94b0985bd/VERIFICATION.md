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

The general argument is in `RESULT.md`; the computations are supplementary finite checks, not an infinite certificate.

Run `python check_veronese.py`: this constructs all symmetric dual matrices and all distinct quadratic Veronese frequencies for dimensions one through three in characteristic three and dimensions one and two in characteristic five. It checks the pointwise absolute Fourier coefficient against its rank class, the complete rank census, Parseval, and agreement of exact-rank norm formula with direct Fourier averaging. Successful terminal marker: `QUADRATIC_VERONESE_FOURIER_PASS`.

Run `python check_second.py` in the same directory (it imports `rank_count` from `check_veronese.py`): this evaluates the convergent Euler product and two parity constants at 75-digit precision for \(q=3,5,7\), then compares them with finite exact-rank norms for \(4\le n\le16\). The checked rescaled error has the explicit bound \(6q^{-n}\). Successful terminal marker: `TWO_TERM_ASYMPTOTIC_CHECK_PASS`.

These tests exercise small prime fields and dimension/asymptotic consistency. They do not exhaust prime powers, prove the infinite limit, or provide independent mathematical validation. The proof explicitly handles arbitrary odd prime powers by quadratic Gauss sums and exact symmetric-form enumerators.
