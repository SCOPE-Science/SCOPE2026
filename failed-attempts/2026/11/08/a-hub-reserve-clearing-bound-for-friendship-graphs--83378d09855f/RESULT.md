# A hub-reserve clearing bound for friendship graphs

## Finding
For every integer \(r\ge 2\), let \(F_r\) be the friendship graph consisting of \(r\) triangles having exactly one common vertex \(h\) and otherwise disjoint vertex pairs \(\{a_i,b_i\}\), with edges \(ha_i,hb_i,a_ib_i\) for \(1\le i\le r\). A pebbling move along an edge removes two pebbles from its source and places one at its destination. A configuration is *clearable* if moves can leave exactly one pebble anywhere; it is *stackable* if moves can leave all surviving pebbles at one vertex. Write \(\operatorname{clear}(F_r)\) and \(\operatorname{stack}(F_r)\) for the least initial sizes at which every configuration has the respective property.

**Hub-reserve theorem.** Every configuration of at least \(4r-1\) pebbles with at least one pebble at \(h\) is clearable. Consequently,
\[
\operatorname{stack}(F_r)\le \operatorname{clear}(F_r)\le 4r \qquad(r\ge2).
\]
The coefficient \(4\) is attained for \(r=2,3\):
\[
\operatorname{stack}(F_2)=\operatorname{clear}(F_2)=8,
\qquad
\operatorname{stack}(F_3)=\operatorname{clear}(F_3)=12.
\]
For each of these two sizes, the only unstackable configurations of size \(4r-1\) have zero pebbles at the hub, \(2r+1\) pebbles at one peripheral vertex, zero at its mate, and one at each other peripheral vertex (\(2r\) labelled choices). This last classification is finite and verified exhaustively; it is not claimed for larger \(r\).

## Assumptions and scope
All graphs are finite, simple and undirected. Pebbles are indistinguishable nonnegative integers on labelled vertices. Moves decrease total pebble count by exactly one. The theorem treats \(r\ge2\) and makes no assumption that a maximum-weight obstruction is concentrated at one vertex. The threshold statements refer to all configurations, with no restrictions on occupancy other than those explicitly stated.

## Proof
**Local clearing moves.** Consider one peripheral pair with occupancies \((x,y)\) and a positive hub count \(H\). The following operations empty the pair, leave the hub positive, and use at most the indicated numbers of moves when \(x+y\le3\). Here \(p\to q\) denotes a legal pebbling move from vertex \(p\) to adjacent vertex \(q\).

* \((0,0)\): no moves.
* \((1,0)\) or \((0,1)\): if \(H\ge2\), use \(h\to a,a\to h\), two moves; the hub loses one pebble.
* \((2,0)\) or \((0,2)\): send the occupied endpoint to \(h\), one move.
* \((1,1)\): if \(H\ge2\), use \(h\to a,a\to b,b\to h\), three moves; the hub loses one pebble.
* \((3,0)\) or \((0,3)\): use \(a\to h,h\to a,a\to h\), three moves; the hub count is unchanged (one pebble initially at the hub suffices).
* \((2,1)\) or \((1,2)\): use \(a\to b,b\to h\) when \(a\) initially has two; two moves, increasing the hub count by one.

When \(H=1\) and the peripheral pair has one pebble or has occupancies \((1,1)\), first send one pebble to the hub from some *other* peripheral vertex carrying at least two; this costs one additional move and raises \(H\) to two. The pair then clears in at most four moves total, leaving at least one hub pebble. These sequences also work if the helper vertex belongs to a pair that remains in the graph.

**Hub-positive threshold at exact weight.** Induct on \(r\). For \(r=2\), a configuration with seven pebbles and \(H\ge2\) has a peripheral pair of weight at most two and that pair can be emptied in at most three moves. If \(H=1\), the peripheral weights sum to six. A pair of weight zero, one, or three is emptied in at most three moves, using a helper if necessary. If a pair of weight two is concentrated at one endpoint, empty it in one move. The only remaining case is peripheral weights \((2,4)\) with the two-pebble pair of type \((1,1)\); instead empty the four-pebble pair in at most three moves without requiring hub assistance: the types \((4,0)\), \((3,1)\), and \((2,2)\) need respectively two, three, and two moves, sending the surviving pebbles to the hub. In all cases the reduced graph is a single triangle with at least four pebbles. Every four-or-more-pebble configuration on \(K_3\) is clearable (the known exact result \(\operatorname{clear}(K_3)=4\)), so the base case follows.

Let \(r\ge3\), and assume the hub-positive result for \(F_{r-1}\) at every weight at least \(4(r-1)-1\). In a hub-positive configuration of total weight \(4r-1\), the peripheral pairs have total weight at most \(4r-2\); hence at least one has weight at most three. Apply the local moves to clear this pair. When \(H=1\) and a helper is required, such a helper exists outside the chosen pair: otherwise, even if every vertex of the other \(r-1\) pairs carried one pebble, the total would be at most \(1+2+2(r-1)=2r+1<4r-1\). At most four moves have been used and the hub still has a pebble. The configuration restricted to the remaining \(F_{r-1}\) therefore has at least \((4r-1)-4=4(r-1)-1\) pebbles and is clearable by induction.

**Weights larger than the hub-positive threshold.** Fix \(r\ge2\) and induct on total weight \(t\ge4r-1\). The preceding argument gives the base \(t=4r-1\). Suppose \(t\ge4r\), with a pebble at \(h\). If some peripheral vertex carries at least two pebbles, one move from it to \(h\) decreases the total to \(t-1\) and keeps the hub positive; the induction on \(t\) applies. Otherwise every peripheral vertex contains zero or one pebble, so initially \(H\ge t-2r\ge2r\). Clear each nonempty peripheral pair, using two moves for a singleton or three moves for a pair of singletons; each such clearing decreases \(H\) by one. Since there are at most \(r\) pairs, the resulting all-hub stack has at least \(r\) pebbles. If its size is at least four, the \(K_3\) result clears it; if its size is one or two it is already clearable. If its size is exactly three, at least one originally nonempty peripheral pair had *both* vertices occupied: otherwise \(H\ge t-r\ge3r\) and removing at most \(r\) singletons would leave at least \(2r\ge4\) pebbles. Reorder the clearing operations to process such a pair last, and clear its two singletons separately by two hub shuttles rather than the three-move combined operation. This uses one extra hub pebble, turning the final three-pebble hub stack into a two-pebble stack, which can be cleared by one move. The hub had at least four pebbles just before the last pair in the original plan, so both separate shuttles are legal. This completes the hub-positive theorem.

**Unconditional upper bound.** Consider an arbitrary configuration of size \(4r\). If the hub is occupied, apply the just-proved theorem. Otherwise some peripheral vertex has at least two pebbles, since \(4r>2r\), the number of peripheral vertices. Send one pebble from that vertex to the hub. The resulting configuration has weight \(4r-1\) and a positive hub, so it is clearable. Clearability implies stackability, proving both upper bounds.

**Sharp finite cases.** The source-independent finite procedure in `artifacts/verify.py` enumerates every nonnegative occupancy vector of total size \(4r-1\) and \(4r\) for \(r=2,3\). Dynamic programming on the strictly decreasing total weight tests every legal move and declares the target reached precisely when the configuration has one pebble (clearing) or one occupied vertex (stacking). It verifies that every size-\(4r\) configuration clears and that at size \(4r-1\), exactly the \(2r\) stated occupancy vectors fail stacking. Thus the upper bounds are exact in these two cases. The script is an exhaustive finite proof for these cases only; the infinite upper bound is proved independently above.

## Verification
Run `python3 artifacts/verify.py` using Python 3 with its standard library only. It constructs all labelled nonnegative pebble distributions for both target weights, enumerates all legal moves, and memoizes the clearable/stackable predicates. Expected terminal lines include `EXHAUSTIVE_FRIENDSHIP_OK 2 upper 8 nonstackable_at_previous_weight 4`, `EXHAUSTIVE_FRIENDSHIP_OK 3 upper 12 nonstackable_at_previous_weight 6`, and `VERIFY_OK`.

## Relationship to prior work
Csernák and Soukup (2026), *Stacking and clearing in graph pebbling*, introduced both parameters and proved their general existence and bounds, the exact value \(4\) for \(K_3\), and exact formulas for complete multipartite graphs and paths. These results motivate asking for the first genuinely glued-block family. Neither their listed exact graph families nor their source's inspected theorem statements give the hub-reserve lemma or the \(4r\) upper bound for friendship graphs. The friendship graphs with at least two triangles are not complete multipartite. Existing results on other invariants of friendship and windmill graphs do not imply the pebbling reachability statement.

## Limitations
No equality \(\operatorname{clear}(F_r)=4r\) or \(\operatorname{stack}(F_r)=4r\) is claimed for \(r\ge4\), even though that would be a natural next question. The finite enumeration for \(r=2,3\) cannot establish such a claim. The proof relies on sharing a single hub among triangular blades and has not been extended to higher-order clique blades or arbitrary cactus graphs. The literature comparison does not certify historical uniqueness; unindexed work is possible. Independent verification has not been performed.

## References
Csernák, T., and Soukup, L. (2026). *Stacking and clearing in graph pebbling*. arXiv:2604.22341, first posted 2026-04-24. https://arxiv.org/abs/2604.22341 . Particularly the definitions and Theorem 8.1 on complete graphs, plus their general bounds and exact-graph-family discussion.
