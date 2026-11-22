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

Run `python verify.py` (Python 3.9+, standard library only). No external data, package installation, or network connection is used.

The program reconstructs \(\operatorname{KG}(5,2)\), computes every shortest path distance after each fault, and enumerates the simplicial general-position faces. The three forbidden-triple counts are 30, 50 and 33, with nonempty face totals 260, 169 and 123. Deterministic vertex toggling yields respectively 129, 82 and 60 matching pairs and the critical-cell count vectors reported in `RESULT.md`.

For each of the 860, 482 and 336 Hasse incidences, matched arrows are reversed and the entire directed graph is topologically sorted, visiting all faces. The checker calculates all Morse differentials through exact signed integer face-incidence expansions and confirms each is zero. A separate calculation of full simplicial boundary ranks over \(\mathbb F_2\) confirms the displayed Betti numbers; it is not used to infer torsion-freeness. The integral homotopy conclusions follow from acyclic integer Morse reduction and degree-zero attaching maps to \(S^1\).

The checker also enumerates all 120 permutations of the five ground labels, proving the representative edge and vertex faults exhaust their respective isomorphism orbits. The check covers only the precisely defined finite graphs; it does not independently establish literature originality or verify extensions beyond the claimed cases.
