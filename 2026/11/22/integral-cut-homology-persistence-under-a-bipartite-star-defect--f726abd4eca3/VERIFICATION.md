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

# Reproducible checks

Run `python3 artifacts/check_star.py` and `python3 artifacts/check_maps.py` from an extracted package (Python standard library only). The scripts independently enumerate induced connected triples, faces of the Alexander dual, cone decomposition and exact mod-two reduced homology. The second enumerates 54 induced homology maps in two degrees. Their output captured at packaging is in `artifacts/verification_output.txt`. The scripts independently recompute the same low-dimensional cases, but finite mod-two calculations do not establish the universal integral theorem; the explicit join/link homotopy argument and integral naturality establish it. No independent audit was requested or performed.
