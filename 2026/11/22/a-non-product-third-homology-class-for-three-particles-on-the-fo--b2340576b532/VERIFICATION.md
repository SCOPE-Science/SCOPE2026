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

The natural integral comparison and reduction of the Świątkowski complex apply to the one-dimensional Q4 graph with no isolated vertices. At weight three and degree three exactly three distinct vertices supply half-edge differences (three choices each); the 15,120-column Koszul map has no incoming degree-four boundary. The torus identification uses the tensor product for the disjoint union of the three embedded cycles, then the natural map of the inclusion into Q4. On an oriented cycle the weight-one generator is the sum of outgoing minus incoming half-edges, with boundaries telescoping; their tensor product represents the torus fundamental class, up to overall sign. Bipartiteness and girth four force the four stated length patterns since at most sixteen vertices are available. Independent exact reconstruction gave 24, 128, 696 cycles of lengths 4, 6, 8, and 152, 576, 240, 144 tori by type. Every product's signed integer boundary was zero. Rank of the differential modulo three was 14,991, giving an upper bound of 129 for the rational kernel. Exact rational reduction gave rank 128 over all 1,112 products, already obtained from square triples. The 1,475-term witness has integral zero boundary, coefficient magnitudes at most two and nonzero rational remainder at coordinate 13,278. This supplies the 129th direction and proves equality; the top integral homology is free as a subgroup of a free group. The mod-three witness check corroborates independence but is not used in place of exact rational rank for the torus span. No claim about quotient torsion or primitivity follows. Uploaded code was inspected, not executed.

## originality

PASS

The comparison complex, product construction and phenomenon of non-product homology all predate the finding. The new claim is graph- and particle-specific: exact rank defect one in Q4 even after every disjoint-cycle torus is included, with a witness. The inspected results for neighboring configurations and other graphs do not imply these ranks or this obstruction.

## value

PASS

The four-cube is a canonical highly symmetric graph with plentiful disjoint cycle products, and the known two-particle result has full generation. The three-particle calculation shows that the analogous natural generating family misses a rational direction even after every possible cycle length is included. The exact rank and explicit witness distinguish a structural obstruction from an integral-index artifact or an incomplete census of square tori.

The dated certificate retains the supplied scientific assessment, sources and limitations.
