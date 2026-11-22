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

# Reproducibility and evidence

Run `python3 verify.py` with Python 3 and SymPy installed. The included checker constructs the fifteen duads, fifteen perfect matchings and thirty-vertex Laplacian deterministically. It verifies exact integer eigenvalues, the base Smith factors, the matrix-tree count, the 720 label permutations as actual graph automorphisms, and all eleven Frobenius types. For each type, both deleted-root choices agree; the Smith form of the full rectangular presentation and of its column Hermite normal form agree. The printed final success marker is `IGUSA_CREMONA_RICHMOND_FIXED_CRITICAL_GROUP_VERIFIED_OK`.

The checks run using exact integer operations and are reproducible from the included source. The graph-to-Igusa identification and perfect-pairing duality are supplied mathematically in RESULT.md; machine computation alone does not certify those standard structural steps. No external verification, external reviewer, or formal proof assistant was used.
