---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

A predecessor with sum s is uniquely parametrized by x; its product is x^2+sx in exact characteristic two. Additivity makes nonempty fibers equal-sized. For 2v<k, where v=nu(s), multiplication by pi^v times a unit annihilates exactly J^{k-v}; a putative root of x(x+s)=0 with nu(x)<v is impossible because its product has valuation 2nu(x)<k. If nu(x)>v the other factor has valuation v, and if nu(x)=v the root must be within J^{k-v} of s. This gives exactly the disjoint cosets J^{k-v} and s+J^{k-v}. For nu(s)>=h, both factors vanish multiplicatively whenever x is in J^h, and x outside that ideal has too low a valuation. Thus counting pressure from each fixed-s stratum gives the stated histogram, adding coincident degrees (e.g. q=2,k=2). The weighted counts give q^{2k} arrows independently by totaling the q^k domain choices of x for each s. At k=1 the formula is q repeated-root, q(q-1)/2 double-distinct-root, and q(q-1)/2 no-root targets; the parity maxima follow by comparing 2q^{h-1} to q^{floor(k/2)} and observing that both strata exist. The frozen verification script and stdout were inspected, not rerun; the valuation argument is not limited to the enumerated presentations.

## originality

PASS

The distinct supported result is the complete ordered-multiplicity histogram for all lengths in exact characteristic two, including how nilpotence and degree collisions affect it. The quadratic-root equivalence and the field case are known or elementary and not credited. The closest indexed random-quadratic laws are in a different ring; the same-map graph studies inspect different invariants.

## value

PASS

In-degree, including the number of sources, is a natural invariant of this longstanding finite-ring graph, with a second use as an exact distribution of roots of uniform monic quadratics. The full nilpotent chain family, rather than an isolated ring or number, gives a uniform description of multiplicities, parity-dependent maximum and small-field degree collisions. This fills a well-posed census not supplied by the basic root observation or short-cycle profile.

The dated certificate retains the supplied scientific assessment, sources and limitations.
