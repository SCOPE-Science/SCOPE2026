# Mathematical review

## Correctness — PASS
The argument uses the original adjacency-based definitions: in a proper \((n+1)\)-colouring of \(K_{2,n}\), each row omits exactly one palette colour; each row therefore contains at most one rich edge. Since every rich edge must have a distinct rich neighbour, exactly two rich edges must occur in one common column. Their colours are each other's row omissions, and all remaining colours form a derangement between the rows. This is a bijection with the counted data. The orbit count follows from conjugacy of the derangement (and inversion under swapping the two small-side vertices). The proper-colouring denominator uses inclusion-exclusion or the direct split of permutations into derangements of \(n\) and \(n+1\). The proof covers every integer \(n\ge3\). An independent direct enumerator corroborates the formulas through \(n=8\). Finite enumeration is not used in the infinite proof.

## Originality — PASS, with residual historical priority risk
Jiangxu Kong, *Linear bounds for rich-neighbor edge-colorings* (arXiv:2610.21036v1, 2026-10-15), proves the optimal index for every complete bipartite graph. Its Section 3.1 supplies an existence construction, but not a classification or count of *all* optimum edge-colourings, an orbit count by derangement cycle types, or their rarity among proper colourings. Kashima, Petruševski, Sedlar, and Škrekovski (arXiv:2610.16446v1) establish general bounds and rich-edge constraints. The founding paper and subcubic literature are relevant but not known to contain an unrestricted \(K_{2,n}\) optimum-enumeration theorem. The original 2024 full text was not accessible; priority remains provisional and independently unconfirmed. A same-parameter search of accessible mathematical records did not identify an equivalent statement; absence from a search is not novelty proof.

## Mathematical value — PASS
The previously established *minimum number of colours* does not determine the multiplicity or structure of optimal solutions. The exact bijection with derangements gives every optimum assignment for an infinite natural graph family, not just a handful of examples. The complete orbit classification yields the partition function \(p_{\ge2}(n-1)\) of optimal types and the fraction \(P_n\sim1/n\) measures their scarcity among proper minimum-palette assignments. These quantities are natural refinements for extremal edge-colouring rather than arbitrary finite slices.

## Limitations and nearby work
The key prior theorem determines the index and a construction; neither is claimed as new. This work applies to labelled \(K_{2,n}\) with \(n\ge3\), counting named minimum-palette colourings and then quotienting by automorphisms plus palette permutations. It does not classify \(K_{m,n}\) for \(m\ge3\), does not handle larger palettes, and has not undergone independent mathematical review.

Self-review: passed. Independent audit: not yet performed.
