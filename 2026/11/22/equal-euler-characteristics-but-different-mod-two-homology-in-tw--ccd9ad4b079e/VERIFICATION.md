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

The graph construction gives 20 vertices and 30 edges in each case. Simultaneous index shift by five is free; reduction of indices modulo five maps each vertex's three neighbors bijectively to those in G(5,2) (inner steps ±3 reduce to ∓2), so it is a two-sheeted covering, not just an orbit quotient. A triple lies on a geodesic exactly when its largest distance is the sum of the other two: concatenation of the two subpaths then realizes the endpoint distance. Consequently all 1,140 triples can be tested by exact distances, and larger faces are precisely the subsets containing no forbidden triple. Increasing-order enumeration prunes only nonfaces and includes every face exactly once by heredity, with no cutoff in the exact reconstruction. We independently reconstructed the two graphs by their rim, spoke and step edges, found all distances by BFS, enumerated the permitted subsets, constructed mod-two incidence columns by deleting one vertex, and reduced with exact XOR pivots; boundary compositions were checked to vanish. For k=2 and k=3 respectively, the forbidden counts are 540 and 720; face vectors are (20,190,600,550,60) and (20,190,420,370,60), with no higher nonzero entries; boundary ranks in degrees 1–4 are (19,161,379,60) and (19,131,289,60). The full one-skeleton ensures reduced H0=0 (also 20−19−1=0). Rank-nullity yields reduced Betti vectors (0,10,60,111,0) and (0,40,0,21,0); both alternating face sums equal −60. The unequal groups rule out homotopy equivalence without yielding integral homology or specifying either homotopy type. RESULT.md lines 25–70, VERIFICATION.md and verify_gp_covers.py were inspected; the frozen verifier was not executed. The independent reconstruction is replayable via python3 independent_gp_check.py, with its two-line exact result in independent_gp_check.out, retained separately in the private audit workspace.

## originality

PASS

The exact comparison of mod-two homology of these particular geodesic general-position complexes is distinct in the inspected sources. The strongest prior same-graph topology is an induced-matching classification of exactly the same cover pair, but it is for another complex. Known general-position definitions, counts by size for the ten-vertex base graph, and same-day homology studies for other graphs do not determine the binary boundary ranks in these covers. The finding does not claim originality for the geodesic predicate or exact rank algorithm.

## value

PASS

These are two canonical cubic double covers of the same Petersen graph, not arbitrary unrelated examples. Their geodesic complexes match on Euler characteristic and number of top-dimensional simplices, yet exact mod-two ranks locate the topological distinction, including the presence versus absence of degree-two homology. This is a useful finite reference comparison of a natural invariant, apparently not determined by a known table or implication. The conclusion is explicitly about this pair, not a general statement about lifts or integral torsion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
