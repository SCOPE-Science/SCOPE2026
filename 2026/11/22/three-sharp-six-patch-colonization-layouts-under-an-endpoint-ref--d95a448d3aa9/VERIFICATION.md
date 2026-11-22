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

# Verification of the two-arm six-patch theorem

Execute `python3 verify.py` with Python 3 standard library only. The verifier reconstructs polynomial representations of the unnormalized Poisson probabilities \(\tau^j/j!\), then directly checks all finite-sum identities for the adjacent objective differences and the positive-coefficient expression proving strict threshold order. It independently evaluates the original expected-patch and endpoint-reach formula over nine positive time values, including strict winner and two-way-tie regimes. The checked package reports 124 passing assertions and at \(\tau=1\), \(R=3/5\), objective values \(2.011511800830\), \(2.058940000562\) and \(2.045818834977\).

The universal statements for all positive deadlines and all nonnegative reward weights are **analytical**: they follow from complete enumeration of three unordered layouts and the strictly positive polynomial in RESULT.md, not from the finite test grid. The code does not establish empirical ecological calibration, uniqueness in larger topology classes, historical publication priority or independent scientific validation.
