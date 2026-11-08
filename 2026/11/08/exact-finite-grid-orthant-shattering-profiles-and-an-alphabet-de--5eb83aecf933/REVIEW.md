# Review of finite-grid anchored orthant shattering

## Correctness

**PASS.** The proof gives a necessary-and-sufficient strict private-coordinate-maximum criterion for every finite support, including the empty trace and singleton boundary. The coefficient formula is an exact inclusion–exclusion count of ordered coordinate tuples, with each successful tuple necessarily having distinct points. The VC-dimension construction and upper bound account for length-one coordinate chains. The asymptotic law follows from a coordinate-level null-or-label coupon process, fixed-order Bonferroni inequalities and a uniform collision bound. No finite experiment is substituted for any of these universal steps. Eleven small grids were exhaustively checked by the supplied independent trace enumerator.

## Originality

**PASS within accessible published comparisons, with priority uncertainty.** Chernikov and Towsner, arXiv:2010.00726, develop higher-arity VC theory and regularity; their definitions and main approximation theorems do not enumerate shattered subsets for principal downsets on finite products of chains. Chalopin, Chepoi and Knauer, arXiv:2405.12660, Sections 4.4–4.5 and 5.3, discuss downset alignments, distributive lattices and VC dimension, but their set systems contain all downsets or associated convex sets. Their general VC dimension statement does not imply the number of supports shattered by the smaller family of individually anchored lower orthants. An earlier investigation of geodesically convex Cartesian boxes has a larger concept class; even its exact profile does not determine the restricted orthant profile. Earlier computation of a shattering polynomial for rectangular path-grid convexity is only two-dimensional and uses strict minima *or* maxima, not the strict-max-only multi-dimensional system here. No equivalent general coefficient formula and alphabet-dependent coupon transition was identified in targeted public records; unknown literature under monotone-conjunction or record-coordinate terminology remains a real priority risk.

## Mathematical value

**PASS.** This is a complete all-parameter classification for a natural discrete geometric range space and gives a precise count of all shattered supports, not just maximum VC dimension. Its exact formula has distinct Boolean and large-alphabet asymptotic regimes connected by one parameter-free coupon limit. This identifies a sharp exponential-versus-near-linear feature-dimension transition in the random shatterability of finite-grid principal downsets. The structural and probability results hold for arbitrary finite coordinate lengths, with no arbitrary numerical cutoff.

## Limitations

This concerns anchored lower orthants, not all boxes or all ideals. The phase transition is in probability for random supports and does not assert stronger uniform finite-size error bounds or imply a new algorithmic learning theorem. Historical priority cannot be proven by search alone; independent mathematical review is still outstanding.

Self-review: passed. Independent audit: not yet performed.
