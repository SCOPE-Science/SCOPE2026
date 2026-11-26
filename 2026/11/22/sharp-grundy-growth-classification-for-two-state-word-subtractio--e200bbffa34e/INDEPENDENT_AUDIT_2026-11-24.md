# Independent mathematical audit

## correctness

PASS

The four maps exhaust all complete two-state tables with the stated acceptance convention. An O-letter repeated n times allows all shorter prefixes, giving mex n, the upper bound from at most n options. With no O or T the accepting state is never reached. With swaps but no resets an accepted suffix toggles parity; odd positions have the empty option and even positions have no zero-valued option, proving the pointwise parity rule. In the remaining case, if the last block has even parity, accepted suffixes lie within that block and leave positive-valued prefixes by induction. If it has odd parity, cuts before the last reset are all allowed; the first T in each earlier T-bearing block realizes the next positive integer, and cuts within the final block leave zero. This yields precisely the mex equal to the number of T-bearing blocks. A value k needs k swaps and k−1 separators, and T(ZT)^(k−1) and ZT(ZT)^(k−1) give equality for both length parities. Renaming letters by transition type preserves all legal cuts and the mex induction, but arbitrary codeword recodings need not.

## originality

PASS

The supported contribution is the complete all-length maximum law and, especially, the pointwise mixed reset/swap formula. Fixed-value regularity, elementary parity and the mex recurrence are antecedents or standard ingredients. The closest sources give general language regularity, or exact laws for different deletion rules; no checked stronger result covers the reset/swap classification.

## value

PASS

This completely resolves the first nontrivial DFA-state class for a natural boundedness question. The growing case without an accepting reset is not explained by the obvious unary accepting-reset strategy: intervening rejecting resets create many distinct mex levels. Both the sharp growth constant and the individual formula are useful beyond deciding which tables are bounded.

The dated certificate retains the supplied scientific assessment, sources and limitations.
