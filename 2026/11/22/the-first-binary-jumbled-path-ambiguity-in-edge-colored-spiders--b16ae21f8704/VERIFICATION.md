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

# Reproducibility and checks

Run `python3 spider_verify.py` with standard Python 3. It checks the shape-partition enumeration, automorphism representatives, independent vertex-pair path traversal, segment decomposition, the exact 3–9-edge table, uniqueness of the two exceptional doubleton fibers, and global complement symmetry. A successful run emits `VERIFY_OK exhaustive_binary_spiders_edges_3_through_9; 25_nine_edge_shapes; 5788_labeling_orbits; 5786_topology_scoped_profiles; exactly_2_doubleton_fibers`.

The finite bounds, tree convention, labels, canonical representation and path endpoints are as in `RESULT.md`. Every compared count is an exact integer and every profile is a tuple of exact integer multiplicities. The checker was replayed using this package's exact `spider_verify.py` bytes. No external dependencies, unlisted data, random sampling, or network services are required. The result is finite only; no infinite statement is certified by these checks. No independent audit has occurred.
