# Self-review

## Correctness — PASS

For each \(N\ge3\), a stationary middle-column site with color \(i\) has predator-neighbor count \(a_{i+1}+b_{i+1}+c_{i+1}\) in its three-column window. The ten three-color column-count types and their multinomial weights produce the exact 100-state transfer trace, with no reliance on spatial-row ordering. The characteristic-polynomial identity is an exact integer equality and is reproduced from the final `verify_strip.py`; the two recurrent components give a primitive 72-state component and a weight-six singleton. Rational Sturm signs and root isolation certify the leading eigenvalue. Independent full ordered-state enumerations for the genuine 3-by-3 and 3-by-4 tori match the first counts. Limits: no proof of fixation from arbitrary states or of any other strip height.

## Originality — PASS, with residual historical-priority risk

The motivating Muñoz–Nuño 2026 full text defines the cyclic threshold rule and samples temporal attractor basins on larger square and rectangular tori, not a full 3-by-N fixed-state generating function. Jen (1988) and Banks–Djirar (1992) established the general transfer/graph enumeration approach; that approach is explicitly acknowledged. Their general statements do not present the exact factorization and growth constant for this rule. Comparison against available nearby research records includes the prior 4-by-4 fixation census and the distinct complete-graph model; neither logically implies the all-width three-row result. A specialized historical enumeration not found in the searches remains possible, and the older literature was not read exhaustively.

## Mathematical value — PASS

At the threshold-four transition, the exact stationary-state entropy of the narrowest genuine eight-neighbor periodic Moore strip is a natural spatial invariant. The answer holds for arbitrarily long strips; it supplies a high-degree rational spatial zeta, an explicit sequence, and a sharp Perron exponent, beyond a routine single finite count. The ten-type compression is specific to the complete three-row vertical neighborhood. It gives an exact baseline for future strip-width comparisons, without claiming an attraction theorem or wider-strip universality.

## Closest literature and limitations

Primary: F. J. Muñoz and J. C. Nuño (2026), arXiv:2610.37990v1. General methodology: E. Jen (1988), *Cylindrical cellular automata*, and S. P. Banks–S. Djirar (1992), *Fixed Points and Shift Cycles in Cellular Automata*. The 1992 report's pertinent binary graph-method pages were inspected as scanned originals; the Jen journal abstract, not its whole article, was available in this check. The exact-polynomial certificate uses SymPy and is reproducible. No priority or independent-review guarantee is asserted.

Self-review: passed. Independent audit: not yet performed.
