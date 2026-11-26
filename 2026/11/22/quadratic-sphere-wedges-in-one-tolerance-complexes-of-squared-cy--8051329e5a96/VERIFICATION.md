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

The claim is for the filled clique complex and ordinary homotopy for every n≥9. In a graph triangle, each of the three positive cyclic gaps must be ≤2 or ≥n−2; they sum to n, so one is ≥n−2 and the other two are 1. A 4-clique is then impossible. The complete tolerance one-skeleton, the degree-four wedge count, and the n duplications from consecutive four-sets give f₂=n(2n−9) and f₃=n(n−4). I checked all three freeness stages, including wraparound: a first-stage face has the lone length-two edge and a third vertex isolated in that face, so its unique possible completion adds the intervening vertex. The second-stage faces have precisely one consecutive edge; its two possible completions are the nominated tetrahedron and one deleted in stage I. For the third-stage face {i,i+1,i+3}, the possible completions add i+2 or i−1, the latter producing the already deleted B_(i−1). The remaining complex is 2-dimensional. Fans over paths in a spanning tree of the squared graph push every edge loop into the tree, proving simple connectivity. Thus Euler characteristic gives free integral H₂ of rank (n²−7n−2)/2, and Hurewicz plus homological Whitehead gives the wedge, not just its homology. Independent incidence peeling on directly enumerated graph cliques for n=9,10,11,12 removed all tetrahedra and gave ranks 8,14,21,29. Replay: node /workspace/branches/independent_finite_checks.js (record 1 block).

## originality

PASS

The strongest inspected results treat unfilled graphs, filled squared paths, different tolerance, a single cycle length outside the claim, or general bounds. None determines the all-n integral wedge for the filled squared cycles under review. This is a bounded best-of-knowledge decision, not a priority certification.

## value

PASS

The filled squared cycle is a natural uniformly nonchordal family for testing tolerance topology. Its explicit collapse removes every tetrahedron uniformly and the exact quadratic sphere multiplicity resolves ordinary integral homotopy, substantially more than a Leray bound or an isolated finite check. The freeness pattern gives a useful constructive benchmark for other graph-power complexes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
