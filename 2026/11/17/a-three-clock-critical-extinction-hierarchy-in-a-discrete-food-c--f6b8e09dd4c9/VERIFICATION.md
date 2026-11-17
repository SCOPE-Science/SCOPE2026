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

Analytically reconstruct the proof through five steps: the explicit invariant positive wedge; factorial upper bounds from \(t_{n+1}\ge t_n+1\); the exact reciprocal increment and summable error; absolute convergence of logarithmic ratios; and the gamma-product asymptotic for the apex. The last uses \(\sum_{k<n}\log\Gamma(k)=\tfrac12n^2\log n-\tfrac34n^2+O(n\log n)\). Every asymptotic statement is quantified for fixed parameters and strictly positive forward-surviving simplex orbits.

`python3 CHECKER.py` uses only Python's standard library. It evaluates three parameter sets in the explicit positive wedge; all log states are propagated directly to prevent underflow. It checks positivity, an exact algebraic identity, the prey reciprocal correction, and the apex second coefficient at increasing integer times. Numerical diagnostics are finite and do not independently prove asymptotic convergence.

No independent audit has been performed.
