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

# Reproducible finite verification

Execute in Python 3.10 or later with no third-party dependencies:

```
python3 verify_cube_edges.py
python3 verify_polyhedron.py
```

The independently constructed graphs each have \(12\) vertices, \(24\) edges and degree \(4\). Both programs check that the minimum edge-resolving set size is \(5\), with \(168\) optima, compared with vertex-metric minimum size \(3\), with \(96\) optima. Both independently verify all \(8\) omission multiplicities are \(21\), all jump and slide edges, full component sizes, radii, diameters, degree histograms, and finite all-pairs distance histograms.

For edge-metric bases, the jump graph has \(948\) edges and one \(168\)-state component of radius and diameter \(5\). The slide graph has \(360\) edges and two \(84\)-state components, each of radius and diameter \(6\), exactly separated by parity of the unique cube vertex unincident to the selected five cube edges. The first verifier additionally computes the \(48\) cube automorphisms and the four edge-basis orbits of sizes \(24,48,48,48\). The vertex-metric slide graph is connected, radius \(7\), diameter \(8\).

The exhaustive search space consists of \(2^{12}=4096\) subsets, including all \(\binom{12}{4}=495\) four-subsets and \(\binom{12}{5}=792\) five-subsets; a witness for each pair of distinct original graph edges is tested. Each reported diameter is reconstructed from shortest paths starting at every state in its component; this is complete finite computation, not statistical testing. The matched actual outputs are stored in `check_cube_edges.json` and `check_geometry.json`.

Limitations: independent human review is not available; no inference is made for larger hypercube line graphs, weighted variants, or non-edge-metric feasibility predicates.
