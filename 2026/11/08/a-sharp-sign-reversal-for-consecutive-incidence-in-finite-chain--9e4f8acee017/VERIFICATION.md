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

# Verification performed

The exact conditional law was reconstructed independently in `checks/verify.py` by enumerating every possible first-round incidence, recovery of the index case, and second-round incidence. Its rational covariance was compared with the algebraic formula for 54 combinations of population size, transmission probability, and recovery probability; all passed. Exact positive and negative covariance witnesses, the \(N=3,\mu=1,p=1/2\) zero and the \(N=3,\mu=0\) exceptional sign were checked.

The all-population assertion relies on the displayed proof: conditioning on first-round outcomes, two binomial moment identities, strict concavity of a logarithmic sign factor, and uniform asymptotic expansion. Enumeration for small \(N\) does not prove uniqueness or asymptotic behavior. The primary 2026 model's finite update rules were checked against equations (5)–(6), including same-round recovery/infection independence and delayed infectiousness of newly infected persons. The published comparisons do not establish exhaustive novelty; classical equivalent results remain possible. Independent audit: not performed.
