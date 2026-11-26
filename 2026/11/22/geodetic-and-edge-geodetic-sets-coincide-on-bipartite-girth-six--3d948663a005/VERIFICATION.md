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

For a geodetic S, each unselected vertex has a selected neighbor on a witnessing geodesic of length at most three. An edge with two selected ends witnesses itself. With one selected end, either the witnessing path already uses the edge, or the selected end and a different selected neighbor of the unselected end are joined by a two-edge geodesic by bipartiteness. With neither end selected, selected neighbors at the two ends give a three-edge path whose endpoints are distinct and opposite in the bipartition. An edge shortening it would form a 4-cycle. The reverse implication uses connectedness and the nonempty edge set, including the single-edge case. Point/line incidence of any finite projective plane satisfies these hypotheses. Independently replayed the Fano census with projective coordinates over F2 and an incidence criterion, rather than either frozen geodesic checker: an unselected point is covered iff it is incident to two selected lines, or is incident to a selected line and some selected point is off that line; dually for unselected lines. Exhausting all 16384 masks, then removing masks with a valid single deletion, reproduces the full polynomial and exactly the 21+14+28+2 constructed minimal masks, not just size counts. Independent replay: python3 /workspace/checks/3.py. K3,3 with two selected vertices in each part verifies that 4-cycle exclusion cannot simply be dropped.

## originality

PASS

The defensible distinct claims are the equality of whole feasible families on the stated graph class and, for Heawood, the exact all-set polynomial and the classification beyond the already known 21 minimum flag bases. In the inspected primary passages and relevant Resultary statements, no stronger theorem or exact census covers those claims. The established plane-incidence geodetic basis theorem is expressly credited.

## value

PASS

Identifying equal feasible-set families for two distinct natural cover notions on an infinite incidence class yields genuinely more information than any equality of scalar minima. The 4-cycle witness gives a useful scope boundary. The Heawood specialization gives a motivated complete model: the nonpure minimal families have sizes four through seven and the largest are the two full shores, while the exact polynomial describes all subsets, not just optima. The already established size-four data are not the value basis.

The dated certificate retains the supplied scientific assessment, sources and limitations.
