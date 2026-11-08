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

# Reproduction of the exact top-homology calculation

Run `python3 verify.py`. The program uses no third-party libraries, generates the dodecahedral graph from its generalized Petersen formula and enumerates all degree-three generators in the reduced Świątkowski model.

The actual checks comprise the graph incidence and vertex degrees, the chain-group sizes, the 9,120 signed boundary columns, exact integer elimination using 9,094 unit pivots, all 26 complete integer null-cycle witnesses, a signed local check that the differential squares to zero, and an independent characteristic-two rank. `verify.stdout` records the deterministic output and the SHA-256 digest of the integral-cycle witness list.

The verifier proves the integer rank of the chosen finite differential, not the general comparison theorem; the latter is used with its published hypotheses. An all-modulo-prime computation alone would not prove an integral rank over every characteristic, and no such substitution is made. The homotopy type and lower integral homology groups are not determined by this check.
