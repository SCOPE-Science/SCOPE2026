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

Each pair of lines can be recovered from its union, since any third line contains at most one point on each, and so is not contained in the union. My exact recreation using disjoint pair blocks in vertex permutations gives 60 six-point concepts and 45 five-point concepts. Direct set traces on every support of size ≤5 give [1,15,105,375,495,0], which excludes larger supports by heredity. Comparing every face with the next cardinality gives precisely the 15 line triangles and all 495 quadruples, no smaller facets. Adjacent-swap orbit generation matches the 3-, 4-, 5-support orbit/trace multisets in RESULT.md 34–46, in particular the three 4-facet orbits of size 45, 90 and 360. Boundary row reduction by symmetric difference gives ranks 14,91,269 and hence reduced Betti (0,0,15,226) over F₂. A separate depth feasibility search prunes only branches with fewer than 2^remaining-depth possible concepts; it accepts depth five and rejects depth six. Unpruned reachability yields 58598 nonempty states, and the frozen JSON tree (labeled in the symplectic model, not the matching order) has all 32 distinct, consistent leaves. Replay with python3 /workspace/reproductions/doily.py followed by the frozen depth5_tree.json path as argument. The original programs were inspected, not run. The classification is finite, with no integral homology claim.

## originality

PASS

The restricted doily census and the topology and online depth are distinct from the strongest inspected OR and plane-union overlaps; retain residual risk for differently indexed finite calculations.

## value

PASS

This is the complete classification for a canonical smallest thick generalized quadrangle, not a selected numerical slice. The Boolean trace and online-query thresholds differ, and the lower-dimensional facets recover exactly the original incidence lines. The two nonzero reduced mod-two ranks and the orbit census make a reproducible benchmark for learning on restricted incidence designs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
