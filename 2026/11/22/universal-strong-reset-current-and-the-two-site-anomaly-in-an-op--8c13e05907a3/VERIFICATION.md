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

# Reproducible checks and limits

The accompanying `CHECK.py` reconstructs the finite-state generator from the specified elementary transitions, calculates stationary measures for finite instances, verifies nonnegative normalization and zero stationarity residuals, and checks equality of injection and extraction currents. Symbolic two-site elimination independently checks the limit coefficient \(\alpha+\beta\). Across the tested finite sizes and rates, 353 finite/symbolic assertions passed.

For arbitrary finite \(L\), the theorem rests on the directed spanning-tree degree argument and exact stationary balance equations, not finite enumeration. Computational assertions neither prove an infinite family nor establish publication priority. Dependencies: Python 3, NumPy, SciPy, SymPy. Run `python CHECK.py` in the package directory; no external data are required.
