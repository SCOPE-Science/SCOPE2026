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

From this directory, install the `requirements.txt` dependency in an ordinary Python 3 environment and execute:

```
python verify_geometry.py
python verify_classification.py
```

Both programs were executed successfully using SymPy 1.14.0. `verify_geometry.py` reconstructs the line equations in exact quadratic arithmetic, enumerates all pairwise projective intersections, verifies the three conic-containing and three line-only ordinary triple points, the three additional ordinary nodes, all three line–conic tangencies, and the total Tjurina number \(36\). `verify_classification.py` exhausts abstract admissible quadruples of ordinary triple intersections among six lines (eliminating the four-triple case), factors the normalized dual-conic incidence equations, and checks the two conjugate solutions are in one coordinate-permutation orbit.

The scripts are independently re-runnable, but they are supporting exact computations, not an infinite case enumeration. All unrestricted universal implications are justified in the proof's counting and normalization arguments; the proof does not require a claim of external, independent verification. The corresponding earlier published degree-eight near-freeness computation is acknowledged rather than independently re-certified as a new theorem.
