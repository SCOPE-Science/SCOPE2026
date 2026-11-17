---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Computational verification

Run `python3 verify.py` with the Python standard library. The program builds each factor's edges, enumerates all three-element faces of their join independently, and for each six-face formed by one factor edge from each factor, constructs the ten complementary pairs of three-faces. It calculates all connected components by breadth-first search and separately computes predicted componentwise vertex and edge counts from the factor colorings. The two constructions are compared as multisets of triples of vertices, edges and first Betti numbers.

Nine finite triples are tested. Their graph-component counts include the equal-face-vector witnesses with components 7, 5 and 4, a three-even-cycle case with ten components, an all-tree case, and uneven bipartition class sizes. The direct enumeration establishes every claim for each reported finite input only; it is not an infinite proof. The symbolic proof in RESULT.md covers every finite connected graph factor with an edge.

The archived standard-output record is `verification_output.txt`, and its expected final line is `THREE_GRAPH_JOIN_TRIPLING_PASS`. No independent mathematical audit has been performed.
