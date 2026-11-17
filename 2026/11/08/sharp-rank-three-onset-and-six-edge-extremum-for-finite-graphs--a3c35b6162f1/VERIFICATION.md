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

The rank definition for finite simple graphs gives rk({v,w})>=1 iff all four adjacency profiles to an external x occur; unrolling empty and singleton extension quantifiers gives rk(X)>=3 iff some v has both a full adjacent partner a and full nonadjacent partner b. These jointly require at least three neighbors and at least three nonneighbors of v, so |V|>=7. They force six disjoint edge types: three incident v; an edge inside its neighbor set; a cross edge between neighbor and nonneighbor sets; an edge inside its nonneighbor set. At equality the profiles force the unique six-edge connected component {02,03,05,12,14,23} with all other vertices isolated, plus at least one isolate for (0,1) profile 00. Explicit v=0, adjacent a=2, nonadjacent b=1 has all four profiles in each pair. The component is asymmetric, so n!/(n-6)! labelled extremizers. Every universal graph containing all seven-vertex graphs contains the witness and has rank>=3, while disjoint union of every five-vertex graph type has no center with required three neighbors and two nonneighbors in one component, giving 6<=N(3)<=7. Distinguishes rank onset from universal forcing. Independent scratch enumeration confirmed no rank>=3 on 1..6 vertices and exactly 5040 six-edge seven-vertex graphs; the analytic argument extends all orders. Does not decide N(3)=6 vs7.

## originality

PASS

The rank recursion is due to Kubiś–Shelah, with graph-rank framework and generic finite-rank witnesses in López-Callejas–Navarro-Castillo. Its full arXiv paper explicitly asks in Section 7 Question 7.4 for N(n) and states 4<=N(3)<=|H_3|, without the new six-edge unique extremizer or the 7-vertex onset. The target supplies a motivated sharp minimal graph classification and improves known bound to 6<=N(3)<=7. The exact remaining N(3) is explicitly unresolved; a graph atlas enumerates graphs but does not alone imply their one-point-extension ranks. Broader early rank literature not exhaustively checked.

## value

PASS

The natural graph extension-rank onset is sharp in both vertices and edges, with a unique six-edge extremal shape and all-n labelled count. It materially sharpens a motivating open forcing cutoff from a generic construction to a one-unit interval and supplies the exact local obstruction. The unfinished N(3) dichotomy does not invalidate the independently valuable structural classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
