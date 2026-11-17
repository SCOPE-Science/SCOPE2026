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

# Verification of the frozen-state energy law

The exact verifier constructs the sixteen transfer states directly from the local four-neighbor rule, checks the sixteen-degree characteristic identity by symbolic polynomial equality, checks the Lucas count at even circumferences four through twelve, and compares selected **weighted** energy distributions. The independent C++17 program evolves the two colored half-steps of Q2R directly on every binary configuration for even circumferences four, six, eight and ten, checks each fixed state, tallies its bond energy and tests energy reflection. Both were executed, and the package includes their original output files. These finite tests are a reproducibility check; the exact transfer bijection, determinant and gauge involution prove the all-circumference claims.

Dependencies are documented in `requirements.txt` for the symbolic verifier; the direct checker uses a standard C++17 compiler. No external mathematical certification was performed. Results depend on counting two vertical directional bonds at height two; using a simple ladder without this multiplicity changes the problem.
