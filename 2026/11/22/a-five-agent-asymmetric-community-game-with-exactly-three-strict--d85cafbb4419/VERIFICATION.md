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

Run `python3 verify.py`. It uses standard-library `fractions.Fraction` and `itertools.product`, and solves rational linear systems by Gauss–Jordan elimination. Its exhaustive finite cases range over both community sizes from one through four, positive within- and cross-community weights, three independent opinion weights, and six threshold values. For every binary action profile it calculates the unique optimal equilibrium opinion vector, directly checks strict binary payoffs, and compares the resulting Nash set with the analytical four-pattern formula.

Expected checker output: `PASS 2160 parameter cases; 92736 enumerated profiles; example: exactly three equilibria`.

The five-person worked example is independently checked with exact fractions, including its three equilibrium action vectors, the polar opinions, and both group mean opinions. The general proof does not rely on this finite enumeration. Weak equilibria at threshold equalities, dynamical behavior, empirical interpretation and historical priority are outside the verified mathematical claim.
