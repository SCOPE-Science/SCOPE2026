# Independent mathematical audit

## correctness

PASS

The conditional cost integer recurrence A_{n,j}(t)=binom(n-1,j)*sum_{u+v=t-(n-1)}a_j(u)a_{n-1-j}(v) counts all permutations, with exact common normalization (n-1)!. The complete certificate lists every nonzero CDF gap through n=8; all are nonnegative. At n=9 j=3 vs 4, integer CDF numerator gaps are +5600 at 16 and -224 at 17 out of 40320, so distributions cross even though conditional means differ 2/5. Independent exact recurrence recomputation covered all 16 adjacent comparisons through n=9 and matched the certificate.

## originality

PASS

Classical Quicksort distributional recurrences, asymptotic laws and moment formulas are prior art; the claim is the earliest exact root-rank conditional stochastic-order failure and its complete finite minimality certificate, not recurrence discovery.

## value

PASS

A natural pivot-balancing heuristic might suggest stochastic dominance, which would control all monotone loss functions instead of only the mean. The sharp nine-key counterexample resolves that plausible hypothesis at its first boundary with exact rational witnesses; finite cutoff is intrinsically useful despite no all-n classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
