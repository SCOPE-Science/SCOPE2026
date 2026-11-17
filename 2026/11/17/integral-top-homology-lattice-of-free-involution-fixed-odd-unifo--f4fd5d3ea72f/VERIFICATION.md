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

# Reproducibility and logical scope

Run `python3 verify.py` with Python 3.8 or newer; it uses only the standard library. The expected canonical output is embedded as `verification_output.json`. The verifier reconstructs original hyperedge involution-orbits at low parameters, rather than assuming the phase-fiber formula as input. It enumerates component and cycle counts for the six-pair case and checks boundary ranks over four prime fields for several discrete-join blocks. These are exact finite calculations, not external expert certification or a complete proof of the infinite theorem.

The general proof uses only elementary barycentric-coordinate geometry, combinatorial matching support, and an integral top-chain decomposition. The signed induced representation follows from the actual permutation of oriented top simplices. The verification does **not** establish absence of lower-dimensional torsion, a general homotopy type, or precedence over every unindexed result.
