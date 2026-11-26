# Independent mathematical audit

## correctness

PASS

Deleting no-op swaps leaves single active edges, unordered disjoint active pairs, and overlapping active swaps on a triple. Their changed supports are, respectively, two neighbors, four positions (uniquely paired into disjoint adjacent edges), and either all three positions of a triple or its separated endpoints. A repeated-endpoint or constant triple adds no new word, a triple with exactly one equal adjacent pair adds one, and an all-distinct triple adds two distinct rotations. Thus the count is 1+b+binom(b,2)-t+2d+e, evaluable in one scan. The triple correction is at most 1 per triple after subtracting t; maximizing also needs b=n-1. Its equality conditions are precisely all-distinct triples for n>=3 or an unequal pair for n=2, giving q(q-1)(q-2)^(n-2) centers. Uniform boundary indicators have mean p and pairwise joint mean p^2, including neighboring sites by conditioning on their shared letter. The local means of t,d,e per triple are p^2, p(q-2)/q, and 2p/q, so E[-t+2d+e]=(n-2)p^2. The resulting mean is the stated one. Swaps are reversible, so the simple graph has degree |B_2(w)|-1; summing degrees and dividing by two proves the edge total. This counts labelled words, not edit histories or swaps across different compositions.

## originality

FAIL

Verified full coverage of the substantive claim by distinct records: assigned record 5 has the identical pointwise formula, nonbinary extremal result and mean, and an indexed result gives the same count in another basis plus a full distribution. The graph edge count is immediate from the common mean. This is a finding of equivalent coverage, not an assertion that record 5 or the later-dated catalogue record has historical priority over record 4.

## value

FAIL

Center-specific ball sizes are useful for coding and graph calculations, but the formula, extremizers and average are already covered by distinct findings, and the extra edge count is only the degree-sum identity. There is no independently useful unknown exact remainder in the delivered statement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
