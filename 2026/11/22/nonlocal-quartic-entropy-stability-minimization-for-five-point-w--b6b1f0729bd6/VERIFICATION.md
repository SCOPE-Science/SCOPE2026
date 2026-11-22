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

# Verification of the stated five-point strict separation

Execute `python3 verify_wordlength_c5.py` with standard Python. Rational intervals are computed for \(\sqrt5\), \(\sqrt{7/10}\), \(\log2\), \(\log3\), and \(\log(7/5)\), using integer-square-root enclosure and the positive atanh series with explicit positive upper-tail bound. The script checks strict upper ratio \(19/40\) using rational comparisons and prints interval endpoints for readability. Its run returned `exact rational witness certified` and `strict upper bound: 19/40 < 1/2`, with ratio interval approximately \((0.4724676671819746,0.4724676671888323)\).

The analytic local lower bound uses a uniform Taylor expansion and Fourier orthogonality; an explicit first/second-harmonic family achieves the value \(1/2\) in the limit. Compactness makes the strict global comparison an attainment theorem. The script verifies the witness and does **not** independently certify the all-functions Taylor argument, global optimality, or an optimizer classification. No independent audit has occurred.
