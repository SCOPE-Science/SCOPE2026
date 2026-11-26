# Independent mathematical audit

## correctness

PASS

With a grounded hub the two-follower petal has inverse trace 4/3 and the one-follower petal 1/2; exchanging one full and one untouched petal for two singly selected petals decreases the trace by 1/3. With a free hub, eliminating the outer blocks gives hub Schur complement (3/2)t_1+2t_2, where t_j counts petals with j selected outer vertices. The inverse trace adds (1+2t_0+t_1/4) divided by that complement to the outer trace. At fixed k with a free hub its derivative in t_1 is -1/6-(m+1/2+k/4)/(k+t_1/2)^2<0. Thus each conditioning has a unique minimizing count profile. Subtracting their costs gives 2(2m+1-3k)/(3k) for k≤m and (2-k)/(2m+k)<0 for k≥m+1. This verifies the tie (m≡1 mod 3), strict regimes, counts, agreement of formulas at k=m, and the F_5 nonnesting example at budgets 3 and 4. The top endpoint k=2m leaves the hub alone and gives 1/(2m), as required. The exact-arithmetic checker verify_friendship.py was inspected, not executed; its finite scope is distinct from this proof.

## originality

FAIL

The earlier indexed all-budget clique-windmill theorem covers the same objective, both hub cases, balanced optimal placements and counts on a larger graph family. Two vertices per blade specialize its statement to the frozen claim; the threshold and nonnesting witness require only simplifying those formulas, not a new optimization theorem. This conclusion does not rely on the inaccessible Sun–Li–Liu paper.

## value

FAIL

All-budget optimal placement and hub abandonment are meaningful questions, but for these graphs the known clique-windmill classifier already yields all patterns and counts and the same comparison by s=2 substitution. The compact boundary and F_5 witness are immediate arithmetic consequences and leave no independently valuable new result in this frozen claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
