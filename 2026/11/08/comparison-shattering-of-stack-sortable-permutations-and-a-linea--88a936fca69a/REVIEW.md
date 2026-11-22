# Scientific review: positional comparison-support classification on 231-avoiders

## Correctness: PASS

The forbidden triple \(i<j<k\) with \(\pi(j)>\pi(i)>\pi(k)\) rules out two queries sharing left index in a shattered support. The right-to-left minimum/maximum insertion independently realizes every label pattern on every permitted support; every inserted first entry is extremal and cannot start a 231 pattern. This proves the complete matroid independence polynomial for every integer \(n\ge1\), including the empty-domain case. Independent finite checks at lengths 2–6 gave the full Stirling coefficients. The auxiliary length-seven online tree was also independently checked but is not needed for the final theorem.

## Originality: PASS, best-of-knowledge for the narrowed claim

The 2 November 2026 Wilf-equivalent length-three avoidance theorem already supplies the all-length VC *dimension* and the exact online dimensions for all six length-three forbidden patterns through \(n=8\), in the inverse/label query formulation; that online content is excluded. The 25 October 2026 321-avoider theorem already proves a linear adaptive gap for a different pattern. Neither published theorem provides the complete support-by-support characterization or its Stirling coefficient spectrum for the positional 231-avoider class. The 2021/2023 Johnson–Wickes permutation-shattering paper studies all induced orders of a selected set, not arbitrary bit assignments to selected pair queries. A 2021 zero-set theory concerns a different hypothesis family. Searches for inversions, stack-sortable, Catalan, matroid and pairwise shattering found no stronger precise result; alternate terminology remains a residual priority risk, not evidence of nonexistence.

## Mathematical value: PASS, focused

A full exact shattering complex of a natural Catalan class is a meaningful stronger invariant than its VC dimension: it specifies every feasible/nonfeasible fixed comparison support, identifies all matroid circuits and facets, and gives the complete rank spectrum in closed form, including \((n-1)!\) facets and \(n!\) supports. These are directly useful to enumeration and design of nonadaptive comparison tests, not merely a small numerical gain. The argument is short and elementary, which does not negate the natural classification's content.

## Limits

This is a narrowed result. The formerly asserted novel depth-eight seed and linearly amplified adaptive gap are already established by, or immediate from, prior work. The exact all-order Littlestone dimension is not claimed. Retained online certificates remain auxiliary; no separate priority is claimed for them. Historical uniqueness is not exhaustively certified.
