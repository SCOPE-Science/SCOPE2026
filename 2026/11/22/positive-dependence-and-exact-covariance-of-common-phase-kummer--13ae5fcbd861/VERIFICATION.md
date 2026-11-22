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

The independent-from-formula diagnostic program `check.py` integrates two floor-defined carry indicators by subdividing the unit interval at every jump of each function. All integrations and kernel arithmetic use Python `Fraction` objects, not floating-point approximations. For every \(3\le d\le35\), it compares the direct two-variable covariance with the exact gcd-kernel formula for all \(1\le j\le k<d\); it also checks positivity and a necessary central-index condition for any observed zero. It reports 7,139 matches and 86 zero cases all involving the center. The analytic Fourier-sign certificate, not the finite program, proves positivity for all integers.

Run in the directory containing the attached source as `python3 check.py`. Python 3's standard library is the only dependency. Source code is complete and self-contained; no external binary, remote service, paper PDF or dataset is needed.

Scope limit: this evidence says nothing about higher-order positive association, independence between all coordinates, or the actual joint arithmetic distribution of prime-adic valuation sums. A separate independent mathematical audit has not been performed.
