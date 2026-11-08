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

Run `python verify.py` from the directory containing this document and the script. The verifier uses exact `fractions.Fraction` arithmetic, explicitly generates all feasible red/blue assignments with one empty vertex, evaluates each possible single-agent move, and checks the quotient edge, its sign, the strict increase of the potential on improving moves, every projected Nash equilibrium, and the combinatorial equilibrium-coloring formula.

Observed output:

```
PASS: instances= 600 projected_states= 3000 edges= 2400 direct_move_checks= 719520 stable_colour_configurations= 35980
The general proof, not the finite experiments, certifies all graph sizes and utility functions.
```

Tested range: \(1\le a,b\le5\), \(a+b\ge3\), \(1\le r\le a+b-2\), and six rational pairs of single-peaked triangular payoff peaks. These tests check finitely many values of the model, not arbitrary real payoff functions, all graph sizes, all schedules, or every possible publication claim. The written potential argument supplies the all-size proof; source comparisons provide evidence but do not constitute an exhaustive novelty certificate. Independent audit has not been performed.
