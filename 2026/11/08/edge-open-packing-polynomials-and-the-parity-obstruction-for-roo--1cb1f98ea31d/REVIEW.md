# Scientific review: edge-open-packing polynomials of rook graphs

## Correctness — PASS

The statement concerns all labelled edge-open packings of \(K_m\square K_n\) for \(m,n\ge2\), including the empty packing. The proof first establishes a reversible decomposition into single horizontal edges, single vertical edges and perpendicular two-edge induced paths, whose supports are mutually disjoint in both row and column coordinates. The proof explicitly excludes parallel incident edges by their completing triangle and chains of three selected edges by a forbidden selected middle edge. Labelled allocation of supports with the four pivot choices for each perpendicular path gives the factorial count. The bivariate exponential formula then follows using unused row and column atoms. The support identities \(a=t+v\) and \(b=t+h\) prove the bound and its unique odd-square obstruction, with explicit constructions for sharpness. The extremal multiplicities follow from equality cases in those inequalities.

A separate literal enumerator checks conflicts by searching for a third ambient edge between endpoints, rather than relying on the classification. It verified all size coefficients for 15 unordered pairs \(2\le m\le n\le6\), counting 852443 compatible subsets in aggregate. Exact arithmetic verified extremal counts on a further 261 profiles. Computational checks are finite corroboration, not a proof of all cases. The unrestricted proof is combinatorial and does not depend on these calculations.

## Originality — PASS (provisional publication priority)

Chelladurai, Kalimuthu and Soundararajan (2022) introduced the parameter and computed values on standard families including complete multipartite graphs, but the latter are not the rook-graph Cartesian products at issue. Brešar and Samadi (arXiv:2403.00750, 2024) gave complexity results and bounds. Brešar, Dravec, Hedžet and Samadi (arXiv:2406.04020, 2024) gave product inequalities; their Cartesian-product Section 5 does not specialize to an exact all-size polynomial on \(K_m\square K_n\). The exact new statement is stronger than those scalar bounds, and neither follows from their general induced-star observation without the new support-block characterization and allocation count.

Targeted research-record searches, open-literature searches under edge-open packing, induced star forest, rook graphs, line graphs of complete bipartite graphs, and injective edge-color-class terminology, plus accessible historical claim summaries, found no equivalent closed polynomial or parity-resolved extremal multiplicity. An unindexed equivalent result, or one expressed through a conflict graph and its independence polynomial, remains a residual risk. Priyamvada–Panda (2024, DOI 10.1142/S1793830923500416) treat injective edge-coloring bounds of graph products. Only the accessible abstract was obtained; its full text remains an explicit overlap uncertainty, although a chromatic-index bound alone does not determine our all-class polynomial. Search failure by itself does not certify priority.

## Mathematical value — PASS

The result answers a natural, complete enumerative question for an infinite Cartesian-product family connected to edge-open packing and injective edge coloring. It gives a structural bijection and a two-sort labelled exponential formula for every coefficient, not merely an isolated extremal cardinality. The sharp parity drop at odd square dimensions and exact optimizer multiplicities exhibit a meaningful boundary phenomenon missed by general product lower bounds. The formulas are self-contained and permit coefficient extraction and exact finite computations; neither a broader theorem nor an application is required for this natural classification to be useful.

## Limitations and closest literature

The source's induced-star-forest description is acknowledged as known; only the rook-specific decomposition, all-size enumeration, parity classification and multiplicities are assessed. This is not an injective edge-coloring enumeration, and it does not cover general Hamming graphs of higher Cartesian dimension. Priority and proof have not been independently audited. Relevant primary sources are Chelladurai et al. (2022), DOI 10.1051/ro/2022171; Brešar–Samadi (2024), arXiv:2403.00750; and Brešar–Dravec–Hedžet–Samadi (2024), arXiv:2406.04020.

Self-review: passed. Independent audit: not yet performed.
