# Scientific review: short-deletion necklaces of permutation powers

## Correctness — PASS

The complete proof reconstructs deleted gaps from the output's labeled adjacent-symbol congruences. The total deletion budget makes these congruences unambiguous below \(q\); at \(q\), one size-\(q\) gap is the only possible wrap, with \(q\) mask orbits producing the unique collapsed output \([P^{k-1}]\). The mask-orbit count is independently derived by Burnside using the cycle decomposition of whole-period rotations. The scope excludes \(k=1\) and \(t>q\); these are not silently inferred. The standalone exhaustive check passed \(75\) configurations covering \(255038\) deletion masks. A finite check does not certify all parameters, so the paper proof carries the infinite statement.

## Originality — PASS, with residual risks

The closest published prior work is Adamson et al. (arXiv:2108.01990) on general and fixed-content necklaces; its full-text introductory results and counting sections do not model deleting prescribed positions from a single repeated permutation template. Atashpendar et al. (arXiv:1802.00703) count linear deletion embeddings and supersequence behavior, and Luchinin et al. (arXiv:2412.03289) prove binary cyclic-source reconstruction bounds. None of those inspected claims implies the unique first-wrap fiber or the exact source-constrained output count. Bianconi–Brugnoli's work on transition-restricted necklaces (DOI 10.1017/S0004972721000307) was accessible in abstract only; it is a specifically named residual bibliographic risk, not a source of fabricated noncoverage. Published-record searches returned related but logically different necklace-orbit and linear deletion results. No independent literature priority certification is asserted.

## Mathematical value — PASS

This is a complete sharp first-collision classification for all alphabet sizes and repetition counts in a natural cyclic deletion channel. The exact exceptional output and its fiber size are structural information unavailable from a generic Burnside count; the formula counts genuinely distinct rotation classes rather than merely deletion masks. The threshold \(t=q\) is intrinsically motivated by the period length and gives a natural boundary of the unique-reconstruction regime.

## Limitations

The theorem is restricted to circular powers of labeled permutations and deletion budgets through one full period. Distinct-source period powers with repeated symbols, larger deletions, and dihedral/reversal quotienting are not covered. The finite checks are not a proof of arbitrary-parameter claims. Related published literature may contain an equivalent result not located by the searches.

Self-review: passed. Independent audit: not yet performed.
