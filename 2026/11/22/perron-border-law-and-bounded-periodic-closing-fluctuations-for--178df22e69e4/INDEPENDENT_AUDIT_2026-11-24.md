# Independent mathematical audit

## correctness

PASS

The frozen and repaired proofs yield the exact signed rule: a border gives a period p<n whose missing closing edge is already inside the word (w_p=w_0), and a smaller period would force a longer border. With no border one takes the shortest positive directed return to the first symbol after the prescribed n−1 edges, including the case of a single letter. The k-border count is exactly tr(B^(n−k)), as the length-(n−k) prefix is a labeled closed walk with starting position fixed. PF word-count bounds provide a uniform tail for all k including overlapping borders. In the repair I checked the growing-block estimate explicitly: divide each bridge entry by its positive PF rank-one limit, giving a uniform relative error O_B(θ^(n−2s)) for s-block pairs after normalization. Summing against the product boundary probabilities preserves this bound in total variation. The two coherent boundary strings then give the signed limit after truncating at floor(n/3); a geometric tail times a polynomial controls the discarded moments on either law. In the example the endpoint event of terminal symbol one advance ahead has limiting probability 1/3; length one cannot match, all k≥2 match probabilities sum to 1/3, and a length-two constant match of mass 1/12 is disjoint from this endpoint event. Thus the residual union bound proves a positive negative atom, not an independence heuristic. Independent replay python3 /workspace/branches/independent_checks.py 3 compared periodic completions, the exact rule and trace counts for every word of lengths 1..8 in three primitive graphs, including one with no loops. The frozen checker was inspected, not run. The finite tests do not certify the limit.

## originality

PASS

PASS applies to the repaired signed distributional and moment limit with its directed negative atom, not the complete original novelty claim. The November 17 finite-state closure record covers the uniform model in broader irreducible scope, sums the exact shorter-period trace counts and proves bounded mean correction and variance. In that setting the frozen incidence and expected-border constants follow mechanically by PF from the trace count, and so do the normalized mean and variance statements from the earlier bounds. The repair gives those results explicit priority credit and promotes only the signed law, exponential convergence (including to limiting unnormalized corrections), and the directed example. The identified earlier tails and trace counts do not give the joint border-endpoint process needed for this law.

## value

PASS

The signed law distinguishes a genuine excess-period obstruction from the earlier deterministic upper bound or positive-part tail results, and gives limiting unnormalized fluctuations rather than simply bounds. The limiting boundary construction captures how repeated chunks of a cylinder interact with the directed endpoint constraint. The explicit positive negative atom shows that going beyond an unrestricted longest-border model makes a necessary mathematical difference. This value does not depend on reclaiming the trace counts or normalized limits.

The dated certificate retains the supplied scientific assessment, sources and limitations.
