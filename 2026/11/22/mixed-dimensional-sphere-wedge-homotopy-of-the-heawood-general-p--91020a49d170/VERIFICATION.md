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

Execute `python3 verify_heawood_gp.py` with Python 3. The verifier needs no dependencies, input files, network access, or external certificates. It constructs the Fano point–line incidence graph with line incidence labels \(\{i,i+1,i+3\}\) modulo seven and calculates exact integer shortest-path distances.

It visits all \(\binom{14}{3}=364\) triples; identifies 210 forbidden triples; tests all \(2^{14}-1=16383\) nonempty vertex masks; verifies the face vector \((14,91,154,147,56,14,2)\); forms 225 deterministic vertex-toggle pairs; and certifies 28 critical faces distributed \((1,21,0,6,0,0,0)\) by dimensions zero through six. Every one of the 1,610 Hasse incidences is examined. The reversed-matching directed graph is shown acyclic because all 478 nodes are removed in a complete topological sort.

A second, independently implemented signed simplicial boundary calculation, using finite-field elimination, returns ranks \((13,57,97,44,12,2)\) over each of the prime fields of orders 2, 3, 5 and 101. Those ranks alone do **not** prove integral torsion-freeness or an integral wedge type. The discrete-Morse critical-cell CW theorem and vanishing of \(\pi_2\) for any graph provide the integral homotopy argument.

The verifier reports:

```
PASS: 210 forbidden triples; 478 faces; 225 acyclic pairs;
      critical cells (dimension:count) = {0:1, 1:21, 3:6};
      478/478 Hasse vertices topologically sorted; 1610 arcs;
      signed chain ranks agree over F_2,F_3,F_5,F_101.
```

Limits: exact finite Heawood graph only; no assertion about other finite projective planes, full automorphism representations, independent audit or global priority of discovery.
