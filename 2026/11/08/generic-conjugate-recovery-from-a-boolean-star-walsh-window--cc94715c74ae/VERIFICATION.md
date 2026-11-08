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

# Verification and reproducibility

Run `python3 verify.py` using the Python standard library. The checker computes all \(2^{2n}\) squared Walsh-Gabor magnitudes in the test dimensions \(n=2,3,4,5,6\), inverts their Walsh transforms exactly as integers, and checks the lag-zero, lag-one and lag-two formulas for every translation. For even dimensions it recovers every squared magnitude by exact rational arithmetic, and reconstructs all coordinates from two local Gram constraints, again with rational arithmetic. It also independently counts nonzero ambiguity coefficients by combinatorial intersections and compares their count with the closed span-rank formula.

The analytic proof covers all even \(n\ge2\); the finite checks do not certify an infinite statement. The checker deliberately does not assert odd-dimensional conjugate recovery. No external certification, statistical independence, or separate mathematical audit has been performed.
