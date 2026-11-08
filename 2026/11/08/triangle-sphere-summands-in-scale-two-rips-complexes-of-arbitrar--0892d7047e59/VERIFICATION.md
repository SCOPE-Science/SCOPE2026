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

# Finite reproducibility checks

Run `python3 verify_total_rips.py`. The script is pure Python 3 standard library and enumerates every connected labeled simple graph with one to five original vertices. It constructs the once-subdivided graph separately from the total graph, compares all graph-distance-at-most-two adjacencies, builds complete clique chain complexes, checks all mod-two reduced homology dimensions, and independently executes the exact elementary-collapse sequence onto the old-vertex clique complex. The expected output is included as `verification_output.txt`.

The calculation is **not** claimed as proof for larger graphs; the all-graph mathematical argument is in the proof section of RESULT.md. No machine computation is used for the infinite quantifiers. Exact integral relative homology and symmetry signs follow from the explicit face classification and chain identification. Full 1991 Prisner source comparison remains unavailable and is not silently treated as cleared.
