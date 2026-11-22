# Review: sparse-branching triangular Jacobi power norms

## Correctness

**PASS (self-review).** The residual identity is exact by finite telescoping. The critical reduction from arbitrary signs and multiple row entries to a deterministic parent forest follows from entrywise absolute-value domination and row-by-row convex maximization: acyclic path expansions are affine in any one row. At each replacement, the existing column sparsity support is preserved. The parent-forest power has disjoint-column support and singular norm equal to the square root of its largest exact-depth descendant count. A level-capacity count proves necessity of the ceiling budget; a levelwise grouped tree constructs equality. The strict \(>1\) criterion uses \(m_*=\lfloor\tau^{-2k}\rfloor+1\) and includes equality boundaries correctly. The supplied pure-Python checker replays small exhaustive forests and the exact rational witness. Finite tests are not the infinite proof.

## Originality

**PASS, with residual search risk.** Dargaville–Pain, arXiv:2611.00552v1, Sections 4 and 6.2, establishes the Neumann iteration identity, identifies nonnormal finite-sweep norm growth, and defines a row-dominance criterion; its inspected main text, conclusion and relevant appended material do not state the sharp degree-limited Euclidean power norm or the minimum vertex budget. The classical infinity-norm contraction of Jacobi does not imply the sharp Euclidean formula. Searches of mathematical literature and published mathematical result records for the aliases *triangular Neumann power*, *row-substochastic sparse powers*, *parent-tree shift* and *bounded branching* found non-identical tree-shift/Cesàro-space and GMRES results, rather than a dominating theorem. Related inverse-norm identities concern a different expression and do not imply the sharp \(\|G^k\|_2\) with a column degree cap. A pre-existing unindexed equivalent extremal matrix-power formula remains possible; index searches alone do not establish novelty.

## Value

**PASS.** ILU triangular solve applications often employ only a few parallel Jacobi sweeps, and strict row dominance by itself guarantees infinity-norm decay but may conceal Euclidean residual amplification. The exact finite \(n,d,k,\tau\) formula identifies the graph-theoretic branching quantity missing from a row-only diagnostic. It gives the sharp worst-case safety condition and the smallest matrix size at which failure can occur, not merely a numerical example. The column bound is structural, checkable, and essential to the threshold; it is not claimed for arbitrary ILU structures.

## Closest sources and limitations

The primary source is Dargaville and Pain, *A comparison of parallel iterative methods for ILU triangular solves*, arXiv:2611.00552v1, https://arxiv.org/abs/2611.00552 (2026-10-31), particularly Section 4 and Section 6.2. The closest indexed tree-shift results use non-Euclidean Cesàro spaces or infinite-dimensional shifts, and the closest Krylov results concern different residual minimizers. No conclusion is drawn about outer-solver convergence, typical ILU matrix patterns, or finite-precision effects. Independent literature indexing is incomplete.

Self-review: passed. Independent audit: not yet performed.
