# Independent mathematical audit

## correctness

PASS

The displayed edge potential sums to zero, with part sums 1/N and -1/N at the two endpoint parts and zero elsewhere. The multipartite Laplacian therefore sends it to the unit source-sink divergence. Signed edge gradients give the cut column; summing the disjoint cross-endpoint-part and endpoint-to-other-part types, using (N-1)/(N-a) >= 1/(N-b) and its reverse, gives F_N(a)+F_N(b). The cut diagonal is (N-1)/N times [1/(N-a)+1/(N-b)], and the complementary norm changes the column sum by 1-2Q_ee. Both matrices are symmetric. For x=N-a and y=N-b in actual distinct parts, x,y>=2 and x+y>=N+1, so xy-2(N-1)=(x-2)(y-2)+2(x+y-N-1)>=0; this gives the two-largest cut rule. In K_(k,2,1), H_N(2)-H_N(1)=(N-6)/(N(N-2)) and H_N(1)-H_N(k)=F_N(k)-F_N(1)=(k-1)/(3N). Thus the cycle maximizing pair is unique even at k=3, when the two selected component scores tie; the strict cut ranking and the two rational norms also check. Independent rational grounded systems reproduced both column sums and cut diagonals on all 780 columns in 45 graphs, with direct maximizing-edge tests including k=3,4,5,6,8,13, via python3 /workspace/branches/reproduce_45.py 4.

## originality

FAIL

Earlier catalog record --745e7b0c399e explicitly covers both scores for every edge, both operator norms, the largest-part cut rule, and the same strict reversal with the family norm values. It even treats two parts, which the frozen result excludes. The frozen matched-margin statement is immediate from the very same score table, and no distinct mathematical remainder is established. This is demonstrated equivalent coverage, not a conjecture from titles or date alone and not a determination of personal provenance.

## value

FAIL

The original mathematical invariant and contrasting extremizers are worthwhile, but they are already available in the earlier, broader theorem. The only separately foregrounded quantitative comparison is one subtraction from its table and does not yield a new useful classification, witness or invariant. Exact rechecking adds confidence without a distinct finding that can support a repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
