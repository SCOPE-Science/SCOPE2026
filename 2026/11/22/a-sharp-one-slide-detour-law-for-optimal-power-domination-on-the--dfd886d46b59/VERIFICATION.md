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

Read the two packaged checkers and complete root certificate; did not execute the uploaded code. The separate reconstruction audit_p17.py in the private review evidence enumerated the empty set, 17 singletons and 136 pairs under closed-neighborhood observation followed by unique-neighbor propagation. It found exactly the 68 nonedges optimal. Representing each pair as an edge of H=the complement, a jump is incidence and a slide is incidence with no triangle in H. Multiplication by 3 sends H to the original graph. Independent all-source BFS reproduced the diameters 3, edge counts 476 and 272, respective sphere profiles (1,14,50,3) and (1,8,32,27), and excess 0 for 1258 and 1 for 1020 distinct unordered pairs. As a structural check on the only possible excess-2 case given these diameters, two edges xy,xz forming a triangle in H have a common Gallai neighbor xw: at most 3+3 of the 8 neighbors of x are in N_H(y) or N_H(z). Thus line distance 1 always has slide distance at most 2. These are exact finite results for optimal placements in the specified graph and observation rule; no extrapolation.

## originality

PASS

The Paley symmetries, Gallai definition/regularity, and broad reconfiguration framework are prior. The supported distinction is the Paley-17 optimal-power-domination pair classification and the joint jump-versus-slide metric on that placement space.

## value

PASS

The standard power-domination and sliding constraints on a canonical graph naturally ask whether locally permitted relocation materially increases distance, even at equal diameters. The optimal pair classification, operator correspondence, and exact per-pair penalty answer this question, give a benchmark for relocation graphs, and distinguish 1020 affected pairs from 1258 unaffected pairs. It is a useful exact fixed-graph invariant rather than just a degree count or a claim of a family theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
