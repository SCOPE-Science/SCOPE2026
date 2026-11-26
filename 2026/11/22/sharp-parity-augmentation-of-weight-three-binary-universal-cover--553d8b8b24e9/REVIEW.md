# Independent mathematical audit

## correctness

PASS

In the length-(n−1) overlap graph the fixed-weight arcs have one predecessor and one successor at every active vertex; those successors rotate the labels. Subtracting the balanced mandatory weight-three layer from any closed walk therefore forces constant auxiliary multiplicity along each weight-two necklace. The pair support hits every position triple: rotate a proposed three-one arc to put the deleted one at its end, and the weight-two arc obtained by appending zero to the same prefix shares that vertex. Conversely, a shared vertex of weight two realizes exactly such a pair. Without a hit, that triple’s necklace would be isolated, and there is more than one required necklace since binomial(n,3)>n. Mantel’s bound gives n(n−2)/4 auxiliary arcs; equality makes the complementary graph balanced complete bipartite (at equality all degrees are n/2 and the neighbors of any vertex are independent). One-step rotation cannot preserve either class individually and hence must exchange them, forcing the parity partition. The parity support is balanced and connected: {0,2,d} links the selected separation d>2 to separation 2, and every mandatory cycle attaches to a selected one. Euler traversal gives exactly the specified windows. The conclusion is uniqueness of the multiset, not the circle. A separate enumeration of all 8 and 16 auxiliary support choices at n=6,8 recovered the unique minima 26 and 68 and checked their Euler words; at n=6 it recovered 11001010100110100011100010. These finite cases are corroboration only; the uploaded verify.py was inspected, not executed.

## originality

PASS

The inspected work provides full-range cycles or optimizes a different notion of cover. No available statement gives the sharp selection cost and unique minimizing multiset here. This is a bounded best-of-knowledge assessment.

## value

PASS

This determines the exact cost of turning separate fixed-weight cycles into one circle while retaining exact-once coverage of the mandatory layer. The n²/4 saving over the complete adjacent range and the forced parity support are structurally useful, not a small-order census. The link to triangle-free extremality explains why all optimum covers have the same factors.

The dated certificate retains the supplied scientific assessment, sources and limitations.
