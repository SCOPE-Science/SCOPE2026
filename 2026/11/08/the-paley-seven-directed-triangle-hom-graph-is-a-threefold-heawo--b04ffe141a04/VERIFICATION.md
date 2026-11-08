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

# Verification
Execute `python3 verify_cover.py` using standard Python 3. The script reconstructs all nonempty three-coordinate Hom cells and checks the common-neighbor property, the exact face counts \((42,63)\), degree three at every vertex, connectedness by a complete 41-edge spanning tree, free rotation on graph cells, orbit quotient size \((14,21)\), local graph-covering condition, the Fano difference-set incidences and both rational character multiplicities.

The recorded output `verification_output.txt` is reproduced verbatim by executing the file supplied with the result. This establishes a finite exact certificate; no third-party independent audit, generalization to larger tournaments, or integral lattice decomposition is asserted.
