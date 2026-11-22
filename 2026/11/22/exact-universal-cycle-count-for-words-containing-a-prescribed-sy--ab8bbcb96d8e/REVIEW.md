# Scientific review: exact universal-cycle count for a required symbol

## Correctness — PASS

The claim fixes a labeled alphabet, one required letter, circular contiguous factors, and rotation-only equivalence. Every edge of the restricted overlap digraph is a unique permitted window. The graph is balanced and strongly connected; the proof gives explicit paths through the all-zero vertex. The key matrix identity is proved over a rational-function field by subtracting the zero-free subalphabet Laplacian from the full de Bruijn Laplacian. The restricted resolvent differs from the smaller full-shift resolvent only by an all-ones matrix; the zero-free Laplacian annihilates this term. The resulting exact determinant and directed matrix-tree coefficient give the in-arborescence count. The fixed-edge BEST theorem yields exactly the number of rotation classes. Exact small-case determinants and direct Euler-tour counts were reproduced from `verify.py`; finite tests are not used to justify the infinite parameter range.

## Originality — PASS, qualified

Leitner and Godbole (arXiv:0808.1309, password theorem) and Blanca and Godbole (arXiv:1008.2251, Theorem 11) already prove existence of universal cycles for the required-letter language; that existence is explicitly excluded from novelty. Sawada and Gabrić (arXiv:2510.16545) explain uniform arborescence-based sampling for other constrained de Bruijn families. A search of relevant mathematical research records returned related enumerations of bounded-weight, locally square-free, and exact-symbol-multiplicity universal cycles, but not the all-parameter count for all words containing a specified letter. Those restricted factor sets do not contain this full permitted factor family as a counting corollary. The evaluated contribution is the closed arborescence count and full characteristic factorization, not a generic application of BEST. An unindexed prior formula or a general spectral theorem not retrieved could still cover it.

## Mathematical value — PASS

The exact number of compact cyclic indexes for the complete one-required-letter language was not given by the existence results. The family arises directly in restricted universal-cycle/password problems and has exponentially many admissible windows. The formula counts every labeled rotation class for all alphabet sizes and orders, replacing an exponentially large determinant with a closed product. The three-point Laplacian spectrum is a structural conclusion with independent use for tree and tour enumeration; the binary agreement with the ordinary de Bruijn count is a meaningful boundary check, not the basis of the value argument.

## Sources and residual limitations

Primary full texts examined: Leitner and Godbole, *Universal Cycles of Restricted Classes of Words* (arXiv:0808.1309); Blanca and Godbole, *On Universal Cycles for New Classes of Combinatorial Structures* (arXiv:1008.2251); Sawada and Gabrić, *Random Generation of Universal Cycles and de Bruijn Sequences* (arXiv:2510.16545). Other related works were compared from their available abstracts or indexed summaries only. The result has not been independently audited, and it does not enumerate simultaneous requirements involving multiple letters, quotient by letter permutations, or reversal classes.

Self-review: passed. Independent audit: not yet performed.
