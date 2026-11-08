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

# Reproducibility and limits

The exact all-graph result is proved analytically in `RESULT.md` from the exhaustive local three-spin composition table, its sharp attainment by a three-edge-coloring, and graph bijections for the two coexistence sets. Computational checks are finite consistency tests, not replacements for the proof.

With Python 3 and no external packages, run:

```
python verification/exhaustive_cube.py
python verification/combinatorial_cube.py
python verification/other_cubic_graphs.py
```

The cuboctahedron verifier visits every one of its \(3^{12}=531441\) classical spin states, constructs all exchange bonds directly from cube-edge incidence, and tests the six strict-phase samples plus both boundary samples with rational arithmetic. The second verifier independently enumerates every cube-edge subset, its matching counts, its even-cycle contributions, and every admissible labeled proper edge-coloring. The third checks every state on two distinct cubic bases, \(K_4\) and \(K_{3,3}\), without extrapolation. Expected final markers are `EXHAUSTIVE_CUBE_OK`, `COMBINATORIAL_CUBE_OK`, and `OTHER_CUBIC_GRAPHS_OK`.

Only the displayed uniform, classical, finite-graph Hamiltonian is established. Arbitrary-field ground energies are exact; complete degeneracies at unspecified coexistence loci, temperature-dependent physics, and graphs without three-edge-colorings remain outside scope. Independent scientific audit has not been performed.
