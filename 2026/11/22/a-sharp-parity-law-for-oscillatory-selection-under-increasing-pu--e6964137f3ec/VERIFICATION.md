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

Run `python checker.py` with Python 3 and no third-party packages. The checker computes expected payoffs directly by hypergeometric focal sampling, independently of the conditioning reduction used in the proof, and compares every value using exact rational arithmetic. It also checks strict return growth, strictly increasing total benefits, terminal neutrality and sharp parity-dependent sign sequences for group sizes from two through twenty. Unrelated payoff schedules verify the vanishing of order-\(n\) forward differences for two through eight participants per interaction.

Observed output:

```text
PASS 19 exact monotone constructive models; 307 independent payoff/coupling equalities; 63 zero nth differences; all parity maxima and terminal neutrality checks
```

The checker is a finite audit, **not** an exhaustive proof for arbitrary group sizes. Those cases rely on the hypergeometric polynomial identity, endpoint signs and explicit construction. Equal fixation probabilities follow algebraically from the Fermi ratio; no stochastic Monte Carlo convergence or independent third-party review is claimed.
