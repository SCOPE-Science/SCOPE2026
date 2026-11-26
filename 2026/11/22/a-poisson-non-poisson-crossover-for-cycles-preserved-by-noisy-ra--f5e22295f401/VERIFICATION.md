---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproduction and limits

Run `python3 verify.py` using Python 3 with only its standard library. The verifier enumerates every function \([n]\to[n]\) for each \(n=2,3,4,5,6\), namely 4, 27, 256, 3125 and 46656 cases (50068 total). It conditions on each map's cycle structure and compares 115 exact rational mean, ordered distinct-pair and inclusion–exclusion void formulas at refresh retention \(\rho=2/3\), including redraw coincidences.

The critical analytic argument is the exact distinct-cycle factorial identity and the two limits \((n)_K/n^K\to e^{-S^2/2}\) on square-root scale versus \((n)_K/n^K\to1\) on the smaller \(1/\delta_n\) scale. Finite enumeration does not prove those limiting transitions. The strict negative covariance is computed analytically for disjoint, bounded, positive-length intervals of scaled lengths **bounded away from zero**. The analytic first and second moment bounds also show that counting all the way down to zero gives an infinite critical limit count. The verification does not certify historical priority.
