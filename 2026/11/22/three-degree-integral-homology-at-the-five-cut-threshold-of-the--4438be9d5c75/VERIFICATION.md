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

A separate exact computation reconstructed the ordinary cut complex using K3□K4=L(K3,4): on each five-set, union the incident endpoints of the five selected bipartite edges, ignoring isolated bipartite vertices; the selected edges have connected line graph exactly when they lie in a single non-isolated component. Taking complements of the 264 disconnected sets and closing under subsets gave the frozen augmented face counts (1,12,66,220,492,768,666,264). The fresh calculation used the original signed simplicial boundaries, not the reported Morse matching or mod-two ranks. Integral column additions clear each ±1 pivot row, after which integral row additions clear its column without affecting the remaining block. In every degree the original boundary reduced to a unit diagonal and zero residual, with augmented ranks by degree 0–6 equal to (1,11,55,165,327,433,228). For each degree d, H_d embeds in coker ∂_(d+1), which is free by the unit invariant factors. Thus there is no torsion at any prime; rank subtraction in the augmented complex gives (0,0,0,0,8,5,36). The ranks agree with the frozen Morse counts and primitive rank-one B5 certificate. All the listed facets have cardinality seven, so the dimension is six and the complex is pure. The degree-four reduced group stays nonzero over any field, contradicting the empty-face Reisner condition; pure shellability would imply Cohen–Macaulayness. No homotopy wedge decomposition follows from these calculations.

## originality

PASS

The closest prior rook results are at different cuts or on different boards, and the grid tables with matching cut or dimensions are for Cartesian products of paths, in some cases for total rather than ordinary cuts. The line-graph interpretation is an exact alias, but does not turn this complex into the matching complex of K3,4. No equivalent or dominating exact result for ordinary Δ5(K3□K4) was verified. The bounded search and accessible comparisons, not absence of hits alone, support this assessment.

## value

PASS

This is a small, standard rook board beyond clique prisms, at the next cut size after the studied four-cut cases. The diagnostic question is whether its ordinary cut homology is top-concentrated or simple over the integers. Two successive nonzero degrees below the top show failure of even top-two concentration, and the exact primitive boundaries separate that effect from field-dependent torsion. The complete invariant provides a comparison case for ordinary cut complexes on clique products and line graphs and disproves shellability and Cohen–Macaulayness on this concrete board; the value is not just the number of disconnected sets.

The dated certificate retains the supplied scientific assessment, sources and limitations.
