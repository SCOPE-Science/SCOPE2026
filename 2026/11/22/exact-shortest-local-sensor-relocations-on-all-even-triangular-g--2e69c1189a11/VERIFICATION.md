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

# Reproducible verification

Run the two standalone Python 3 standard-library programs:

```sh
python3 verify_slide.py
python3 verify_predicate.py
```

`verify_slide.py` independently enumerates **every** size-\(k\) matching with two holes on \(n=4,6,8,10,12\) original vertices, reconstructs their complete adjacent-edge-slide graph and runs a breadth-first search of the **entire** graph from one canonical matching. It independently computes every target's symmetric-difference cycle count and source-hole path indicator, then checks the full all-pairs distance formula for every target against the computed shortest path. Vertex-transitivity of the slide graph proves that one complete BFS suffices to test all starting configurations under the tested orders. It checks all degree/edge totals and the exact diameter. The largest tested graph has \(62{,}370\) vertices and \(623{,}700\) undirected edges.

`verify_predicate.py` independently constructs the original triangular-graph adjacency and executes closed-neighborhood observation and unique-unobserved-neighbor forcing on **all** candidate selected sets up to the minimum size for \(n=4,6,8,10\). It checks that precisely the matchings power-dominate at minimum size and exhaustively excludes smaller sets; it also checks every local slide degree and the total triangle count. For \(n=10\) it tests all \(148{,}995\) candidate size-four sensor sets.

The expected final status markers are `VERIFY_SLIDE_OK` and `VERIFY_PREDICATE_OK`. Exact run outputs are included in `verification_output.txt`. These computational checks only certify their finite tested ranges. The infinite-family theorem is supported by the full proof in `RESULT.md`, and independent audit and historical priority verification have not been performed.
