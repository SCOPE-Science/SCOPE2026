# Scientific review

## Correctness — PASS

The central one-swap condition is precisely the pairwise Kendall-distance-at-least-three property because the full adjacent-transposition Cayley graph is the received-message space. Distinct words in one orientation cannot be one or two adjacent swaps apart; the opposite-orientation sign-string argument gives the universal lower bound of one swap per at most three changed adjacent comparisons. The explicitly stated separated-center inequality gadgets provide a topological-order construction attaining that bound for every length, including endpoint cases. For lengths one through seven, exact generated-confusability-graph and independent-set enumerations establish all finite capacities and multiplicities; an independent pairwise Kendall inversion checker confirms every edge. Both optimum codebook witnesses pass exact checks. The finite search supports only the finite segment and is not used as a proof of the general theorem. Risk: normal implementation errors remain possible despite independent checks; reproducibility and exact finite exhaustive paths materially reduce this risk.

## Originality — PASS, with historical-priority qualification

The complete formulations of classical rank-modulation coding results in arXiv:0908.4094, arXiv:1110.2557, arXiv:1310.5515 and arXiv:1408.4963 treat unrestricted permutations; none states or implies the optimal zigzag-source one-swap capacities and precise matching plateau. The public \(S_5\) Kendall code census concerns a 120-word unrestricted ambient space; the public zigzag-fence linear-extension theorem concerns legal swaps within a single fixed poset and not distinct opposite zigzag orientations; the public alternating *parity* codebook result studies Fourier multipliers. Neither covers this theorem. Actual searches also tested adjacent swaps, zigzag/fence/alternating synonyms, minimum cross-orientation distance, Euler numbers, and the exact 42-edge codebook plateau. Additional accessible prior research claims were compared by mathematical implication, not only by matching titles. Residual risk: obscure or unindexed prior formulations could contain equivalent claims and were not exhaustively excluded.

## Mathematical value — PASS

This is a full-length capacity theorem for a classical constrained permutation source, not an arbitrary isolated numerical test. The natural operational question is whether one-swap correction requires expurgating any of the two Euler-zigzag orientation families. The result exhibits a sharp first non-expurgation length of eight, an exact formula and construction for the cross-orientation distance for all lengths, and a noteworthy 42-disjoint-conflict plateau at lengths six and seven yielding trillions of equality cases. These results make meaningful finite design and theoretical boundary benchmarks. Their significance is limited to one adjacent-position swap on this specific source.

## Limitations and closest literature

The theorems concern no more than one adjacent swap and do not address general rank-modulation codes or larger error radii. Closest literature: Barg–Mazumdar (2009); Mazumdar–Barg–Zémor (2011); Buzaglo–Etzion (2013, 2014); the unrestricted distance-three \(S_5\) equality census; and the zigzag-fence exchange theorem. An unindexed equivalent source remains possible.

Self-review: passed. Independent audit: not yet performed.
