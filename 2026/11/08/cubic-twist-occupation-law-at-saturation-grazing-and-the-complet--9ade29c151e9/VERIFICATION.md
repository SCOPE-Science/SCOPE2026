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

Run `python3 checker.py` with the standard Python library. The checker integrates the original differential equation, separately from the algebraic flight-time matching, for 16 energy/parameter choices and verifies period and saturated-time fraction to absolute tolerance \(2\times10^{-5}\). It also tests the harmonic core, monotonicity at sample energies, near-threshold fractional coefficients, and the high-energy leading constant. It executed successfully against the embedded program prior to packaging.

The following analytic identities were also independently reconstructed and checked by symbolic differentiation:
\[
\frac{d}{ds}\left\{4\left[\frac1\Omega\arctan(\Omega/s)+\frac1m\arctan(ms/\Omega^2)\right]\right\}
=\frac{4s^2}{(s^2+\Omega^2)(m^2s^2+\Omega^4)},
\]
with \(\Omega^2=m^2+1\), and the cubic expansion at \(s=0\) has coefficient \(4/(3\Omega^6)\).

## Verification limits

ODE integration and finite test ranges are numerical sanity checks, not proof of all-energy claims, infinity limits, or absence of equivalent earlier research. The proofs of those claims use exact piecewise-harmonic matching, elementary series, and circle conjugacy, as documented in RESULT.md. Independent external mathematical audit has not been performed.
