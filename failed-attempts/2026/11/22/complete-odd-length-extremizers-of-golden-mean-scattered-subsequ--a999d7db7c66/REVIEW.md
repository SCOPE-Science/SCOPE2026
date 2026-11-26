# Independent mathematical audit

## correctness

PASS

The all-zero and alternating targets force at least 2m+1 zeros and m+1 ones. At the resulting length bound, a one at zero-rank c supplies exactly the eligible marker indices in {c−1,c}. Covering 2m+1 positions with m+1 such intervals leaves at most one excess membership, so repeated ranks are impossible, including at clipped endpoints. The first and last ranks are in {0,1} and {2m,2m+1}; jumps are one or two. For m≥1 this permits exactly two all-two sequences and m sequences with one jump of size one, giving the displayed distinct words and automatic avoidance of 11. The two m=0 words are immediate. To show attainability and sufficiency, pair up target positions consecutively on either side of the odd-index singleton assigned to 10 or 01. Each pair lies in {00,01,10}, all contained in 010; either singleton fits in the remaining block. Independently, enumerating explicit subsequence sets for target lengths 1,3,5,7 checked the optimal-content hosts and all shorter hosts of feasible length (python /workspace/reproductions/golden.py). The proof has no cutoff.

## originality

FAIL

The list and count, not just the minimum length, are a direct implication of the earlier exact fixed-marker classification, Resultary record 522f2396053e. At k=2m+1 and r=m+1, extremal full coverage forces exactly the length that minimizes cover length for the one-marker family at fixed r. The earlier theorem determines every such host by a one-unit slack vector, hence gives the exact same list, count and rigidity. The only remaining check is that each of these already determined words contains every golden-mean target, which follows by the direct two-letter/singleton block test. This is verified prior implication, not a finding that the earlier source literally states the golden-mean theorem verbatim, nor a failure based on the inaccessible unpublished length reference.

## value

FAIL

The equality-case question is natural, but the fixed-marker result already yields all candidate optima, the count and rigidity by the one-unit slack specialization. Beyond that known structure the frozen finding adds only the immediate embedding of admissible two-letter blocks and a singleton. It does not establish a substantive new classification, boundary, or extension requiring an independent exact fact; no separate valuable repair is identified.

The dated certificate retains the supplied scientific assessment, sources and limitations.
