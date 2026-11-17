# Scientific review

## Correctness — PASS

The complete quantifier \(n\ge4\) and single-graph-edge deletion are explicit. Green [1], Theorems 3.3.2 and 4.1.2, establish free third homology of the intact complex with the stated rank, while a separate filled-cube argument establishes simple connectivity. The deleted-edge link is exactly two simplices joined by \(n-2\) corresponding edges, giving an integral basis of \(n-3\) cycles. Four-coordinate induced cross-polytope boundaries map to that **full integral basis** under the relative-chain quotient, proving surjectivity and the primitive kernel. Van Kampen and the homological Whitehead theorem upgrade the homology calculation to a homotopy splitting, and the primitive degree matrix ensures inclusion compatibility. An independent mod-two enumeration agrees for \(n=4,5,6\). Residual correctness risk is ordinary human proof-review uncertainty, not a known missing lemma.

## Originality — PASS

Green [1] determines the intact half-cube clique complex but does not give the edge-deleted complex or its inclusion map. Bendersky–Elia–Grbić [2] studies hypercube Rips cohomology and cross-polytope cycles, without the parity-restricted, one-edge failure. Adamaszek–Adams [3] concerns the unrestricted binary cube. Vertex deletion of the halved-cube complex is a distinct local surgery with a link and loss rank \(\binom{n-1}{3}\), not an implication of the present edge-deletion formula \(n-3\). Searches for demihypercube, half-cube, scale-two parity restriction, edge puncture and edge faults did not identify an equivalent theorem. Unindexed edge-deletion work and incompletely accessible source text remain possible overlap risks; absence of a search hit is not evidence of absolute uniqueness.

## Value — PASS

A single failed graph bond is the smallest natural perturbation that retains all sampling sites in a flag/Rips complex. The theorem supplies an all-dimension integral homotopy classification, the exact local-to-global rank loss \(n-3\), a primitive inclusion map, and a splitting explained by geometric four-coordinate sphere carriers. Neither correctness, computability, nor a numerically small rank loss is alone used as the value rationale: the structural homotopy response and inclusion profile for this canonical symmetric family are the mathematical contribution.

## Limitations and closest literature

The formulas do not cover several deleted edges or equivariant splitting. The motivating 2026 full-cube literature [2] and earlier full half-cube computation [1] are credited. Verification by exhaustive finite mod-two ranks is supplementary and not an integral proof.

Self-review: passed. Independent audit: not yet performed.
