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

# Exact verification and reconstruction

Execute the two standalone scripts in this package using only Python 3 standard library:

```
python3 verify_line_graph.py
python3 verify_coordinates.py
```

**Line-graph construction.** The first script makes the cuboctahedral graph as the line graph of the labelled three-cube, identifies the six old cube-square faces, branches on all twenty-four directed cuboctahedral edges and retains precisely the orientations with two outgoing arrows per vertex. Its assertions establish exactly 600 states; per-square flippability 192; labelled active-face counts 144 for the empty set, 24 per singleton, 8 per distinct pair, 16 per transversal triple, 64 for all six and zero otherwise. It constructs the actual legal-move adjacency graph, proves by exhaustive BFS the component histogram 144, 72, 30, 16 and 1 in dimensions 0, 1, 2, 3 and 6; and checks 576 edges. An exact integer polynomial of degree eleven annihilates the kinetic adjacency on **every one** of its 600 standard-basis vectors. This annihilator is a spectrum consistency check; spectral multiplicities derive from the explicit hypercube decomposition.

**Independent coordinate construction.** The second script independently constructs vertices by coordinate permutations of \((0,\pm1,\pm1)\), determines edges by Euclidean squared distance two, identifies square faces by fixed coordinate, and recursively assigns one of sixteen local orientation words to each of six faces. Its outgoing-arrow pruning is exhaustive, not sampling. It independently computes the identical joint-flippability coefficients, 600 states, 263 components and per-face marginal. Hypercube decomposition yields the exact isotropic eigenvalue/multiplicity table: \(\pm6:1\) each, \(\pm4:6\) each, \(\pm3:16\) each, \(\pm2:45\) each, \(\pm1:120\) each, \(0:224\). It also verifies \(\operatorname{Tr}(H_{\rm kin}^2)=1152\) and \(\operatorname{Tr}(H_{\rm kin}^4)=9936\) with unit couplings.

**Noncomputational proof obligations.** The displayed coefficient formula in RESULT.md matches both programs because each square edge is assigned once and the vertex coefficient enforces the complete ice rule. The disjoint-edge reversal lemma proves the graph is a disjoint union of hypercubes, and a tensor-product eigenbasis gives the weighted kinetic and RK statements for every positive choice of six couplings. No numerical extrapolation is used to prove the weighted formulas.

**Limits.** Script assertions are exhaustive only for this specified 12-vertex graph. They do not certify experimental preparation, larger graphs or independent scholarly originality. The zero-mode statements concern only the defined square-only RK operator, not a Hamiltonian with additional triangular flips.
