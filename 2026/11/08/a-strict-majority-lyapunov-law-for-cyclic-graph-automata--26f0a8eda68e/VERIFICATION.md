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

Run `python3 verify_majority.py` using Python 3 with only its standard library. The script constructs graphs and computes the simultaneous successor-neighbor update directly. The successful checks cover:

- All 1,098 labeled undirected simple graphs of sizes 2–5, with all 1,319,754 initial configurations for three and four colors, at the smallest strict-majority threshold.
- All 5,001 nonempty eligible partial-update selections for three colors on every labeled graph of sizes 2–4.
- Random configurations and graphs of sizes 8, 12, 18, 30, and three-color Moore toroidal grids of sizes 3, 4, 5, and 7.
- Universal sharpness families \(K_{m,m,m}\) and the binary exception \(K_{m,m}\) for stated values of \(m\).

Every simulated nonempty update checks the quantified Lyapunov inequality, and each full trajectory checks the global edge-budget upper bound. The checker reports its counts and terminates normally on success. These checks were executed successfully on the embedded script's bytes in this package. Finite exhaustive and random checks cannot replace the analytical proof for arbitrary finite graphs.

The unresolved questions include the borderline half-degree contact rule, potential stronger finite-graph results in older inaccessible sources, arbitrary infinite networks and the best possible worst-case constant on Moore tori.
