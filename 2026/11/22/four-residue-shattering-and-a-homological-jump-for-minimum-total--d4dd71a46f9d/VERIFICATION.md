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

Every open-neighbor constraint is an edge-covering constraint on the step-two graph, so complementing the minimum vertex covers gives the maximum independent sets and preserves shattering. Maximum sets split by component. On an even component the only choices are the two alternations, also true of the single-edge components at n=4. On an odd cycle of length m, a maximum word has exactly one 00 edge and no 11 edge. For a nonadjacent pair, prescribed endpoint bits force odd 00 parity on exactly one arc. Use alternation on the other and insert a duplicated zero in an alternating word shortened by one edge on the odd-parity arc (it has length at least two). Adjacent pairs fail the 11 trace. For three queried vertices, the mod-two endpoint differences L_i-1 are consistent because the three arc lengths sum to odd m; they force at least one 00 on each arc, impossible. This proves the full support test, not just the degree bound. The odd-component complex is the graph complement of the cycle, with no filled triangles: it is connected for m>=5 (minimum degree m-3 precludes disconnectedness for m>=5), and a spanning tree gives wedge rank E-V+1. The triangle is discrete. For two components the support counts multiply and the complexes join; collapsing the based contractible part of the join gives suspension of the smash and hence the claimed sphere dimensions and squared ranks, including n=6. The supplied brute force checker was inspected, not executed; its finite traces and Euler data are not the proof of unrestricted homotopy.

## originality

PASS

The scalar fixed-weight VC result is prior coverage and expressly excluded from the contribution. Best of the inspected statement-level evidence, the exact optimum-only support criterion and ensuing support polynomial and homotopy are distinct. Counting and homotopy once the support lemma is proved are elementary, not claimed as new general techniques.

## value

PASS

For a standard optimization family, the all-support invariant answers every query feasibility question; cardinality counts of optimizers and a scalar VC bound cannot do that. The support graph and its parity joins explain a concrete jump from circles to three-spheres and give their exact integral ranks. The value lies in this complete description, not a claim about an arbitrary graph or unrelated domination notions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
