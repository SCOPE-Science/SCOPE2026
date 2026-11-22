# Review: sharp adjacency-trace spectra of finite cographs

## Correctness — PASS

For a cograph and a nonempty parameter set of size \(m\), the augmented family of open-neighborhood traces adjoins the empty set and full parameter set. The cotree induction gives at most \(2m\) augmented traces: a disjoint-union split contributes two subfamilies intersecting only at empty, plus the full parameter set; a join split gives two translated subfamilies intersecting only at full, plus empty. When just one child has parameters the other contributes only an augmented extreme. Both are valid exact bounds for all finite cographs. An explicit nested-prefix threshold graph on \(2m\) vertices meets the bound. Distinctness of all clique-vertex and prefix traces and absence of an induced four-vertex path are checked directly. Clique-and-isolates and subsets of threshold witnesses realize every integer from one through \(2m\). Complement duality proves the closed-neighborhood claim. A shattered three-set would need eight traces, contradicting the six-trace upper bound; a two-set is shattered by the construction.

The standalone verifier enumerates all \(6039\) labeled cographs of orders at most six and \(362227\) nonempty marked parameter sets, confirms constructions through \(m=14\), and confirms all spectrum values through \(m=11\). The checker is corroboration, not an infinite proof.

## Originality — PASS within inspected evidence

The closest explicit general bound is Bonnet–Foucaud–Lehtilä–Parreau, arXiv:2301.04217, whose theorem \((d+2)2^{d+1}m\) gives \(4m\) at twin-width zero rather than the exact \(2m\). The 2025 merge-width theorem gives general linear neighborhood complexity without a cograph-specific coefficient. The 2026 monadic-dependence model-checking theorem establishes broad polynomial type counts and its companion gives almost-linear neighborhood complexity, neither implying this complete exact integer spectrum. Searches for exact P4-free/cograph trace counts, cotree profiles and zero-twin-width constants found no logically dominating primary statement. Related published graph-class and threshold-graph findings concern deletion, logical equivalence, or adaptive shattering rather than the exact trace spectrum. Unavailable older specialized results and imperfect indexing remain genuine priority risks; absence of an indexed match does not establish historical uniqueness.

## Value — PASS

Exact neighborhood complexity is a standard finite-model and graph-structure invariant used to measure possible one-variable adjacency patterns over parameters. The result replaces a generic \(4m\) estimate with the sharp \(2m\) coefficient at twin-width zero, proves the complete integer spectrum rather than only extremal growth, establishes minimum witness order, and transfers it to closed neighborhoods by a genuine complement equivalence. These are natural all-size structural statements, not arbitrary fixed-size computations. The elementary cotree argument is an advantage for reproducibility; significance is confined to adjacency trace complexity rather than broad first-order type counting.

## Limitations and priority risk

Existing theorems could conceivably imply the coefficient via a specialized corollary not explicitly indexed, or an older cotree result could state the same theorem under a different vocabulary. The work does not prove a stronger bound for all graphs of positive twin-width, nor anything for quantified formulas. Its historical novelty is provisional. No outside scientific assessment is claimed.

Self-review: passed. Independent audit: not yet performed.
