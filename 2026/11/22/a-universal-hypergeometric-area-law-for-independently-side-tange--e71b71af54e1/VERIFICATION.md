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

Run `python check_random_inellipse.py` alongside this file's extracted companion artifact using Python 3 and the standard library only. The actual run passed 20,000 exact-geometric-formula sample checks, three separate 680 by 680 midpoint quadratures of independent nonnegative moments against a hypergeometric series, and the analytic-maximum/Hessian finite-difference comparisons. Computed mean is 0.338173084502 with 20,000-term series truncation; an extended high-precision calculation gives 0.33817308452717244. The analytic proof uses matrix identities, Heron's formula, nonnegative termwise beta integration, and local Taylor expansion; none of these universal identities follows from finite diagnostics. Human priority and independent mathematical auditing have not been performed.
