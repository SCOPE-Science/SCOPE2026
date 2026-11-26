# Independent mathematical audit

## correctness

PASS

These are distinct ordered, overlapping adjacent-pair histograms of linear words, with the unchanged word included. Each interior swap changes only the three local pairs on its four-symbol context. Independent integer histogram differences in alphabets of sizes 2,3,4 give one zero and 2,14,24 nonzero differences per specified support of sizes 2,3,4, respectively. A context uses at most four symbols; even a symbol canceled from the difference can be relabeled alongside the support into a fixed four-symbol set. Thus the finite classification lifts to every q, with q=2,3 checked separately. Row sums count all letters but the final one, and column sums all but the initial one. Interior swaps preserve both marginals, while unequal first and last swaps each change just one, and different ones, for n>=4. This proves the exact additive boundary formula, with n<=3 handled directly. In a repeated de Bruijn cycle of order four, any window of n>=q^4+3 covers the full context set. Exactly q^3 rotations fail each boundary inequality, so fewer than q^4 fail either when q>=3. For binary words a direct recomputation of actual swapped-word profiles gives maxima 1,1,2,3,4,4,4,4,5 at n=0 through 8. The family 01011 followed by t zeros and 01 has both required unequal boundary pairs and opposing nonzero interior changes from 0101 and 1100 for every t>=1. Finally the chance of a missing four-letter context is bounded by q^4 times an exponentially decaying disjoint-block omission probability at fixed q. Outside that event the offset is exactly the sum of the two independent endpoint inequality indicators. The unconditional distribution therefore converges to the claimed binomial law; no independence from the context-coverage event is assumed.

## originality

PASS

Profile histograms, word-level adjacent transpositions, local edit differences and de Bruijn cycles are established tools. The inspected matches do not give this at-most-one-swap histogram-image maximum, the sharp binary onset or the limiting boundary offset. The most relevant same-day comparison gives an exact answer for substitution, not swap. This is a bounded, best-of-knowledge assessment.

## value

PASS

For fixed-length reads that report only a directed pair histogram, the image of a single adjacent-swap ball measures actual ambiguity in the observation space rather than ambiguity of the underlying word. A sharp all-alphabet ceiling, explicit saturation, and the exact binary onset are useful benchmarks for that natural local-error statistic. The independent endpoint effects further explain why random long words fall short of the maximum with nonzero limiting probability even though they almost surely realize every interior change.

The dated certificate retains the supplied scientific assessment, sources and limitations.
