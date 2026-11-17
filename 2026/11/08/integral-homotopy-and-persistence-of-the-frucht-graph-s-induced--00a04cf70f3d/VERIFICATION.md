---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

The 12-vertex Frucht graph is reconstructed from the exact LCF jumps and 18 cubic edges. Independent exhaustive union-find and maximum-induced-degree enumeration over all 4096 subsets gives augmented face counts 169,825,2335,2542 for d=0,1,2,3, and acyclic complete Hasse matchings with 82,411,1164,1267 pairs. Exact signed Morse boundaries vanish except at d=3, ∂7(critical mask 3828)=critical mask 3762 with unit coefficient, yielding integral wedges ∨3S2, S3, (∨4S6)∨S7, (∨3S6)∨S7. For the actual F2→F3 inclusion, independently lifted genuine integral cycles and computed projections give masks 926→926, 3308→0, 3506→3506, 3762→3762(boundary in F3), and 1782→1782. Thus H6 map has primitive rank two with torsion-free cokernel; H7 map is an isomorphism, giving asserted integral interval multiplicities. A separate original-simplicial mod-two boundary quotient yields inclusion H6 rank2. Exact cutoff d≥3 follows from cubicity. This is an exhaustive finite proof for one graph, not an extrapolation.

## originality

PASS

PASS best of knowledge: earlier Frucht higher-independence filtration is defined by component order rather than induced forest plus degree bound, coinciding only at stages F0 and F1. Its full paper does not imply the degree-2/3 Frucht forest wedges, actual degree-six transition map or new degree-six birth. The earlier Frucht independence/deletion result establishes only d=0. Published Heawood forest filtration uses a different graph and all strict degree maps vanish, unlike the nonzero Frucht persistence maps; general Carnero Bravo forest filtration framework has no exact Frucht classification in examined material. Residual unindexed literature risk is disclosed.

## value

PASS

The Frucht graph is a natural small asymmetric cubic test case for a genuine induced-forest degree filtration. Complete integral homotopy stages, primitive nontrivial H6 transition and an essential H7 class are not routine normalized data: the death-and-birth profile cannot be deduced from stage Betti ranks alone and contrasts structurally with symmetric-graph examples. A researcher studying integral forest persistence could need these precise values.

The dated certificate retains the supplied scientific assessment, sources and limitations.
