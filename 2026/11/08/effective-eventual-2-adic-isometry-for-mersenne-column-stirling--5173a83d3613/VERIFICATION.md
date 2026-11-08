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

Reproduce by running `python3 verify_stirling.py` from the extracted finding package.

Observed: `VERIFY_OK direct_independent_cases=25 eventual_cases=48 m_range=4..7 big_gap_bits=25 counterexample_at_small_n=11`.

Checks: small Stirling values from an independent integer recurrence; higher columns by inclusion/exclusion numerators reduced modulo a power of two large enough to determine valuation; pairs include multiplier gaps divisible by 2^25; a low-exponent counterexample confirms why the sufficient threshold cannot be omitted. All exact modular comparisons assert expected valuations.

The 2-adic divided-difference inequalities and the published doubling theorem, not finite calculation, prove the unrestricted result. Historical priority and independent mathematical audit remain unverified.
