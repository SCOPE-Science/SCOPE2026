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

Explicit vertices empty, singletons and consecutive cycle pairs give polar fractional odd-cycle vertex-cover Q={z≥0,z_i+z_(i+1)≥1}. The polar vertices are the 1/2 vector and inclusion-minimal integral covers; duality gives all coordinate, maximal clique and rank facets. Their Euclidean support distances bound any ball by r≤2/(n+√n) and r≤1/(a+√a); the uniform r1 center attains all. At active rank or maximum independent sets, sums of coordinates force unique center. Comparing 2√a−1−√(2a+1) yields exact tie a=4; cyclic 2/3 gaps give M_(n,s)=n/s*C(s,n−2s). Independent construction of full facet matrix from graph independent sets and SciPy Chebyshev LP a=2,3,4,5 gave radii ~0.2763932,0.2073452,1/6,0.1381966 and tangent counts 6,8,19,22. Universal result relies on polar proof.

## originality

PASS

PASS best of knowledge for standard-coordinate exact inradius, unique center, rank/clique contact transition, and complete facet supporting-hyperplane distance multiset. Classical odd-antihole facet descriptions are prior and explicitly credited, but inspected relevant primary does not provide the metric solution.

## value

PASS

Meaningful sharp metric phase transition in stable-set polytopes of a natural minimally imperfect graph family, including an exceptional all-orbit contact tie at n=9 and an exact full facet-distance census; facet enumeration alone does not produce these Euclidean distances.

The dated certificate retains the supplied scientific assessment, sources and limitations.
