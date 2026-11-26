# Independent mathematical audit

## correctness

PASS

A strict drop takes the image S to S minus the letter's source, and occurs exactly when both endpoints lie in S. Sources cannot recur, and each arrow points to a surviving or later-removed vertex. There are no repeated undirected edges or undirected cycles: an undirected cycle would require that every vertex of that cycle use its sole outgoing arrow on the cycle, giving a directed cycle. Thus the words are rooted spanning forests with descendant-before-ancestor edge orders, and any such order realizes all its drops. In a path component with a edges, pruning either endpoint until one vertex remains yields 2^a internal words; fixing the survivor at position j instead gives binom(a,j-1). For a path, the k=n-m components have ordered nonnegative edge counts of sum m. Shuffling their orders gives the multinomial sum 2^m k^m. For a cycle, marking one omitted edge gives n cuts and counts each forest-word pair k times, yielding the ratio n/k. At m=n-1 the path binomial row and the uniform cycle reset counts follow by choosing the survivor, with each possible path position appearing once per fixed cycle vertex across the omitted edges. The empty word, P1, and C3 are included in these arguments. A separate bounded transformation-based DFS also matched the spectra and per-vertex reset counts through n=6 for both families; no replay artifact from that check was retained. The unrestricted proof does not depend on the finite check.

## originality

PASS

The supported distinct claim is the all-rank multiplicity of literal minimum-length words in the alphabet of both orientations of every edge, including the ratio and reset-image specialization. The inspected statements on reset thresholds, individual element lengths and nearby collapse-schedule counts do not cover it.

## value

PASS

Rank and word length are natural observables for this generating alphabet. The formulas give the exact number of fastest compression sequences at each attained rank and quantify the contribution of closing the path into a cycle. For instance, normalizing by alphabet size to the m-th power gives the probability that m independent uniform letters achieve the largest possible rank loss. Neither reset threshold nor enumeration of monoid elements supplies that statistic.

The dated certificate retains the supplied scientific assessment, sources and limitations.
