# Independent mathematical audit

## correctness

PASS

The append step partitions descendants into those retaining and omitting the new last symbol; the intersection consists of one-deletion descendants ending in that symbol. Counting those by whether the last run repeats, lengthens, or forms a return gives the increment of binom(R,2)+S-T. At n=2 the count is one. The transfer records a change, start of a long run, and return, using only whether the preceding edge changed. The count q(q-1)^k over each fixed edge pattern proves iid Bernoulli change indicators. At each successive double change, exactly one of q-1 equiprobable choices is a return, even after conditioning on the entire edge pattern and earlier returns. Centering in these independent edge indicators gives the linear coefficient p(m-1) and quadratic coefficients -1/(q-1) for adjacent indices and 1 otherwise. Orthogonality and conditional binomial variance yield the stated polynomial. For the mean, a fixed output of length n-2 is contained with the probability of at least n-2 successes in n Bernoulli(1/q) trials, by greedy matching (continue against dummy symbols after a full match). The linear Bernoulli CLT and lower-order residuals give the fixed-q Gaussian, without relying on finite experiments. Fresh literal deletion-set histograms, the transfer and both exact moments agreed for q=2,3,4,5 through lengths 9,7,6,5 respectively, including the stated q=3,n=5 histogram. Replay: python /tmp/opencode/frozen_review_reproduce.py deletion.

## originality

FAIL

Distinct indexed statements give the exact same ensemble law, the deterministic profile identity, the conditional return distribution, and the exact variance. The two-state expression rewrites the same local profile count. The unstated Gaussian limit follows immediately from the indexed deterministic identity and the ordinary binomial CLT because all non-quadratic profile terms are bounded by O(n). This judgment is about mathematical coverage and routine implications; it does not infer chronology or dependence from indexed dates.

## value

FAIL

The random two-deletion volume is a natural statistic, but the precise histogram and variance are already covered. The remaining transfer notation is an immediate encoding of the same edge-profile model, and the leading normal limit needs only the binomial CLT and the deterministic linear-size error. Neither supplies an independently motivated remaining counting problem, refined limiting scale, or structural consequence outside that existing description.

The dated certificate retains the supplied scientific assessment, sources and limitations.
