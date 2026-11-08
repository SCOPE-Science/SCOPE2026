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

# Verification of the finite certificate

Run `python3 verify.py` with Python 3.9 or later. This exact, deterministic program uses only the standard library and checks every edge, graph distance, Boolean-level metric identity, Rips face, Morse pair, codimension-one Hasse incidence and directed acyclicity for the two nontrivial certified scales. No probability, timeouts, sampling or external calls are involved.

Expected relevant output: radius two gives 260 faces, 120 matched pairs and critical cells in dimensions zero and two (one and nineteen, respectively); radius three gives 3200 faces, 1599 pairs, one critical vertex and one critical three-cell. Each complete directed Hasse graph is topologically sorted, ending in `Hasse_DAG=PASS`. The program then checks the ten antipodal distance-five pairs and reports `VERIFY_OK`. The corresponding exact integral homotopy claims use the discrete Morse theorem, not a separate numerical-only inference. The direct metric comparison is to the two middle levels of the five-cube.

Boundaries: this verifier proves only the specified 20-vertex case. It does not check every possible isomorphism in related graph families, and no independent review was performed. Published scale-two coverage is acknowledged rather than recertified as a new result.
