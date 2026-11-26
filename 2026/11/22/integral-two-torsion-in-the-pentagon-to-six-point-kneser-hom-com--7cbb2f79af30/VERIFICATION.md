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

For an ordinary Hom cell take the union of underlying ground-set pairs in each nonempty coordinate. Coordinate support sizes are between 2 and 4, and adjacent coordinate supports must be disjoint, which is necessary and sufficient for all adjacent cross-pairs to be graph edges. Independently enumerating such cyclic supports, and every exact-support subfamily at each coordinate, gave cell counts (6570,28350,40500,22950,5400,450). Valid free facets with one current top coface removed all cells in grades 5, 4 and 3 with 450, 4950 and 18000 elementary pairs, respectively. Stopping before any grade-2 removals gave the different 2-complex with counts (6570,28350,22500). The one-skeleton is connected; its spanning-tree quotient has 21781 loops. With signed product boundaries, exact unit row/column elimination gave 21771 units. All residual columns are rational multiples of a nonzero column, verified by exact cross multiplication, and their entries have gcd 2, so there is one further nonzero Smith factor 2. Hence the boundary rank is 21772; H_1 has free rank 9 with precisely Z/2 torsion and H_2 is a free kernel of rank 728. H_0=Z and there are no higher groups. The independent method did not rely on the recorded mod-two calculation to determine integral torsion.

## originality

PASS

The complete unreduced integral table for source C5 and target KG(6,2) is distinct from the verified close comparisons. These include the edge-source Kneser neighborhood case, the pentagon with a complete target, the pentagon with the smaller Petersen Kneser target, and other complexes on the same graph. This is a bounded assessment rather than a claim of global priority.

## value

PASS

Six is the first ground-set size supporting three mutually disjoint pairs, so this is a natural next test beyond the Petersen target with the odd-cycle source fixed. The exact degree-one order-two obstruction in the ordinary, unquotiented Hom complex rules out a wedge-of-spheres type, which cannot be seen in its rational homology. Its accompanying ranks and vanishing give a concrete benchmark for odd-cycle Hom theory, beyond the edge-source classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
