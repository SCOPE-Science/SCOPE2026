# Scientific review: Exact GC-balanced length-four DNA deletion-code capacity and classification

## Correctness — PASS

Exactly 96 balanced length-four DNA words form 52 reverse-complement orbits, of which eight are self-fixed. The remaining 44 two-word orbits are individually deletion-correcting. The 344-edge conflict graph has a checkable rational cover by fourteen conflict cliques with each vertex in at least two, proving that seven pairs (fourteen words) is the maximum. The explicit seven-pair witness meets the bound. The complete census of 20 optimum codebooks and the four symmetry classes of sizes 4, 4, 4, 8 was checked by an independently implemented C++ enumeration as well as a Python checker. The proof covers the full finite domain, with no extrapolation from small samples.

## Originality — PASS (priority qualified)

King (2003) studies the GC-balanced Hamming model; D'yachkov et al. (2003) formulate strand-closed deletion-similarity codes; D'yachkov et al. (2005) give an unrestricted four-base deletion construction. Their inspected results do not state the combined exact GC-balanced four-base deletion optimum or its complete 20-code classification. Targeted scholarly and research-record searches also did not find an equivalent statement or stronger implication. A later 2025 multi-constraint single-edit paper was found at abstract level but not inspected in full, leaving a specific historical-priority risk. Failure to locate another claim is not proof of historical novelty.

## Value — PASS

The joint GC-content, strand-closure, and deletion-correction conditions are independently motivated in DNA coding theory. Their interaction is mathematically nontrivial: the sharp 14-word optimum requires a fourteen-clique rational cover of a 44-vertex conflict graph. A full extremizer census is useful for understanding the finite design choices, and is not just a recomputation of a Hamming optimum or an arbitrary substring slice. No experimental applicability is asserted.

## Limitations and provenance

Single exact deletion, length-four, binary GC classification over four labeled nucleotides only. The independent scientific audit and historical-priority check have not been performed. Verification uses the complete standalone data and source in this package, not a solver log or a finite extrapolation.

Self-review: passed. Independent audit: not yet performed.
