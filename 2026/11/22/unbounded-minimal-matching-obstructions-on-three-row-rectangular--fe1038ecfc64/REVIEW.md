# Scientific review: unbounded minimal matching obstructions on three-row grids

## Correctness — PASS

For each integer \(n\ge2\), the sixteen explicitly specified edge sets are matchings of size \(n+1\). Fixing the central horizontal dominoes leaves only endpoint middle-row vertices available for vertical tiles. The four choices at each end split into two phases, determined by which outer row has its first/last free column of each parity. Compatible phases tile both outer rows; incompatible phases leave odd outer-row intervals and cannot be completed. Exactly eight of the sixteen configurations have incompatible phases. Each boundary-edge deletion admits a substitute vertical boundary edge of the retained opposite-end phase. After removing any middle-row spine edge, two newly available middle-row sites can instead be covered by opposite outer-row vertical edges, fixing both parity defects. These give completions of every one-edge deletion and hence minimal nonfaces. The width-three family therefore has minimal nonface size at least \(n+1\), arbitrarily large. The attached checker confirms the phase split and every single-edge deletion for twenty-one strip widths, but finite verification is not the infinite proof.

## Originality — PASS, subject to historical-priority risk

The motivating public paper by Chandrakar, Chau, Goyal, Karki and Subhash (arXiv:2611.18058v1, 2026-11-13) treats the *same* perfect-matching extendability complex and a related middle-row spine. It determines homotopy information and mentions three-element minimal nonfaces without stating unbounded minimal nonface cardinality or the eight boundary-phase obstructions. This shared spine is explicitly acknowledged. Chandrakar and Singh (arXiv:2407.05809, 2024-07-08) classify two-edge minimal nonfaces on width-two grids; their classification does not imply the width-three result. Related published records on finite three-row perfect-matching homotopy types and signed domino sums do not cover this infinite-degree minimal-nonface statement. Search failure alone is not an originality proof. A broader existing result on minimal nonextendable matchings or irreducible forbidden domino patterns remains a residual priority risk.

## Value — PASS

Minimal nonfaces are the minimal forbidden partial tilings and the minimal monomial generators of the Stanley–Reisner ideal. The explicit obstruction family shows that fixed-width three-row strips require forbidden patterns of unbounded arity, whereas the established width-two classification requires only size two. This is a qualitative structural jump across an entire infinite family, not a routine finite census or arbitrary parameter slice.

## Scientific limits

Only eight members of a defined sixteen-configuration template are fully classified; the global set of all minimal nonfaces, the maximum degree and Betti numbers are not determined. Completion after removing a domino is shown for each of these eight configurations. Historical priority is provisional pending independent literature review.

Self-review: passed. Independent audit: not yet performed.
