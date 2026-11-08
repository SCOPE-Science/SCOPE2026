# Circular bounded-gap token systems have transport-optimal sliding paths

## Finding
For integers \(k\ge2\), \(1\le a<b\), and \(ak<n<bk\), every pair of \(k\)-token placements on a labelled cycle with successive clockwise gaps in \([a,b]\) is connected by a *shortest* sequence of single-step slides that never violates the bounds. The minimum length equals the optimal circular order-preserving transportation cost. This is an exact all-pairs shortest-path formula, not merely a connectivity result.

## Assumptions and scope
Let the sites of \(C_n\) be \(\mathbb Z/n\mathbb Z\), with a token at each site of a \(k\)-subset. For increasing representatives \(0\le x_0<\cdots<x_{k-1}<n\), extend \(x_{i+k}=x_i+n\). The placement is feasible precisely when \(a\le x_{i+1}-x_i\le b\) for all indices \(i\) modulo \(k\). The graph on all feasible placements joins two if one token slides by one cycle edge to an unoccupied site while remaining feasible. The theorem assumes \(ak<n<bk\); this guarantees that no placement has every gap equal to \(a\) or every gap equal to \(b\).

For another placement \(Y\), use sorted representatives \(y_0,\ldots,y_{k-1}\) with \(y_{i+k}=y_i+n\). Define
\[
 D(X,Y)=\min_{0\le r<k}\ \min_{h\in\mathbb Z}\sum_{i=0}^{k-1}|x_i-y_{i+r}-hn|.
\]
Then \(d_{\rm slide}(X,Y)=D(X,Y)\). The integer lift parameter \(h\) is not a free physical rotation: it accounts for how a cyclically ordered matching is unwrapped. Because \(x_i\in[0,n)\) and \(y_{i+r}\in[0,2n)\) when \(0\le r<k\), the inner minimum is attained with \(h\in\{-2,-1,0,1\}\), providing an explicit \(O(k^2)\) evaluation.

## Proof
**Step 1: Lower bound by preservation of cyclic order.** No legal single-site slide can cause two tokens to exchange cyclic order, since the destination must be unoccupied and all intervening gaps remain positive. Track the tokens along any legal sequence and unwrap their integer positions continuously. At the end, their cyclic order agrees with some rotation of the listed targets, possibly translated by a common multiple of \(n\). If the resulting integer displacements are \(\delta_i\), each slide changes one position by one, so the number of moves is at least \(\sum_i|\delta_i|\ge D(X,Y)\).

**Step 2: Feasible lifts and their meet.** Fix any matching rotation \(r\) and lift \(h\). Write \(u_i=x_i\) and \(v_i=y_{i+r}+hn\), extended periodically by \(u_{i+k}=u_i+n\), \(v_{i+k}=v_i+n\). Both sequences satisfy \(a\le u_{i+1}-u_i\le b\) and the corresponding bounds for \(v\). Their coordinatewise minimum \(w_i=\min(u_i,v_i)\) satisfies the same bounds and the same period relation: the inequalities \(t_i+a\le t_{i+1}\le t_i+b\) are preserved by taking the coordinatewise minimum of two solutions. Hence \(w\) is another feasible periodic lift.

**Step 3: One-unit descent lemma.** Let \(p,q\) be feasible integer lifts with \(p_i\ge q_i\) for every \(i\), and suppose some inequality is strict. An index \(i\) with \(p_i>q_i\) can be decremented by one unless the preceding gap is exactly \(a\), or the following gap is exactly \(b\). In the first blocking case, \(q_i-q_{i-1}\ge a=p_i-p_{i-1}\) and \(q_i<p_i\) force \(q_{i-1}<p_{i-1}\). In the second case, \(q_{i+1}-q_i\le b=p_{i+1}-p_i\) forces \(q_{i+1}<p_{i+1}\). Thus a blocked active index points to an active predecessor across a gap \(a\), or to an active successor across a gap \(b\). If every active index were blocked, the finite directed dependency graph would contain a directed cycle. Its underlying graph is the cycle on the \(k\) token indices. A directed two-cycle across one gap would require that gap to equal both \(a\) and \(b\), which is impossible; for \(k=2\) the two distinct cyclic gaps give the same conclusion unless both equal the same endpoint. Any longer directed cycle must run all the way around in one direction, requiring all gaps to be \(a\) or all to be \(b\). Both are excluded by \(ak<n<bk\). Therefore an active index has a legal decrement, after which the constraints and the coordinatewise bound \(p\ge q\) persist. Induction yields a legal path from \(p\) down to \(q\) in exactly \(\sum_i(p_i-q_i)\) moves.

**Step 4: Transport-optimal path.** Apply Step 3 from \(u\) down to \(w\), then reverse a Step 3 path from \(v\) down to \(w\). The resulting path from \(u\) to \(v\) has exactly \(\sum_i|u_i-v_i|\) slides; every intermediate lift remains feasible. Choose the rotation and lift minimizing this sum. Together with Step 1 this proves equality of graph and transport distances for all pairs, and hence connectivity.

**Boundary and special case.** When \(n=ak\) (respectively \(n=bk\)) every feasible placement has every gap equal to \(a\) (respectively \(b\)), so no single-site move is legal. For a cycle's minimum independent dominating sets, their clockwise gaps are exactly two or three and their cardinality is \(\lceil n/3\rceil\). If \(n\ge5\) is not divisible by three, the strict conditions hold with \(a=2,b=3\), yielding the stated shortest-distance formula. For \(n\equiv0\pmod3\) and \(n\ge6\), the minimum configurations are frozen; the theorem does not assert their connectivity.

## Verification
Two included independently organized programs check the theorem for bounded small instances. `verify_exhaustive.py` enumerates all feasible subsets, constructs the full slide graph and uses breadth-first search from every configuration to compare each graph distance against the explicit minimized transport sum. It covers 48 parameter quadruples with positive interior slack among the displayed ranges. `verify_constructive.py` independently tests coordinatewise meets and performs the specified legal decrement construction for every order-preserving lift, across 54 parameter quadruples and 17,467 unordered configuration pairs. Exact outputs are included. These finite checks corroborate the proof; they are not its replacement.

## Relationship to prior work
Bonsma, Kamiński, and Wrochna (2014) study independent-set reachability on claw-free graphs, including cycles, and prove polynomial-time reachability rather than the constrained all-pairs metric identity stated here. Demaine et al. (2014) address sliding independent sets on trees, without these cyclic simultaneous upper and lower gap constraints. Brewster, Mynhardt, and Teshima (2023) determine the entire minimum-independent-domination reconfiguration graph of paths and cycles (including a bracelet-graph description); their Sections 3.1–3.4 classify vertices, adjacency, and Hamiltonicity but do not supply an all-pairs shortest-slide transport identity. The cycle application here is a metric refinement of their earlier structural classification. The general bounded-gap theorem does not follow from merely knowing the bracelet graph's adjacency list without an additional geodesic argument.

## Limitations
The shortest-path theorem is for **single-site, unweighted, indistinguishable token slides** with an identical gap interval imposed at every site on the cycle. No analogous assertion is made for nonuniform site-dependent bounds, other graphs, multiple-step moves, or excluded endpoint cases. Historical priority is qualified by the possibility of related hard-particle exclusion or cyclic transport results under different terminology. No independent scholarly review has been performed.

## References
Bonsma, P.; Kamiński, M.; Wrochna, M. (2014). *Reconfiguring Independent Sets in Claw-Free Graphs*, arXiv:1403.0359, first public version 2014-03-03, https://arxiv.org/abs/1403.0359.

Demaine, E. D., et al. (2014). *Linear-Time Algorithm for Sliding Tokens on Trees*, arXiv:1406.6576, first public version 2014-06-25, https://arxiv.org/abs/1406.6576.

Brewster, R. C.; Mynhardt, C. M.; Teshima, L. E. (2023). *The i-Graphs of Paths and Cycles*, arXiv:2303.08190, first public version 2023-03-14, https://arxiv.org/abs/2303.08190.
