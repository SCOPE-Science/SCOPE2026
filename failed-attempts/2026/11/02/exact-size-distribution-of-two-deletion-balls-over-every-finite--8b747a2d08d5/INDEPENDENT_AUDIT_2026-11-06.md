# Independent mathematical audit

## correctness

PASS

For all integers q,n>=2, distinct length-(n-2) outputs are indexed by unique earliest greedy embeddings. Let S be the number of adjacent symbol changes, J the count of consecutive pairs of changes, e the sum of endpoint-change indicators, and T the count of pairwise distinct triples. The source derives B=1+binom(S,2)+2(S-J)-e+T. Conditional on the change bits the rainbow events are independent with q-2 vs 1 choices, yielding the binary-change generating polynomial and its equivalent run-composition sum. The orthogonal Bernoulli expansion gives its exact nonbinary variance. I independently compared BOTH assigned formulas with direct descendant sets in 21 exhaustive (q,n) cases and symbolically proved their variance polynomials coincide for all formal p,n. These finite tests corroborate, not replace, the greedy embedding and conditional-choices proof; n=2 yields B=1.

## originality

FAIL

FAIL because the earlier assigned source record 1 gives EXACTLY THE SAME theorem for all finite q,n, not merely analogous methods or one common example. Identify its K=1+S-e-J (zero-runs) and E=J-T (reversing ABA triples); its B=binom(S+1,2)+K-E is algebraically identical to this record’s B=1+binom(S,2)+2(S-J)-e+T. Thus their full histograms, moments, and all-alphabet quantifiers coincide. The other package’s Git commit 05761bcbb01365a0932467e888f0c5798cb6a416 is timestamped 2026-11-02T03:34:52Z; this package was committed at 03:34:54Z in 7baefd51e5dc01305283118346369604a4e7a5d2. Even before broader literature, this is an exact previously recorded same-repository result; no novel remainder is articulated or supported. An originality disclaimer cannot convert a duplicate original claim into a pass.

## value

PASS

The complete distribution of a natural deletion-channel ball-degree statistic is mathematically useful, with all tails and moments for every q and n. The statement is substantively motivated, but that value cannot cure exact prior coverage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
