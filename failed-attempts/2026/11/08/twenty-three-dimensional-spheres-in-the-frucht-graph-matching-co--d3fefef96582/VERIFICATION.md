---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-19.md",
      "INDEPENDENT_AUDIT_2026-11-19.json"
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

At the assigned frozen eight-blob tree, direct reading fixed the graph by 12-entry LCF and explicit 18 edges. Independent self-authored recursive include/skip enumeration returned 1,025 nonempty matching faces with f-vector (18,117,333,397,152,8) and 21/104/8 facets at sizes 4/5/6. Independently reconstructed pivot sequence [9,3,4,17,15,1,0,8,13,12,2,14,10,16,6,11,5,7] gives 502 disjoint cover pairs, leaving 1 dimension-zero and 20 dimension-three critical cells; checked all 3,629 covers and Kahn sorted all 1,025 vertices with standard reversed orientation. Acyclic Forman matching implies CW type with one point and 20 three-cells, hence integral wedge of 20 S^3. Finite exhaustive proof applies to this fixed graph, not an infinite family. The saved log alone was not relied upon.

## originality

FAIL

The complete published Oct18 Resultary/SCOPE Frucht matching-complex theorem already proves exactly the assigned integral wedge of twenty 3-spheres, using the same 1,025-face and 502-pair Morse construction. Different graph-edge labeling was independently proven isomorphic. Publication commit 2026-10-25T19:49:48Z precedes assignment source commit 2026-11-08T17:30:20Z. Other prior same-object records reproduce the result and one extends it to all one-edge deletions; no original claim remains.

## value

FAIL

Exact integral homotopy of the natural canonical asymmetric cubic Frucht graph is a meaningful finite topological invariant; the nonpure 5-dimensional complex and complete acyclic Morse compression are substantial computations in isolation. However the entire mathematical invariant, exact sphere multiplicity and homotopy (not merely Betti numbers) were established in an earlier accessible public source; new pivot ordering and independent code are reproducibility, not a new mathematical gap or distinct unknown exact fact. No mathematically independent contribution remains.

The dated certificate retains the supplied scientific assessment, sources and limitations.
