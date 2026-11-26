---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

In the killed equation Df″−(s+r1_{x>L})f=−r1_{x>L}, the reflecting and bounded solutions are a cosh on the inactive leg and r/(s+r) plus a decaying exponential on the active leg. Continuity of value and derivative at L gives the stated transform. Its s↓0 limit is 1 and the analytic expansion has finite moments (the square-root factors cancel at zero). As an independent moment check, put a=L√(r/D), y=x√(r/D), M₁=r EₓT, M₂=r² EₓT². On the left M₁(y)=1+a+(a²−y²)/2; on the right M₁(y)=1+a exp(−(y−a)). The second-moment equation gives M₂′(a−)=−2a(1+a)−2a³/3; the bounded right solution is 2+[c+a(y−a)]exp(−(y−a)), giving M₂(a)=2+3a+2a²+2a³/3. Subtracting M₁(a)² yields the stated variance. Strong Markov at resets to L gives iid intervals, and the conditional hazard gives a nonlattice law. The renewal variance-to-mean limit is Var(T)/(ET)². Its difference from one is a(2a²/3−1)/(1+a)²; its derivative has numerator (2a³+6a²+3a−3)/3 over (1+a)³, with the numerator strictly increasing on a>0. This verifies the crossing, unique minimum and its characterization; r/(1+a) increases strictly with r. These are fixed-parameter long-time statements about effective resets, not counts of alarm proposals. CHECK.py was inspected, not executed.

## originality

FAIL

There is exact broader coverage of the full clock transform in Salminen–Stenlund's diffusion occupation-time formula; Bressloff independently gives an evaluated finite-box occupation resolvent with exactly this half-line limit. These are explicit formulas, not merely general Feynman–Kac advice. The observed count is a renewal count with that clock. Its sharp crossing and minimum, though not found written verbatim in those sources, follow by two derivatives, the standard renewal Fano identity, and a one-variable sign calculation. No additional uncovered result of the frozen scope was established. This is a coverage judgment, not a claim that an earlier paper printed the same Fano threshold.

## value

FAIL

The dispersion question is natural and the threshold can be useful, but this record's exact result is a routine consequence of the prior evaluated occupation law for an already introduced resetting process. The derivative and sign formulas add a convenient presentation rather than a distinct exact fact not mechanically implied. No independent scientific remainder warrants repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
