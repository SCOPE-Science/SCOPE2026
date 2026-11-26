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

The positive-length paths span the nilpotent arrow ideal, whose vertex-algebra quotient is semisimple. There are w+e arrows, 2e length-two paths and e length-three paths, no longer paths, so J has dimension w+4e and J³ has the stated basis. Each cubic coefficient is precisely a_u b_{uv} c_v because only a concatenation of three arrows can survive and the specified path has one such factorization. This leaves 3e higher-path coordinates free. Fixing the set S of nonzero outer coefficients forces S to include every endpoint of a nonzero target edge, then determines the middle variable on each induced edge and leaves each other middle variable free. This derives the entire prescribed fiber and ensures surjectivity (choose all outer coefficients equal to one). In fact the fiber depends only on the set of forced endpoints. At zero, the squarefree ideal is the intersection of coordinate primes for vertex/edge-variable transversals of the triples; minimal transversals give geometrically irreducible components. Disjoint triples from a maximum matching lower-bound all transversal sizes, and a minimum bipartite vertex cover realizes equality. For a fixed set S of retained outer variables, the unique least transversal with these retained outer variables is W\S plus the middle variables of induced edges. Thus the components of maximum dimension are directly enumerated by the S satisfying |S|-e_G(S)=w-nu(G). The leading term of the root polynomial comes from just these sets and has positive coefficient c_G, with next degree at least one lower, yielding the stated probability and error for fixed G. Conditioning on all outer variables nonzero gives exactly uniform output and the probability of failure is at most w/q, giving the TV bound. The argument has no coefficient or sign restriction and applies in characteristics two and three. Independent inclusion-exclusion checked all 16, 32 and 64 graph supports in three further cases (K2,2 over size 5, an irregular disconnected graph over size 7, and a six-cycle over size 4); direct transversal enumeration checked the top-component counts 2, 9, 2 and exact TV estimates. These checks used coefficient counts and not brute-force path multiplication.

## originality

PASS

The distinct result is the exact prescribed cubic census for a whole graph-indexed radical family, coupled to the matching-controlled zero fiber, its exact leading coefficient and a uniformity bound on the whole target distribution. The arrow-ideal description, monomial component description and König's theorem are prior mechanisms, not new results. The closest actual cubic-fiber statement is a single-chain algebra, and the most similar graph-indexed counting methods concern different equations. The comparison supports the specialized claim without making an exclusive priority assertion.

## value

PASS

The prescribed-target count, the leading coefficient of the exceptional probability, and the top components are usable invariants of a natural layered path-algebra family. In particular the same graph statistic controls codimension and the decay exponent, while the explicit component count distinguishes graphs with equal matching number, and the near-uniform law clarifies why that exceptional fiber does not dominate total variation. The result yields more than the application of a matching theorem to determine one exponent.

The dated certificate retains the supplied scientific assessment, sources and limitations.
