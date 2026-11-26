# Independent mathematical audit

## correctness

PASS

A finite avoiding word either has no 11 or has a terminal run of at least two ones after a prefix without 11 ending in zero (or empty). This gives F_{k+2}+F_{k+1}-1. In the required-edge subgraph, outdegree minus indegree is 1_{begins 10}-1_{ends 11}; the positives are precisely the length-(k-1) states beginning 10 and containing no 11, so there are F_{k-1} positives and as many negatives ending 11. Extra edges of any covering closed walk decompose into directed paths from negatives to positives and cycles. A path shorter than k-2 preserves a suffix-prefix overlap of length at least two and hence carries the negative source's terminal 11 into the positive target, impossible because the target contains no 11 anywhere. This uses the stronger no-11 property from Step 2, rather than merely the first two symbols as suggested by the compressed wording in Step 3. Appending the last k-2 symbols of the target gives a path of exactly that length because both endpoints share the one-symbol overlap 1. Matching all deficits and surpluses balances the graph; required edges already weakly connect their vertices by prepending zeros, and inserted paths attach to this support. Euler traversal yields the upper bound. Reversal/complement and the Fibonacci ratio give the other assertions. The independently written `python /tmp/opencode/frozen_review_checks_3_4.py cover` solved the full minimum-cost circulation, with integer connected solutions and matching lengths 8,16,29,53,94,166,290,504,871 for k=3..11; the finite check does not prove the all-k result. The archived verifier was inspected, not executed.

## originality

FAIL

The exact all-k optimum for a single forbidden triple with unrestricted cyclic hosts is fully covered by a distinct indexed record, e87a9a41d879, under bit complementation (already an explicit symmetry of the frozen claim). No distinct scientific remainder is established. This is a finding of exact equivalent catalogue coverage, not a conclusion about who obtained the theorem first. The earlier and later archive path dates and the unsuccessful primary search do not settle historical priority.

## value

FAIL

The minimum unrestricted cover and its repetition overhead are natural objects, and the proof is correct. But this narrow exact invariant is entirely recovered by the already indexed complement-equivalent theorem, including the construction and its numerical dependence at the claim level. The record supplies no additional invariant, bound, or independently needed distinction that survives this overlap.

The dated certificate retains the supplied scientific assessment, sources and limitations.
