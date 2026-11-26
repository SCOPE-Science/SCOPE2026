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

The stated graph was rebuilt from KG(5,2) with one inflated vertex; testing all adjacency-preserving extensions confirmed exactly the twelve lifted permutations stabilizing {0,1}. Distinct ranks in each flag force a quotient identification within its closed simplex to be the identity on barycentric coordinates; each simplex is embedded, its facets have distinct rank sets, and the alternating deletion boundary has no stabilizer factor. The independent /workspace/review-work/orbit_check.py run with argument 1 used a different edge order, ordered-partition flag generation, reverse canonical representatives and alternative collapse, spanning-tree and pivot orders. It recovered 1051 matchings, 162053 flags, orbit cells (121,1250,3981,5222,2850,480), and 6524 verified free pairs leaving (43,235,385,193). All 193 generators in the resulting genuine 2-skeleton were eliminated by nonabelian substitutions. Exact unit pivots with higher-boundary coordinate checks left free chain ranks one in degrees zero and three and zero elsewhere. This gives trivial pi_1 and integral homology (not just rational). Hurewicz gives pi_2=0 and a sphere map realizing the H_3 generator; the simply connected homological Whitehead theorem gives the stated homotopy equivalence.

## originality

PASS

The strongest inspected exact-object precursor gives the unquotiented ordinary matching complex and rational symmetry character, not the integral geometric orbit type. The other close claims change the graph, the action or the simplicial construction. In particular the proof of simple connectivity and the absence of integral torsion are not supplied by the rational representation. The bounded source comparison supports a distinct result, not a universal priority claim.

## value

PASS

The ordinary matching complex of a standard symmetric cubic graph and its full geometric orbit space are natural objects. The exact sphere type supplies integral and nonabelian information not recoverable from the known character, and distinguishes what the quotient does from what rational averaging predicts. The reproducible extraction of integral chains and actual attaching words is meaningful for precisely this action, even without a graph-family theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
