---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The input graph and strict open-neighbor rule determine three distinct votes per vertex. Independent replay /workspace/reviews/replay4.py (Python 3 + NumPy) generates the adjacent-swap graph, builds majority by combining at-least-one and at-least-two truth tables on arbitrary 12-bit halves, and tests F^{t+2}=F^t on every 24-bit input from t=0 through first equality. The fixed and period-two columns agree at every t: [208,27808,185520,137856,35424,37728] and [43056,3314528,8819280,3471744,350880,353184]. No state remains after step 5; the witness 9762 has the stated trajectory and first equality at 5. Exhaustive adjacency/nonadjacency-preserving backtracking finds precisely 48 automorphisms, independently supporting the manuscript's terse group upper bound. Acting on fixed configurations and on unordered pairs {x,F(x)} gives precisely the stated orbit-size histograms, hence 20 and 717 classes. The only positive fixed masks of weight at most 4 are the six commuting-swap square masks. Analytically, the bipartite factorization's first even/odd equality conditions follow by projecting F^{2k} and F^{2k+1} to their sides; equality persists under F. This is a census by entry time and ultimate period, not individual basin sizes. The supplied programs and archived outputs were inspected, not executed.

## originality

PASS

Best-of-knowledge pass for the graph-specific cutoff, entry census and orbit/support classification, not for the general bound on eventual period or the graph's geometry and symmetry.

## value

PASS

The truncated octahedron is a distinguished cubic bipartite graph (and a small permutohedron), rather than an arbitrary 24-vertex sample. The exact sharp clock and joint census by entry and period describe how the qualitative period-two theorem manifests on it. Unordered cycle orbits separate spatial degeneracy from temporal phase, and the identification of all minimal fixed supports with faces gives a structural check. These are useful benchmark data for comparisons across graph families without being a general convergence theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
