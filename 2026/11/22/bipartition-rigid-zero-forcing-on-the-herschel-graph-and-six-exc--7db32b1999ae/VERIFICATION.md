---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

For the explicit eleven-vertex graph, a forcing set must hit every nonempty fort, since otherwise the first force into it is impossible; if closure stalls the final white set is itself a fort. Hence testing the inclusion-minimal forts is sufficient. An independently written bounded replay, branches/1791af5a-f25c-4121-a0c7-8c5fcc027d75/herschel_replay.py, exhausts the 2,047 candidate forts and finds 558 forts, 30 inclusion-minimal. The resulting hitting sets have minimum size five, with 114 optima, all with signature (3,2) in the stated bipartition. An edge slide necessarily changes this signature, whereas jumping is Hamming distance two on the optimum masks. The independently regenerated 540 jump edges give a connected graph with every eccentricity five and pair counts (540,1938,2664,1167,132). Subtracting half symmetric difference gives (6183,252,6) for excess 0,1,2; the six excess-two pairs all have exchange distance four and Johnson distance two. Exhaustive degree-preserving permutations yield 12 automorphisms, under which those six pairs are one orbit. The replay matches the exact exceptional mask pairs in certificate.json, lines 2375–2408. The supplied verifiers were inspected, not run. The conclusion is a complete classification of the stated ordinary rule on the supplied labeled graph, not of other forcing rules or graph families.

## originality

PASS

There is close prior catalogue coverage of both patterns—slide freezing from a bipartition-count constraint and distance-four exchanges with Johnson distance two—but not located on the stated Herschel graph. The structurally similar Möbius–Kantor results deserve explicit credit as precedents for the type of claim, not as implications for an eleven-vertex graph. The exact Resultary match for the Herschel theorem is this frozen record itself. The supported distinct content is the explicit Herschel roster signature and exact exchange metric, particularly the single six-pair excess-two orbit.

## value

PASS

The smallest non-Hamiltonian polyhedral graph is a natural fixed benchmark for reconfiguration under an observability rule. An exact obstruction freezes every edge slide despite connected unrestricted movement, and the unique orbit of six two-move detours gives structural information beyond a minimum-set count or a generic diameter bound. The full finite metric also distinguishes the example from close graph analogues without claiming a family theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
