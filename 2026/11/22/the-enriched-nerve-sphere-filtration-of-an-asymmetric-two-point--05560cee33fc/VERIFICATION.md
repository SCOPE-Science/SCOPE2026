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

The directed triangle inequality makes length sublevels simplicial; degeneracies are exactly tuples with an adjacent repeated vertex, leaving two alternating cells per degree. Counting directed steps places the even pair at ms and odd cells at ms+a and ms+b. The two surviving end faces give the asserted signed boundary. Independently split the filtered augmented integral chains using u_n and z_n=v_n-u_n for n even, z_n=v_n+u_n for n odd, and z_0=q-p. The change of basis is unimodular when the second cell enters, and d u_n is a unit times z_(n-1), d z_n=0. The resulting two-term elementary summands give exactly the finite bars (drop zero-length intervals), plus one essential bar without augmentation. For homotopy, the first edge connects the vertices and the second gives the circle. Whenever the preceding stage is a sphere, the first new cell has degree one in absolute value by the same primitive boundary; for attaching spheres of dimension at least one this is a homotopy equivalence onto the preceding sphere up to homotopy. Its cofiber is contractible; the next cell then yields a sphere one dimension higher. Ties may be separated for this attachment argument without changing the actual inclusive filtration. All finite bars have length a, so their diagonal match costs a/2; the first reduced death and first positive-degree birth recover a and b. Inspected checker and recorded 68-instance outcome; the F2 computation up to degree ten does not supply the all-degree integral proof and was not rerun.

## originality

PASS

The levelwise classification and barcode together for two arbitrary positive directed costs are not covered by the inspected precedents. The symmetric barcode is explicitly covered over F2 by Melodia's stronger uniform-metric calculation (specialize to m=2 and rescale). The symmetric low-scale sphere stages are also exact special cases of other catalogue records. None gives the asymmetric intervening contractible stages or the asymmetric all-degree integral filtration and recovery result.

## value

PASS

This is the minimal example in which nonreversibility splits a two-cell arrival and introduces a repeating interval with trivial homotopy. The calculation gives a complete integral benchmark in every degree, not just a list of critical lengths or field Betti numbers, and exhibits exactly what the full barcode detects that the distance to a point loses. These directed distinctions survive the substantial symmetric prior coverage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
