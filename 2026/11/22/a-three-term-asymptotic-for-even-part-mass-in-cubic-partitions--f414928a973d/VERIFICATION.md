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

# Reproduction and limitations

Run `python3 check_cubic_even_mass.py` with Python 3. It uses only the standard library, computes partition counts by unrestricted-coin dynamic programming, computes cubic counts by convolution, and computes the total even mass from divisor sums. A separate colored-part insertion recursion gives an independent exact-integer test of both sequences through index 125. It tests Bessel asymptotic diagnostics at indices \(100,200,400,800,1200\).

Expected completion lines: `COLORED_PARTITION_COEFFICIENT_IDENTITY_OK 126` and `CUBIC_EVEN_MASS_ASYMPTOTIC_DIAGNOSTICS_OK`. The diagnostic arithmetic does not certify the all-index analytic theorem: that depends on the modular identities and the explicitly described short-/long-arc estimates in RESULT.md. Modified Bessel ratios are evaluated numerically via a terminating positive-term series; this does not substitute for their standard analytic asymptotic expansion.
