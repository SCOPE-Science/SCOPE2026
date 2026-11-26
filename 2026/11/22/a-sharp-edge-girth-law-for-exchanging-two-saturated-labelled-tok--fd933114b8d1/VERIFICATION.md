---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

Each of the 2s tokens must make at least one move. Read an external excursion as a segment of a token's walk between consecutive visits to {u,v} with at least one interior vertex outside it (exclude a direct uv move). If any such segment joins opposite endpoints, it has length at least dist_{G−uv}(u,v)=g_G(uv)−1, which charges at least g_G(uv)−2 above that token's baseline. Otherwise every token must cross uv directly. At least one token must leave the saturated pair before any direct move is legal. If its return were the only excursion, both endpoints would then be full again and that token still on the wrong side, so the sequence could neither finish there nor continue without another departure. Two return excursions each cost at least two non-uv moves. For the upper bound, the buffer algorithm uses an exterior neighbor of one endpoint; after parking its first token and the other endpoint's first token, both endpoints have one vacancy and the outer site holds exactly two tokens. All subsequent direct pairs preserve the vacancies until the three final moves fill them, giving 2s+4. For a finite alternate path of length ℓ, parking one token at its penultimate vertex vacates one place; the 2s−1 alternating direct moves then leave a place at the other endpoint for the final detour move. This gives 2s+ℓ−1 and yields the minimum including bridges. Capacity s≥2 and at least three vertices are essential to the given construction. The definition of excursion in the frozen prose should be read as above; direct uv steps are not excursions. Frozen verify.py was inspected, not executed; its finite BFS is corroboration, not a proof over all graphs.

## originality

PASS

The complete-host metric already yields the triangle branch by a K₃ restriction and the first-move lower bound. The star-proof estimate in Cai et al. also gives the universal 2s+4 upper bound via a three-vertex star subgraph, though not the pairwise lower bound. The surviving contribution is the exact edge-local law on arbitrary hosts, including when an alternate path beats that uniform upper bound, and its matching lower bounds. No inspected source dominates that claim; priority remains provisional.

## value

PASS

Shortest paths between these highly congested labelled states constitute a natural local metric not determined by the known diameters. The exact upper/lower threshold identifies which short detours beat two temporary displacements, uniformly over all valid capacities and graphs. It provides genuinely new structural information beyond a known triangle computation or a uniform star upper bound; it does not settle odd-cycle diameters.

The dated certificate retains the supplied scientific assessment, sources and limitations.
