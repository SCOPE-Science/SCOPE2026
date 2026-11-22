# Review of the constrained swap-and-replace sphere spectrum

## Correctness

PASS. The count of legal replacements and swaps is disjoint and exact: each occurrence of `101` supplies exactly the one overcounted neighboring zero and the two forbidden swap positions, yielding a net loss of one from length. The gap-decomposition binomial sum handles all values of the one count and the number of short internal gaps, with the all-zero exception explicit. Its sum gives the rational enumerator, and endpoint witnesses cover the full degree support. The stated mean and variance follow by a simple analytic dominant-root perturbation. Direct word enumeration through length 20 and independent transfer enumerations through length 100 agree with all formulas. Risks: these conclusions do not apply to cyclic words, unconstrained target outputs, or multiple edits.

## Originality

PASS, with historical-priority qualification. The 2023 foundational tilde-Fibonacci-cube paper proves a total edge count; the open 2025 overview proves other graph invariants but does not give a full degree spectrum. The classical 2011 Fibonacci-cube degree distribution applies to replacement-only edges; at length three it differs from the tilde distribution. Other constrained-word edit distributions treat different restrictions or edit operations and do not imply the present result. Searches for direct aliases and exact database/tabular presentations found no matching theorem. An unindexed or differently named predecessor could remain, and negative searches alone do not prove absolute historical novelty.

## Value

PASS. Under a locally constrained substitution/transposition channel, the exact source-dependent size of each radius-one error neighborhood is a natural invariant for assessing nonuniform error exposure and sphere-packing analyses. The local cancellation identity, exact histogram, unbroken range, sharp fragile/robust configurations and linear-order variance characterize the entire language for every length, not just isolated numerical instances. No code-size improvement is claimed.

## Closest literature and limits

Anselmo et al. (arXiv:2303.09898, 2023), section on tilde-Fibonacci cubes: vertices, recursive construction and summed edges; Anselmo et al. (OASIcs Grossi 5, 2025), section 6: edge counts and metric data; Klavžar–Mollard–Petkovšek (2011): ordinary Fibonacci-cube degree sequences; Gabrys et al. (2022): different synchronization-error coding regimes. Their results motivate but do not imply the conditional per-input spectrum given here. The primary residual risk is an unlocated equivalent study of constrained swap-and-replace ball sizes.

Self-review: passed. Independent audit: not yet performed.
