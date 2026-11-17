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

For even N and triangle-free H_N, every allowable-edge greedy step reduces vacancies by two and cannot stop with k≥3; a terminal two-set must be forbidden. For each forbidden e, exact conditional one-step survival is (binom(k−2,2)−h0)/(binom(k,2)−1−h0−h1), with baseline s0=(k−3)/(k+1). One-step degree-bounded r-mark comparisons give uniform survival ΘΔ((k/N)^r) for r=2,3,4 above fixed L, hence conditional counts E[h0|e] = OΔ(k²/N), E[h1|e]=OΔ(k/N). Their relative survival correction OΔ(1/(Nk)) telescopes with logN/N loss. At fixed final L, all extra forbidden edges disappear conditionally with probability 1−OΔ(1/N). Baseline product yields 3/(N²−1); summing disjoint forbidden final pairs gives 3m_N/(N²−1)(1+OΔ(logN/N)). Independently computed exact subset recursions: single forbidden edge n4=1/5,n6=3/35,n8=1/21,n10=1/33; forbidden cycles n6=1/3,n8=212/825,n10=178177/825825. These finite checks do not prove uniform asymptotics.

## originality

PASS

Exact deleted-perfect-matching jamming coefficient and graph RSA background are already prior; neither establishes the uniform sharp leading coefficient over arbitrary irregular, disconnected triangle-free Δ-bounded forbidden graphs. Bounded-degree *adsorption substrate* results differ from bounded-degree *exclusion graph* with dense allowed substrate. Best-of-knowledge originality passes with a substantive full-text risk for early graph RSA publications.

## value

PASS

The imperfect-saturation probability in dense random greedy matching with sparse local restrictions is a natural rare-event quantity. The strong uniform coefficient independent of forbidden graph geometry, including arbitrary disconnected and irregular fixed-Δ cases, provides a structural universality law and specific cycle prediction beyond the solved deleted-matching special case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
