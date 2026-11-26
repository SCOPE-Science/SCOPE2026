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

Reconstructed the cubic lower bound: any proper three-colouring is three perfect matchings, and each pair makes cycles. The three distinct colours at a fixed cubic vertex give a unique representative of each orbit; existence of four-colour states and the full census were independently reproduced. I used nonzero vectors and covectors of F_2^3 with zero pairing to construct the incidence graph, assigned line-stars rather than point-stars, and tested two-colour forests by traversing alternating paths from endpoints (an unvisited vertex belongs to a cycle). For adjacency, I used no proposed-move validity checker: for each deleted flag, two valid states are adjacent via that flag exactly when their remaining patterns agree modulo palette; a full unaffected line-star fixes this palette bijection. Every 20-edge acyclic restriction still uses four colours: with at most three, at least two of the three matchings would have size seven and their union would cycle. Thus a legal named recolouring cannot be hidden as a quotient loop. The calculation asserted that no unordered pair occurred for two different deleted flags. Full independent results: 230336 proper representatives, 119784 acyclic representatives, 2874816 named acyclic states, 299880 undirected edges, and components 1×392, 14×112, 42×24, 40040×1, 76776×1. The degree histogram agrees term by term; all 392 frozen states have sizes (5,5,5,6), as do 42112 mobile states. Replay: /workspace/branches/heawood_independent.py, Python ≥3.10; run `enum 0 24 DIR` then `join DIR` with a fresh directory (actual enumeration run partitioned at 0,3,7,11,15,19,24). No frozen code was executed. In the source, the incremental program prints rather than asserts much of its census; its GCC-style header is not universal C++17. The independent calculation does not rely on those claims or on sampled eccentricities.

## originality

PASS

The minimum palette is known and is not credited as novel. The closest inspected indexed results change the colouring predicate or the move; none gives the four-colour acyclic single-edge quotient spectrum or implies it. The supported originality is the exact state and move-graph census, not the general existence theorem, Fano representation, enumeration technique, or single-edge move concept.

## value

PASS

Heawood is a canonical small cubic incidence graph. At the minimum acyclic palette, local mobility does not follow from existence; the exact spectrum reveals isolated optima and many finite sectors alongside two very large sectors. The precise counts, degree distribution and one-way frozen profile give usable reference invariants for testing local recolouring conjectures and enumeration or sampling on the constrained space. This is a complete classification for a natural move rule, not an arbitrary sample or another computation of the known index.

The dated certificate retains the supplied scientific assessment, sources and limitations.
