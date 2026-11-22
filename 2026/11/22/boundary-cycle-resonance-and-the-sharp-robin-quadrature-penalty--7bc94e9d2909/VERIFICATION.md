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

Run `python verify.py` under Python 3 with SymPy installed. The checker constructs the four-node \(Q_1\) stiffness, mass, load, and boundary sampling matrices from their actual symbolic basis functions; evaluates edge mass integrals; verifies the exact midpoint and exact-boundary solutions; determines the sampling determinant; and takes the singular two-parameter symbolic limit. It also evaluates 42 exact cyclic sampling ranks for lengths \(3\) through \(16\), including midpoint resonance, single-node imbalance, and two balanced deviations. Execution returned `VERIFY_OK 64`.

The analytic proof covers arbitrary finite compatible polygonal boundary cycles and all relevant parameter sequences. The 64 checks alone do not establish universal correctness, mathematical novelty, or independent validation. The symbolic computations are reproducible using this accompanying file with no external data.
