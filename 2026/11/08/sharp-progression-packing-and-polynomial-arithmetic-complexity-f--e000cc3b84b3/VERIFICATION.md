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

Run `python3 verify.py` using the adjacent standalone script. The finite computation checks representative exact minimum-index spans and all equality exponent patterns for bases \(2\) through \(9\), target weights \(3\) through \(6\), and selected exponents less than \(12\). It also directly constructs binary arithmetic factors for bases \(2\) through \(7\) and lengths \(1\) through \(25\), checking the formula against all tested origins and steps.

Observed output:

`VERIFY_OK exponent_sets=19448 exact_minimizers=272 sample_windows=2898000 maxima_cases=150`

The script uses only Python's standard library. The unrestricted mathematical result is proved in `RESULT.md`; finite testing does not certify the infinite range and does not establish independent validation.
