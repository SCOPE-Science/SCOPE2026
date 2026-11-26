---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

A vertex in an F^3-fixed state is either always resting or advances cyclically at every step. The former cannot be adjacent to the latter, since the latter is excited in one phase; connectivity leaves all rest or all advancing. The all-advancing states are exactly successor-neighbor ternary colorings, and have least period three. A transfer on consecutive columns checks the middle column at each step and both open boundaries exactly once. The frozen normalization by the current top color quotients the free global-shift action, so the factor three restores all labelled colorings and does not count orbits instead. I independently rebuilt an unnormalized pair-column transfer using next-color bit masks (python3 /workspace/checks/strip.py). It has 729 states and 7395 arcs, reproduces all ten initial counts, and gives 729 consecutive exact zeros of the recurrence residual. Cayley–Hamilton on that matrix gives the scalar recurrence for every n>=2, independently of the frozen 243-state certificate. The independently evaluated rational numerator and mod-seven gcd check agree; the denominator's top coefficient is a unit mod seven, so there is no rational cancellation. On |x|=8 the remainder bound 355185204 is below 3*8^9=402653184, leaving only one exterior root by Rouche; signs at 8 and 9 isolate the positive simple root. The residue coefficient for lambda^n is -rho*P(rho)/D'(rho) with rho=1/lambda (the offset is n-2), giving 0.144327187163185... and lambda=8.641216502027382.... The same unnormalized check on two rows verifies the cubic denominator with largest growth (3+sqrt(17))/2. Thus lambda^2>64>lambda_2^3 and the entropy comparison is strict without rounding. The frozen scripts and packaged outputs were inspected, not executed. This does not count non-immediate waves, attraction basins, or strips with periodic boundary conditions.

## originality

PASS

The successor-neighbor criterion, general GH phase dynamics and exact two-row census have precedents; the new claim is the reduced all-length width-three open-strip generating function and the per-vertex comparison for the same wave sector. The strongest inspected exact width-two computation and broader GH dynamical results do not imply that width-three law. Similar three-row rook-graph search material concerns a different adjacency and was not used to infer priority or to characterize its unread full theorem. The unresolved early paper is retained as a historical access risk.

## value

PASS

The three-row open strip is the first width with interior degree four, a natural extension of an exact two-row benchmark. The reduced denominator and isolated growth root give an all-length census, not merely a set of small computations. The strict increase of wave entropy per site shows that an extra interacting row does more than multiply the number of sites, even though the immediate-wave fraction is exponentially small. These exact data are useful for comparisons within primitive-three excitation dynamics; they are not claims about the dynamical entropy of all trajectories.

The dated certificate retains the supplied scientific assessment, sources and limitations.
