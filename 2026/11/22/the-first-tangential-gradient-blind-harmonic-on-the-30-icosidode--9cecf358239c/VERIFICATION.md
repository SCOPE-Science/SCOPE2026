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

# Reproducible exact checks

Run `python verify_h3.py` (requires SymPy). A successful run prints exactly six ranks 3, 5, 7, 9, 11, 12, and the corresponding six nonzero determinants 10, 46, 22, 60, 5, 61 in the field of 101 elements, plus the invariant value 85 at the first coordinate axis. All 30 exact edge directions and 90 tangential-gradient coordinates are checked by the script.

The finite-field certificate proves rank lower bounds in characteristic zero, not equalities by itself. A separate mathematical argument uses an icosahedrally invariant nonzero degree-six solid harmonic and the half-turn symmetry at every edge direction to prove the necessary rank upper bound. Each degree 1–5 has the maximal possible lower rank. Degree zero is excluded because its gradients are identically zero. Degrees greater than six and any quantitative stability constant are not established.
