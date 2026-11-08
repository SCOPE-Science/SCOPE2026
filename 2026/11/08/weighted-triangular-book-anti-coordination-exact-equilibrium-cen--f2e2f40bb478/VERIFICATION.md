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

# Reproduction and scope

Run `python3 verify.py` with Python 3.9+; only the standard library is needed. The checker constructs weighted graphs and computes each player's exact rational payoff under every binary profile for finite test settings. It directly compares the full Nash count, best and worst equilibrium cut weights, aligned/opposite types, equal-weight binomial special case, and perturbation threshold with independent formulas.

Observed output:

```text
PASS: 2605 independent parameter settings, 318360 directly enumerated labeled profiles; exact equilibria, welfare, counts, and perturbation cases
```

The settings include exhaustive rational weights in \(\{1,2\}\) through four pages, boundary spine weights, randomized heterogeneous rational weights through seven pages, all-unit examples through eleven pages, and the even-page perturbation family. Finite testing is not a proof for arbitrary page counts and real weights; the case analysis in `RESULT.md` establishes the general theorem.
