---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

For n>=5 and the specified synchronous independent-attempt rule, the blue cycle stays an interval. The m=1 boundary uses a_1=89/80, while m>=2 two-endpoint recurrences distinguish whether 0/1/2 frontier leaves are blue. Solving their rational generating functions, the initial singleton correction, and the one final deterministic leaf-clearing round proves ept(S_n)=11n/16+4437/3344+(1323/6688)(-2/9)^(n-2)-(147/608)(-2/5)^(n-2), and a positive leaf-start disadvantage. Independent exact Fraction reconstruction confirmed the recurrence and both expressions for n=5..17, including ept(S_5)=1225469/256500. The general-n result follows from the algebraic rational-series identity and geometric error bound, not those finite tests.

## originality

PASS

The directly relevant 2019 Chan et al preprint and 2020 journal version explicitly posed the sunlet 11/16 limiting-increment conjecture and tabulated numerical values for n<=45. Their finite-state matrix technique gives computable finite instances, but does not exhibit the two explicit geometric correction terms, all-size evaluation, optimal start orbit and proved increment limit. Background pure-cycle/path forcing formulas do not imply the degree-three pendant-leaf system. Best-of-knowledge PASS with residual old or unindexed exact evaluation risk.

## value

PASS

Solving a published limiting-increment conjecture with an exact all-size expectation and initial-vertex optimality settles a natural probabilistic graph-process statistic, and alternating corrections quantify its convergence; not merely a numerical re-fit.

The dated certificate retains the supplied scientific assessment, sources and limitations.
