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
The proof is exact for all interior initial conditions and arbitrary strictly positive payoff gaps. The critical identities checked by direct differentiation are the log-odds differential equations and the decomposition \(\dot W=\lambda W+F\), \(\dot Z=-\lambda Z+G\). Bounded vanishing forcing produces the positive exponential coefficient and an additive \(o(1)\) log-odds error. `check.py` was run on five representative parameter combinations and passed; it does not claim exhaustive finite testing or an independent formal certificate. The proposed law is not asserted under weak dominance, boundary initial data, or additional randomness.
