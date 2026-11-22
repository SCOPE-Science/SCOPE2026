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

# Reproducibility and verification

Run \(\texttt{python verify.py}\) using Python 3 and only its standard library. The script does not read external data or require any packages. It constructs the complete split graph's edge list in a fixed order, enumerates Prüfer sequences to obtain spanning-tree supports, runs an exact integer Walsh-Hadamard transform, and independently evaluates signed Laplacian cofactors by the Bareiss algorithm. It checks all characters for triangular cores with one through four independent vertices and for a five-vertex clique with one independent vertex, then tests dyadic divisibility and randomly selected (deterministically seeded) opposite-sign leaf-pair identities at larger odd cores. The recorded run completed \(248034\) exact assertions with all tested cases passing.

This is finite evidence only. The unrestricted parity theorem, dyadic divisibility and cancellation propagation use the mathematical proof in RESULT.md. No computational experiment is offered as proof of an infinite assertion. The odd-order nullity is generally only lower bounded; no exact classification of all its zero characters is claimed.
