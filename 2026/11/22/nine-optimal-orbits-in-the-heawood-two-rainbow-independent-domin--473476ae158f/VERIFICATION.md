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

For a fixed zero set the source correctly uses a separate two-coloring choice on each connected component of the positive induced subgraph, including isolated vertices, and requires each zero to see both named colors. I independently used maximal cliques in the complement of the Heawood prism. Under the label-to-layer correspondence, a prism independent set uses at most one copy of each vertex; every used fiber is dominated by its vertical edge, and each unused fiber needs domination in both layers. Thus maximal independent sets of the prism give exactly the labeled functions, with weight preserved. The new census gave coefficients 868,168,42,28,2 at weights 8,9,10,11,14 and zero elsewhere, totaling 1108. It reproduced the optimum point-zero counts (70,84,168,224,168,84,70). The connected incidence graph's automorphisms either preserve or reverse the bipartition; testing every point-to-side bijection and uniquely recovering the line images from neighborhoods yields exactly 336 automorphisms. Acting on the 868 optima without exchanging the named colors gave the complete nine-orbit TSV, including all specified lexicographic representatives and sizes.

## originality

PASS

The invariant and the prism correspondence are known. The inspected same-invariant papers and closely analogous enumerators do not imply the complete Heawood polynomial or the nine optimal orbits for named labels. The exact catalogue match was the frozen record itself; priority is assessed only relative to the evidence inspected.

## value

PASS

Heawood is a canonical small incidence graph. The noncontiguous feasible-weight spectrum is information not supplied by the minimum, and the nine kinds of minimum configurations separate solutions otherwise indistinguishable by weight. Together with the point-zero distribution and representatives, this supplies a precise comparison or validation instance for enumeration and symmetry calculations on other incidence graphs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
