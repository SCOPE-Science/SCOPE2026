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

The initial unobserved edges are precisely those with both endpoints outside the sensor endpoint set C. The edge set of any residual cycle is a fort in the line graph: an outside edge either sees none or at least two edges of that cycle, so no force can be first. For a residual tree, process non-root vertices in postorder. At a current leaf, a second root-graph edge exists by minimum degree two; its other endpoint is either in C or has already had all its remaining edges observed, and thus this observed edge forces exactly the parent edge. Isolates need no forcing. This proves both directions for the full stated class. In Petersen, a failure is confined to the edges on the complementary vertices of some cycle. The five-cycles pair with complementary five-cycles, the six-cycles with complementary stars, and the longer cycles allow at most a single sensor edge; exhaustive independent enumeration confirms the 22 maximal failures and the polynomial. The 15 same-omitted-symbol pairs and the 140 other inclusion-minimal triples give the five optimum triangles and the size-40-plus-isolates profile at budget 3. At budget 4 every minimal triple can reach an optimum pair by adding a same-symbol sensor and removing the two other sensors, and any two optimum pairs connect through their union. At all larger budgets delete extras monotonically to a minimal pair or triple. Replay the separately written python3 /workspace/branches/95752fb1-339c-414c-851b-d5e5aae1e315/independent_check.py; full_run.json in that directory records the exact 32,768-mask exhaustion, both propagation and a forest check, and the component profiles. The original Python/C++ files and saved JSON were inspected, not executed; the finite reproduction is specific to Petersen.

## originality

PASS

The general power-domination/zero-forcing reduction and the complete-root-graph special case are known, and the Petersen graph has closely related vertex feedback-set, line-graph zero-forcing, and location-domination enumerations. The supported different result is the endpoint-restricted forest criterion for all minimum-degree-two root graphs and its exact Petersen edge-sensor census and reconfiguration geometry.

## value

PASS

The equivalence replaces a dynamic closure test by a structural forest test across a natural graph class. The Petersen specialization explains the obstruction family and gives a concrete separation of minimum-set exchange, a disconnected intermediate budget, and sharp permanent connectivity. The complete census is motivated by those structural and reconfiguration questions rather than being an arbitrary finite slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
