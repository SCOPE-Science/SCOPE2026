# Review: Twenty-five Frobenius spectra of Zariski chambers on smooth cubic surfaces

## Correctness — PASS

The classical blow-up intersection product produces exactly 27 (-1)-line classes. Two meeting negative curves force a semidefinite 2x2 principal block, and a pairwise-skew set has intersection matrix -I; the support correspondence is bijective. The Frobenius-invariant support B is realized over the ground field by D=-K+2B with nef big positive part -K+B, verified against every irreducible curve. Exact finite reflection closure has 51840 elements and 25 conjugacy classes; all 2764 cliques and all 25 cycle profiles were exhaustively enumerated. An independently constructed orbit-union fixed-point algorithm checked all powers, and Burnside summed to 8*51840. The attached programs replay the computations.

The finite checks are exact and exhaustive; their independently designed orbit-union branch is compared against the cycle profiles for every power of every class representative. The infinite geometric theorem rests on the proved correspondence with all smooth cubic surfaces' universal 27-line intersection configuration. The 25 rows are conditional on the Weyl type and do not claim realization over all finite fields.

## Originality — PASS, with historical qualification

Bauer–Funke–Neumann give only geometric 2764; Rybakov–Trepalin give 25 Picard/Weyl classes but no chamber spectra; the exact same skew-line simplicial complex has a published non-equivariant homotopy theorem, not a complete classwise Frobenius permutation table. Directly compared full relevant original texts and scientific equivalences, plus literal database/source searches. The discrepancy of fixed chambers 1 vs 13 for the same 27-line type 3^9 shows the result is not implied by line-cycle distributions alone. Earlier unindexed identical tables are possible.

Closest full-text comparators: Bauer–Funke–Neumann (2009) on the non-equivariant chamber number; Rybakov–Trepalin (2016) on the 25 Weyl classes and Picard eigenvalues; Sottile–Yahl on 27-line splitting types; and the published same-complex homotopy classification. The related one-nodal cubic work concerns a singular surface's resolution. The four implication/scope comparisons and all source-inspection limitations are recorded in `AUDIT.json`.

## Mathematical value — PASS

The 2764 Zariski chambers are a natural invariant of big linear series on cubic surfaces. The complete 25-type arithmetic classification determines rational stable-base-locus support classes and their extension-field counts, and reveals that identical line splitting does not fix rational chamber counts (1 versus 13 with the same 3^9 line splitting). This is a meaningful natural complete classification, not an arbitrary slice or recomputation of the known total.

## Limits and outstanding risks

No assertion is made that every type occurs for every finite field or that a 27-line cycle partition by itself uniquely specifies the Weyl class. Historical priority is provisional and a separate external mathematical audit has not been performed. The quoted geometric 2764 total and classical Weyl-group framework are credited as previous results. All verification programs and table entries are included in the same package.

Self-review: passed. Independent audit: not yet performed.
