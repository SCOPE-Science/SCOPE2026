# Scientific review of the two-length tandem-duplication joint law

## Correctness — PASS

The theorem fixes a uniform independent alphabet model, two distinct positive duplication lengths and every permissible source length. Equality of two one-step duplicated outputs is proved equivalent to all intervening lagged equalities; this gives an exact count of distinct descendants. The equality-constraint graph has binomial one-color marginals and pairwise-independent distinct edges. Up to source length equal to the sum of the two duplication lengths, its connected components are induced paths and residue-class cycles, and the gcd-based cycle-survival threshold is derived exactly. The full-cycle correction follows by comparing the all-equal probability with the forest baseline. The mixed factorial-moment inequality proves the independence threshold at **all** longer lengths without extrapolating the short-length generating function. The proof specifies its finite and infinite scope and has no numerical-only lemmas. The two executable tests independently corroborate the graph/collision identity and the exact generating coefficients.

## Originality — PASS, qualified

The standard fixed-length tandem-duplication operation, difference transform and one-length coding model are prior work in Jain, Farnoud, Schwartz and Bruck (arXiv:1606.00397), with earlier capacity/expressiveness studies in Jain, Farnoud and Bruck (arXiv:1509.06029) and a different evolution model in Penso-Dolfin and Greenman (arXiv:1402.0104). The later Kovačević–Tan article (arXiv:1808.10328) provides single-length code bounds, not the same-source **joint** law for distinct lengths. The evaluated two-length generating polynomial, sharp gcd independence boundary and coexistence of zero covariance with higher-order dependence are not logical consequences of the published stated results without additional graph analysis. The general forest equality formula is standard and is acknowledged. Relevant full-text sections and accessible abstracts were inspected, and searches for equivalent wording, alias invariants, general multi-length dominance and exact tables found no conclusive prior coverage. Unindexed earlier derivations and a comprehensive yet-unread version of later channel literature remain residual priority risks; an independent historical-priority audit is not represented as completed.

## Value — PASS

The size of a one-error descendant sphere measures source-dependent ambiguity in a tandem-duplication channel. Comparing two possible duplication lengths for the **same** word is natural when mutation length is unknown. The result shows exactly where the two size statistics cease to be independent, despite staying uncorrelated, and gives an explicit finite-length joint law throughout the entire first-dependence regime. The gcd boundary and factorial correction are structural rather than selected numerical examples; they can inform joint redundancy estimates and tests of channel models without claiming such downstream bounds have already been proved.

## Boundaries and verification

The closed joint polynomial is established only for source length at most the sum of the duplication lengths. Its first-order marginals, zero covariance and independence threshold hold for every permissible length. The uniform-i.i.d. source hypothesis is essential. Complete biological validity, code constructions, extensions to noisy duplications and independent priority verification are not claimed. The repeatable checks are `python verify_joint.py` and `python check_graph.py`.

Self-review: passed. Independent audit: not yet performed.
