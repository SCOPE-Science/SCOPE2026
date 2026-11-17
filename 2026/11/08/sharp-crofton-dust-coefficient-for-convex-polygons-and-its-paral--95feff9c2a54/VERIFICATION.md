---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

For an invariant unoriented Crofton line conditioned to meet convex polygon K, total line intensity is perimeter P. The event of cap area <=epsilon*A is exactly the sum of two support-cap offset widths; angular orientation conversion yields (1/P)int_0^{2pi}delta(u,epsilon*A)du. At almost every normal exposing a vertex with interior angle alpha, the small cap triangle has area delta^2 sin(alpha)/(2pq), yielding its J(alpha) coefficient. An inscribed disk yields uniform O(sqrt(area)) domination allowing angular dominated convergence. AM-GM on incident projections and 2sqrt(ab)<=a+b give strict C<sqrt2 for parallelograms, approached by flattening rhombi. The small exterior-angle integral produces C(P_n)=pi^2/(4sqrt(n))+O(n^-5/2), distinct from the circular cap exponent 2/3. Independently integrated the corner terms and limiting regular-polygon/rhombus trends; numerical finite epsilon checks are secondary.

## originality

PASS

Dias–Parisio 2014 studies cuts from a uniformly chosen boundary start and independent angle; its sqrt(epsilon) exponent applies to a different line law. Bäsel 2012 uses the same motion-invariant Crofton line measure but calculates chord length and two-point distance laws, not fragment area, and does not derive an all-convex-polygon vertex-angle coefficient or a sharp parallelogram extremum. Resultary nearest records concern short chords or boundary-point random hulls, not this area statistic. A plausible 2011 predecessor is only partially accessible and its full paper remains a historical priority risk; this alone does not negate a best-knowledge PASS.

## value

PASS

The formula identifies a natural scale-invariant dust-tail coefficient for every nondegenerate convex polygon under a canonical geometric-probability protocol and gives a genuine sharp nonattained parallelogram extremum and a regular-polygon-to-disk singular limit. It resolves shape dependence, cutting-protocol sensitivity, and a geometric boundary-layer crossover, not just a numerical special polygon.

The dated certificate retains the supplied scientific assessment, sources and limitations.
