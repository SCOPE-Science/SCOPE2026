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

# Reproducible checks

`python3 verify.py` (Python 3 standard library) passes 42,747 assertions. It enumerates every binary creation word of lengths 2–12; independently detects Hamiltonian cycles by a subset dynamic program for graphs through nine vertices; checks graph degree and edge/clique identities; checks all local-run counts against the reflection formula. An independent height-state recurrence checks positive-path counts and area sums through 79 steps, while short survival counts are checked by direct step enumeration.

The exact finite assertions cannot establish Brownian-meander convergence or uniqueness in the literature. The infinite theorem uses the published finite-horizon meander invariance principle and exact ballot asymptotics. The local–global independence deduction is a mathematical argument, not a simulation statement. The complete graph boundary and finite versus asymptotic independence are explicitly addressed. Independent audit: not performed.
