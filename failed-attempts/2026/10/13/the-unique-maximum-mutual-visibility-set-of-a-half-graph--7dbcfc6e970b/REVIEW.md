# Independent mathematical audit

## correctness

PASS

Every same-side pair is at distance two; a cross-side nonedge has distance three and can use the omitted b_n,a_1 in that order. Thus the proposed set is feasible. A complement of size zero or one leaves a selected same-side pair with no omitted common neighbor. For a complement of size two, two omissions on one side are impossible for n>=4 by the same obstruction. For n=3 with B entirely selected, b_1 and b_2 force a_1 omitted and the one selected a_i has i>1, so its length-three path to b_1 cannot avoid an internal selected B-vertex; the reversed case is symmetric. If the omissions are a_p,b_q, the largest selected A index is at least n-1 and must be <=q, so q>1. Then b_1 is selected, and a same-side pair containing b_1 forces p=1. Now a_n remains selected, forcing q=n. For the K_{n,n} comparison every choice of one omission from each side works and no same-side double omission works when n>=3, giving n^2. Independent replay: python3 /workspace/checks/1.py enumerates masks of all geodesic interiors and all complements of size at most two for n=2..14; it finds six size-two maxima for n=2 and just the claimed maximum for each n=3..14. This finite oracle is corroborative only.

## originality

FAIL

A distinct indexed Resultary record, SCOPE-20261013-ac5be6025f34, explicitly states and proves the identical all-n maximum-size and labeled uniqueness theorem, in addition to stronger enumeration. It is not the frozen record itself. Its wording treats the maximum facts as previously established, without identifying the frozen record as their source. Same-day archiving and that wording do not settle priority or provenance. The decision is based on demonstrated equivalent coverage, not on a claim that one record was published before the other.

## value

FAIL

The uniqueness contrast with complete bipartite graphs is structurally informative in isolation, but the actual Finding gives no further invariant or classification beyond the exact labeled theorem already present and proved in the indexed full-polynomial record. Its elementary extremal argument is also present there. No distinct valuable remainder is preserved by narrowing or rewording the Finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
