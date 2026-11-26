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

The undominated set R and the side to move suffice: a move on v is legal iff R intersects N[v], and then removes that intersection; a vertex used earlier cannot be used legally again. Thus every move strictly decreases |R|, and the two exact continuation counts follow by induction from (0,0) at R empty. After forcing an opening and one reply, the turn is again the first player's and both forced moves must be added. I independently implemented paired min/max recursion on R, with Floyd–Warshall distances, and checked every ordered opening/reply in all four graphs. The Heawood construction uses the Fano binary-vector lines, with an explicit polynomial-field isomorphism to the given modular incidences; Desargues uses two copies of the two-subsets joined by disjointness (complement the three-subset). The GP(8,3) and Pappus adjacency were generated from their specified pair conditions. All are cubic, connected, and girth six. The independent tables match every distance/outcome bin in the supplied certificate and RESULT.md and are invariant under the choice of opening. Start values in graph order are (7,6),(7,6),(8,7),(9,9); the optimal-reply counts (S responding, D responding) are (3,13),(12,3),(3,2),(4,19). Replay: python3 /workspace/reproductions/1.py; output 1.txt. This is an exact finite computation for these graphs, not a test of a general bound. The supplied C++ counts replies only at a representative opening; the independent check and the supplied Python procedure cover all openings.

## originality

PASS

The supported distinct claim is the exact strategic census of the four specified graphs, in particular the full replies for both starts, not the definition, a general starting-player inequality, or the structural classification of the graphs. The identical-looking row for a different graph was checked instead of treated as priority or dismissed based on date.

## value

PASS

The graph set is a structurally motivated exceptional quartet. For each opening the output not only gives both optimal game lengths but tells a player how sharply the best response is constrained by distance, including the split within Möbius–Kantor distance three and the Pappus distance-four requirement. This is usable tactical information not determined by a game-length bound or even by knowing both game lengths; the scale is finite and the result does not claim a theorem about all cubic symmetric graphs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
