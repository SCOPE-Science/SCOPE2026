---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The cube's translations and coordinate permutations act transitively on edges, so the graph with edge {0,1} deleted represents all faults. The independent bounded check enumerated all 255 nonempty vertex masks by two cycle tests and confirmed the exact face vectors (8,17,10,2), (8,28,36,14), (8,28,56,60,30,2), (8,28,56,66,40,6) in threshold order. Each sequential-vertex pairing was a matching of codimension-one incidences; topological sorting accepted all vertices of the full oriented Hasse graph at each stage (37,86,184,204 face nodes, respectively). Critical masks in hexadecimal: 01 and {18,24} at degree bound zero; 01 and {2c} at bound one; 01 and {3e,7c,bc} at bounds two and three. The latter three masks each have five vertices. The discrete-Morse CW models have one vertex and cells only in a single positive dimension, making their attaching maps constant and giving the stated wedge homotopy types without relying on field homology. All ten listed collapse pairs were checked in order for codimension one, unique strict coface and exclusion from the target; the 184-face residual is exactly the degree-two subcomplex. Maximal degree three makes this the last transition, and the collapses prove the actual inclusion is a simple-homotopy equivalence. Carnero Bravo's intact formula at n=4 gives one S³ and four S⁴. No map from the intact cube is inferred from the two types.

## originality

PASS

The intact crown classification and missing-edge biclique connectivity are known. The precise nonregular crown fault's degree-bounded filtration and the relative ten-collapse certificate are not supplied by the inspected statements. The claim is provisional with respect to unindexed exact computations.

## value

PASS

The three-cube is a canonical small crown and already has a mix of sphere dimensions; its unique edge-fault orbit is a natural complete experiment in stability of that classification. The exact disappearance of degree three, decrease in degree four, and genuine inclusion-level collapse answer distinct questions beyond a single Betti number. This is useful as a benchmark for a larger fault theory without claiming one.

The dated certificate retains the supplied scientific assessment, sources and limitations.
