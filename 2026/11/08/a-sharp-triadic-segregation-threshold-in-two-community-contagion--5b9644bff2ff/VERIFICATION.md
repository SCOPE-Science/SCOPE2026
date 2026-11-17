---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

Starting from the actual equal-community pure-triangle two-dimensional field, exact s=(x+y)/2,d=(x−y)/2 reduction gives d²=s²[2ε(1−s)−1]/[ε(1−2s)], λ=[2εs((1−s)²−d²)]⁻¹ at every unequal interior equilibrium. Positivity restricts 1/2<ε<1 and 0<s<1−1/(2ε)<1/2. Independently recomputed symbolic Jacobian gives trace T/D, determinant [2ε(1−s)−1]P/D², with P=ε(12s³−17s²+8s−1)+4s³−3s²; the exact polynomial identities cancel to zero. On the potentially stable interval P>0 iff ε>F(s)=s²(3−4s)/(12s³−17s²+8s−1), whose unique minimum at s=(3−√3)/4 equals (9+24√3)/61. Verified the sum-of-squares positivity used to force negative trace; at ε=9/10,s=1/3, the witness trace is −1 and determinant 6/25. Hyperbolic local only; equality nonhyperbolic, λ selected as needed, and other contagion models are excluded.

## originality

PASS

Landry–Restrepo derives exactly these pure-triadic equations as a restriction, including numerical disparity regimes, but does not state an all-positive-λ necessary-and-sufficient stable unequal-endemic threshold at (9+24√3)/61 in inspected text. Broader simplicial SIS sufficient criteria and an earlier Resultary equilibrium-existence barrier do not imply HYPERBOLIC stability of the same branch; mathematical comparison is made at the trace/determinant level.

## value

PASS

A natural open question in the original numerical phase diagrams is the exact least triangle assortativity enabling a STABLE asymmetric endemic state at any strength. An algebraic global lower boundary, exclusion beneath and feasible stable construction above is a meaningful sharp phase transition not supplied by local numerical examples or general sufficient criteria.

The dated certificate retains the supplied scientific assessment, sources and limitations.
